import time
import sqlite3
from sensorhub.hub import SensorHub
from contextlib import closing

interval = 30.0
hub = SensorHub(None)

try:
    connection = sqlite3.connect("data.db")
    sql = "INSERT INTO data(ext_temp, int_temp, humidity, motion, brightness, bar_temp, pressure) VALUES(?, ?, ?, ?, ?, ?, ?)"

    while True:
        ext_temp   = hub.get_off_board_temperature()
        humidity   = hub.get_humidity()
        int_temp   = hub.get_temperature()
        motion     = hub.is_motion_detected()
        brightness = hub.get_brightness()
        bar_temp   = hub.get_barometer_temperature()
        pressure   = hub.get_barometer_pressure()

        localtime = time.localtime()
        t = time.strftime("%I:%M:%S %p", localtime)
        print(t + "\t"+ "Int Temp: " + str(int_temp) + "C Ext Temp: " + str(ext_temp) + "C")

        with closing(connection.cursor()) as cursor:
            cursor.execute(sql, (ext_temp, int_temp, humidity, motion, brightness, bar_temp, pressure))
            connection.commit()

        time.sleep(interval)
except sqlite3.Error as error:
    print("Failed to insert data", error)
finally:
    if (connection):
        connection.close()
        print("The SQLite connection is closed")
