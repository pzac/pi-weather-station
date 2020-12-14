import time
from sensorhub.hub import SensorHub

interval = 1.0

hub = SensorHub(None)

while True:
  localtime = time.localtime()
  t = time.strftime("%I:%M:%S %p", localtime)
  int_temp = hub.get_temperature()
  ext_temp = hub.get_off_board_temperature()
  print(t + "\t"+ "Int Temp: " + str(int_temp) + "C Ext Temp: " + str(ext_temp) + "C")
  time.sleep(interval)
