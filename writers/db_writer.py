import MySQLdb

class DBWriter():
    def __init__(self, temperature, humidity, luminosity):
        self.temperature = temperature
        self.humidity = humidity
        self.luminosity = luminosity

    def write(self):
        """
        Writes the metric record to the database
        """

        db = MySQLdb.connect("localhost", "root", "root", "meteo")
        cursor = db.cursor()

        insertion_statement = "INSERT INTO metrics \
                (temperature, humidity, luminosity) \
                values(%f, %f, %f)" % (float(self.temperature), float(self.humidity), float(self.luminosity))

        cursor.execute(insertion_statement)
        db.commit()

        db.close()
