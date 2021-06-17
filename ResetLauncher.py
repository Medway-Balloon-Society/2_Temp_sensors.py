import os
from gpiozero import Button, LED
from subprocess import call
from pathlib import Path
from time import sleep as delay;

ReturnLauncher = Button(26)
status = LED(13)
my_file = Path("launcher.sh")
lock = False

status.on()
delay(1)
status.off()
delay(1)
status.on()
delay(1)
status.off()
delay(1)
status.on()
delay(1)
status.off()
if my_file.is_dir():
    call("launcher.sh", shell = True)
    quit()
else:
	while True:
		if(ReturnLauncher.is_pressed):
			f = open("launcher.sh", "w")
			f.write("cd /\ncd home/pi/WB2\npython3 MainCode.py\ncd /")
			f.close()
			#print("pressed, commencing file operation")
			call("sh launcher.sh", shell = True)

			quit()
