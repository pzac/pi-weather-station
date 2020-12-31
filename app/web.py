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
        data = normalize_row(rows[0])
        return render_template("index.html", data=data)
    except sqlite3.Error as error:
        return error
    finally:
        if (conn):
            conn.close()

@app.route("/last-hour.json")
def last_hour():
    return json.dumps(rows_where("time >= datetime('now', '-1 hour')"))

@app.route("/last-24-hours.json")
def last_24_hours():
    return json.dumps(rows_where("time >= datetime('now', '-1 day') AND (id % 12) = 0"))

@app.route("/last-week.json")
def last_week():
    return json.dumps(rows_where("time >= datetime('now', '-7 days') AND (id % 120) = 0"))

def query_to_dataset(sql):
    data = {'time': [], 'ext_temp': [], 'brightness': [], 'int_temp': [], 'bar_temp': [], 'humidity': [], 'pressure': [], 'motion': []}
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            row = normalize_row(row)

            data['time'].append(row['time'])
            data['ext_temp'].append(row['ext_temp'])
            data['brightness'].append(row['brightness'])
            data['int_temp'].append(row['int_temp'])
            data['bar_temp'].append(row['bar_temp'])
            data['humidity'].append(row['humidity'])
            data['pressure'].append(row['pressure'])
            data['motion'].append(row['motion'])
        return data
    except sqlite3.Error as error:
        return error
    finally:
        if (conn):
            conn.close()


def rows_where(conditions):
    sql = "SELECT " + fields() + " FROM data WHERE " + conditions + " ORDER BY time DESC"
    return query_to_dataset(sql)

def fields():
    return "id, datetime(time, 'localtime'), ext_temp, brightness, int_temp, bar_temp, humidity, pressure, motion"

def normalize_row(row):
    ext_temp = row[2]
    if ext_temp:
        ext_temp = ext_temp + ext_temp_offset

    out = {
        'time': row[1],
        'ext_temp': ext_temp,
        'brightness': row[3],
        'int_temp': row[4],
        'bar_temp': row[5],
        'humidity': row[6],
        'pressure': row[7],
        'motion': row[8],
    }

    return out

if __name__ == "__main__":
    app.run(host='0.0.0.0')
