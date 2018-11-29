#!/usr/bin/python3
import sys
import time
import http.client as http
import urllib
import json
import RPi.GPIO as GPIO
deviceId = "DsUObVD6"
deviceKey = "5Fv4m5XsU6cU3x60" 
def post_to_mcs(payload): 
	headers = {"Content-type": "application/json", "deviceKey": deviceKey} 
	not_connected = 1 
	while (not_connected):
		try:
			conn = http.HTTPConnection("api.mediatek.com:80")
			conn.connect() 
			not_connected = 0 
		except (httplib.HTTPException, socket.error) as ex: 
			print( "Error: %s" %ex) 
			time.sleep(10)
			 # sleep 10 seconds 
	conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers) 
	response = conn.getresponse() 
	print( response.status, response.reason, json.dumps(payload), time.strftime("%c")) 
	data = response.read() 
	conn.close() 

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
while True:
	SwitchStatus = GPIO.input(4)
	if(SwitchStatus == 0):
		print('Button press')
		time.sleep(1)
	else:
		print('Button released')
		time.sleep(1)
	payload = {"datapoints":[{"dataChnId":"SwitchStatus","values":{"value":SwitchStatus}}]} 
	post_to_mcs(payload)
