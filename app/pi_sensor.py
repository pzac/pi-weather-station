from sensorhub.hub import SensorHub

class PiSensor:
    def __init__(self):
        self.hub = SensorHub(None)

    def ext_temp(self):
        try:
            return self.safe_value(self.hub.get_off_board_temperature())
        except IOError:
            return None

    def humidity(self):
        try:
            return self.safe_value(self.hub.get_humidity())
        except IOError:
            return None

    def int_temp(self):
        try:
            return self.safe_value(self.hub.get_temperature())
        except IOError:
            return None

    def motion(self):
        try:
            return self.safe_value(self.hub.is_motion_detected())
        except IOError:
            return None

    def brightness(self):
        try:
            return self.safe_value(self.hub.get_brightness())
        except IOError:
            return None

    def bar_temp(self):
        try:
            return self.safe_value(self.hub.get_barometer_temperature())
        except IOError:
            return None

    def pressure(self):
        try:
            return self.safe_value(self.hub.get_barometer_pressure())
        except IOError:
            return None

    def safe_value(self, x):
        if x == -1:
            return None
        else:
            return x
