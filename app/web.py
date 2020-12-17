from flask import Flask
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

if __name__ == "__main__":
    app.run(host='0.0.0.0')
