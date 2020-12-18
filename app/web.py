from flask import Flask,json
from flask import render_template
import sqlite3

app = Flask(__name__, template_folder="./templates")

@app.route("/")
def index():
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        query = "SELECT * FROM data ORDER BY time DESC LIMIT 1"
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
    sql = "SELECT * FROM data WHERE time >= datetime('now', '-1 hour') ORDER BY time DESC"
    data = query_to_dataset(sql)
    return json.dumps(data)

@app.route("/last-24-hours.json")
def last_24_hours():
    sql = "SELECT * FROM data WHERE time >= datetime('now', '-1 day') AND (id % 12) = 0 ORDER BY time DESC"
    data = query_to_dataset(sql)
    return json.dumps(data)

def query_to_dataset(sql):
    data = {'time': [], 'ext_temp': [], 'brightness': [], 'int_temp': [], 'bar_temp': [], 'humidity': [], 'pressure': [], 'motion': []}
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            data['time'].append(row[1])
            data['ext_temp'].append(row[2])
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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
