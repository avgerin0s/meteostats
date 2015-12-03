import MySQLdb
import serial
from validator import Validator
from writers.db_writer import DBWriter
from writers.log_writer import LogWriter
import json
import datetime
import time
import sys

# Change according to your device
raw_input("Press Enter to start...")

print "Starting..."

default_device = '/dev/tty.HC-05-DevB'
ser = serial.Serial(default_device, 9600)

time.sleep(6)
print "Started!"

prev = []


while True:
    buf = ser.readline()
    arr = buf.split(",")

    if len(arr) > 3:
        continue

    temperature = float(arr[0])
    humidity = float(arr[1])
    luminosity = float(arr[2])

    validator = Validator(temperature, humidity, luminosity)

    if (validator.is_valid()):
        prev = [temperature, humidity, luminosity]
    else:
        if len(prev) > 0:
            arr = prev
        else:
            continue

    print ", ".join(str(x) for x in arr)

    db = DBWriter(arr[0], arr[1], arr[2])
    db.write()

    log = LogWriter(arr[0], arr[1], arr[2])
    log.write()
