from __future__ import print_function
from uszipcode import ZipcodeSearchEngine
search = ZipcodeSearchEngine()
from flask import Flask, render_template, request
import requests
import geocoder

#zp = str(60022)
#r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zp+',us&appid=c2b4563e38b579109a4696ba93973a93')
#json_object = r.json()
#sun = json_object['weather'][0]['main']
#print (sun)

num2 = 1
zp = str(60022)
while True:
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zp+',us&appid=c2b4563e38b579109a4696ba93973a93')
    json_object = r.json()
    sun = json_object['weather'][0]['main']
    if sun == "Clear":
        print(zp)
        break
    else:
        zp = res1[num2]
        num2 + 1
        continue
