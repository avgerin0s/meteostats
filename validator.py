import MySQLdb

class Validator():
    def __init__(self, temperature, humidity, luminosity):
        self.temperature = temperature
        self.humidity = humidity
        self.luminosity = luminosity

    def is_valid(self):
        return (self.valid_temperature() and
        self.valid_humidity() and
        self.valid_luminosity())

    def valid_temperature(self):
        return -10 < self.temperature < 45

    def valid_humidity(self):
        return 0 <= self.humidity <= 100

    def valid_luminosity(self):
        return 0 <= self.luminosity <= 100
