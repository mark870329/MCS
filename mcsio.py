#/usr/bin/python3
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
	SwitchStatus = GPIO.input(4)
	if(SwitchStatus == 0):
		print('Button press')
	else:
		print('Button released')
