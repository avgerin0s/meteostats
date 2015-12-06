import matplotlib.pyplot as plt
import MySQLdb
from MySQLdb import cursors
import matplotlib.dates
import datetime
import numpy as np

conn = MySQLdb.connect("localhost", "root", "root", "meteo",
        cursorclass=cursors.DictCursor)

cursor = conn.cursor()
query = "SELECT * FROM metrics"
cursor.execute(query)
data = cursor.fetchall()

raw_dates = []
temp = []
hum = []
lum = []

for entry in data:
    raw_dates.append(entry["date"])
    temp.append(entry["temperature"])
    hum.append(entry["humidity"])
    lum.append(entry["luminosity"])

x = np.array(raw_dates)
plt.plot(x, temp)
plt.plot(x, hum)
plt.plot(x, lum)
plt.legend(['temperature', 'humidity', 'luminosity'])
plt.show()
