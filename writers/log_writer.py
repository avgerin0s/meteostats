import json
import datetime

class LogWriter():
    def __init__(self, temperature, humidity, luminosity):
        self.temperature = float(temperature)
        self.humidity = float(humidity)
        self.luminosity = float(luminosity)

    def message(self):
        return "Temperature: " + temperature + " Humidity: " + humidity + " Luminosity: " + luminosity

    def timestamp(self):
        return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')


    def write(self):
        """
        Write to the log file
        """

        dict = {
                "message": message(),
                "@timestamp": timestamp(),
                "temperature": temperature,
                "humidity": humidity,
                "luminosity": luminosity
                }

        f = open('output.txt', 'a')
        json.dump(dict, f)
        f.write("\n")
        f.close()
