import time
import board
import busio
import adafruit_bmp3xx
from Adafruit_BMP085 import BMP085

i2c = busio.I2C(board.SCL, board.SDA)
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c,address=0x76) #i2c address for bmp388
bmp.sea_level_pressure = int(bmp.pressure)
bmp2 = BMP085(0x77)

temp = 7

tempFinalBMP833 = int(bmp.temperature())
tempFinalBMP180 = int(bmp.readTemperature())

print("BMP388:")
print(str(tempFinalBMP388))
print("BMP180:")
print(str(tempFinalBMP180))
