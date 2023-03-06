import serial
import time

arduino = serial.Serial("COM3", 9600) #ustawienie komunikacji portu com3 komputera z płytką
time.sleep(2) #ustawienie opóźnienia pracy programu 

while True:
    data = arduino.readline()[0:4]
    if data:
        print(data)
