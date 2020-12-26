from flask import Flask,json
from flask import render_template
import sqlite3

app = Flask(__name__, template_folder="./templates")

ext_temp_offset = -2

@app.route("/")
def index():
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        query = "SELECT " + fields() + " FROM data ORDER BY time DESC LIMIT 1"
        cursor.execute(query)
        rows = cursor.fetchall()
        return render_template("index.html", data=rows[0])
    except sqlite3.Error as error:
        return error
    finally:
        if (conn):
            conn.close()

@app.route("/last-hour.json")
def last_hour():
    return rows_where("time >= datetime('now', '-1 hour')")

@app.route("/last-24-hours.json")
def last_24_hours():
    return rows_where("time >= datetime('now', '-1 day') AND (id % 12) = 0")

@app.route("/last-week.json")
def last_week():
    return rows_where("time >= datetime('now', '-7 days') AND (id % 120) = 0")

def query_to_dataset(sql):
    data = {'time': [], 'ext_temp': [], 'brightness': [], 'int_temp': [], 'bar_temp': [], 'humidity': [], 'pressure': [], 'motion': []}
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            data['time'].append(row[1])

            ext_temp = row[2]
            if ext_temp:
                ext_temp = ext_temp + ext_temp_offset

            data['ext_temp'].append(ext_temp)

            data['brightness'].append(row[3])
            data['int_temp'].append(row[4])
            data['bar_temp'].append(row[5])
            data['humidity'].append(row[6])
            data['pressure'].append(row[7])
            data['motion'].append(row[8])
        return data
    except sqlite3.Error as error:
        return error
    finally:
        if (conn):
            conn.close()


def rows_where(conditions):
    sql = "SELECT " + fields() + " FROM data WHERE " + conditions + " ORDER BY time DESC"
    data = query_to_dataset(sql)
    return json.dumps(data)

def fields():
    return "id, datetime(time, 'localtime'), ext_temp, brightness, int_temp, bar_temp, humidity, pressure, motion"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
