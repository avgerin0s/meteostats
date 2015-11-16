import serial
from writers.db_writer import DBWriter
from writers.log_writer import LogWriter
import json
import datetime

# Change according to your device
ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

while True:
    buf = ser.readline()
    arr = buf.split(",")
    print buf

    db = DBWriter(arr[0], arr[1], arr[2])
    db.write()

    log = LogWriter(arr[0], arr[1], arr[2])
    log.write()
