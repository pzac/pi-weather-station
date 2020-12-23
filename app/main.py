import time
import sqlite3
from pi_sensor import PiSensor
from contextlib import closing

interval = 60.0
debug = False

connection = sqlite3.connect("data.db")

sql = "INSERT INTO data(ext_temp, int_temp, humidity, motion, brightness, bar_temp, pressure) " \
      "VALUES(?, ?, ?, ?, ?, ?, ?)"

hub = PiSensor()

while True:
    try:
        ext_temp   = hub.ext_temp()
        humidity   = hub.humidity()
        int_temp   = hub.int_temp()
        motion     = hub.motion()
        brightness = hub.brightness()
        bar_temp   = hub.bar_temp()
        pressure   = hub.pressure()

        if debug:
            localtime = time.localtime()
            t = time.strftime("%I:%M:%S %p", localtime)
            print(t + "\t"+ "Int Temp: " + str(int_temp) + "C Ext Temp: " + str(ext_temp) + "C")

        with closing(connection.cursor()) as cursor:
            cursor.execute(sql, (ext_temp, int_temp, humidity, motion, brightness, bar_temp, pressure))
            connection.commit()
        time.sleep(interval)
    except IOError:
        print("Error reading from sensor")

