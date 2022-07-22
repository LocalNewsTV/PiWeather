#!/usr/bin/python
import time
import requests
from sense_hat import SenseHat
sense = SenseHat()
#Hours between we want the screen to display
morning = 7
night = 22
#Gets our API Data
def call():
    key = '7d98db344ac643c69ab184637222007'
    response = requests.get('http://api.weatherapi.com/v1/current.json?key=' + key + '&q=V9A&aqi=no')
    response = response.json()
    return response
#Checks if the current time is appropriate to display data
def isAcceptable():
    timeNow = time.strftime('%H')
    if (int(timeNow) < morning and int(timeNow) > night):
        return False
    return True
#Runs once at start of program to ensure things work
def testSuite():
        data = call()
        tempF = str(data["current"]["temp_f"]) + 'F'
        tempC = str(data["current"]["temp_c"]) + 'C'
        sense.show_message(tempF + '-' + tempC, text_colour=[120, 0, 140])
#Main flow of events: Checks if its an appropriate time -> Warns if Temp is too hot -> 
def main():
    if (isAcceptable()):
        if(int(time.strftime('%M')) % 15 == 0):
            if(sense.temp > 45):
                sense.show_message(str(sense.temp)[0:4] + " warning", text_colour=[255, 0, 0])
                sense.clear(0, 0, 0)
                quit()
            data = call()
            tempF = str(data["current"]["temp_f"]) + 'F'
            tempC = str(data["current"]["temp_c"]) + 'C'
            sense.show_message(tempF + '-' + tempC, text_colour=[120, 0, 140])
#Runtime
try:
    sense.set_rotation(180)
    sense.low_light = True
    testSuite()
    while True:
       main()
       time.sleep(55)
       sense.clear(0, 0, 0)
finally:
    sense.clear(0, 0, 0)