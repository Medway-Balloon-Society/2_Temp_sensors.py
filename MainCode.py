import time
import board
import busio
import adafruit_bmp3xx
import csv

from picamera import PiCamera, Color
       
from subprocess import call

import datetime as dt

from gpiozero import Button, LED


import os
from pathlib import Path

from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
bmp.sea_level_pressure = int(bmp.pressure)

altitude = 5
pressure = 4
temp = 7

camera = PiCamera()

my_file = Path("launcher.sh")

startLED = LED(13)

cameraStartRecordingButton = Button(21)
  
recording = False

startLED.on()
sleep(3)
startLED.off()

if my_file.is_dir():
    os.remove("launcher.sh")

def sensor_write(Saltitude, Spressure, Stemp):
    with open ('Readings/alt.csv', 'a') as log:
        log_writer = csv.writer(log)
        log_writer.writerow({Saltitude})
        
    with open ('Readings/press.csv', 'a') as log:
        log_writer = csv.writer(log)
        log_writer.writerow({Spressure})
        
    with open ('Readings/temp.csv', 'a') as log:
        log_writer = csv.writer(log)
        log_writer.writerow({Stemp})
        
 #   print(Saltitude, Spressure, Stemp)
    

while(recording == False):
    #print("waiting for button press")
    if(cameraStartRecordingButton.is_pressed):
        recording = True

file = open("Readings/alt.csv", "r+")
file.truncate
file.close

file = open("Readings/press.csv", "r+")
file.truncate
file.close

file = open("Readings/temp.csv", "r+")
file.truncate
file.close

camera.resolution = (1920, 1080)
camera.framerate = 24
camera.start_recording('Videos/Recording.h264', quality = 20, bitrate = 750000)
startLED.on()
sleep(1)
startLED.off()
sleep(1)
startLED.on()
sleep(1)
startLED.off()
sleep(1)
startLED.on()
sleep(1)
startLED.off()
sleep(1)
startLED.on()
sleep(1)
startLED.off()
sleep(1)
startLED.on()
sleep(1)
startLED.off()
sleep(1)
startLED.on()
sleep(1)
startLED.off()


start = dt.datetime.now()
while (dt.datetime.now() - start).seconds < 120:

    altitude = int(bmp.altitude)
    pressure = int(bmp.pressure)
    temp = int((bmp.temperature * 1.8) + 32)
    
    sensor_write(altitude, pressure, temp)
            
    camera.annotate_text = str(temp) + ' F' + '                                  ' + str(altitude) + ' m' + '                                   ' + str(pressure) + ' hpa'
    camera.annotate_foreground = Color('white')
    camera.annotate_text_size = 40
    print((dt.datetime.now() - start).seconds)
camera.wait_recording(10)
	
camera.close()
print("Congrats on the leaf Nate! Also thanks to Sid for... THONK")
#call("sudo shutdown -h now", shell = True)


