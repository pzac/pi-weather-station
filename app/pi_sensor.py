from sensorhub.hub import SensorHub

class PiSensor:
    def __init__(self):
        self.hub = SensorHub(None)

    def ext_temp(self):
        return self.hub.get_off_board_temperature()

    def humidity(self):
        return self.hub.get_humidity()

    def int_temp(self):
        return self.hub.get_temperature()

    def motion(self):
        return self.hub.is_motion_detected()

    def brightness(self):
        return self.hub.get_brightness()

    def bar_temp(self):
        return self.hub.get_barometer_temperature()

    def pressure(self):
        return self.hub.get_barometer_pressure()

