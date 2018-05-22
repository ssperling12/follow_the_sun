from flask import Flask, render_template, request
import requests
import geocoder

g = geocoder.ip('me')
zp = str(g.postal)
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=88901,us&appid=c2b4563e38b579109a4696ba93973a93')
json_object = r.json()
sun = json_object['weather'][0]['main']
if sun == "Clear":
    print (sun)
else:
    print ("X")
