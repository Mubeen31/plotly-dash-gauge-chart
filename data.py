import serial
import csv
from datetime import datetime

# copy the port from your Arduino editor
PORT = 'COM5'
ser = serial.Serial(PORT, 9600)

while True:
        message = ser.readline()
        data = message.strip().decode()
        split_string = data.split(',')  # split string

        humidity = float(split_string[0])  # convert first part of string into float
        temperature = float(split_string[1])  # convert second part of string into float
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        # print(temperature)
        print(dt_string, humidity, temperature)

        with open("humidity_and_temperature.csv", "a") as f:
            writer = csv.writer(f, delimiter = ",")
            writer.writerow([dt_string, humidity, temperature])
