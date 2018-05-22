import geocoder
import unicodecsv
import logging
import time
import csv

pcode=[]

g = geocoder.ip('me')
lat = float(g.lat)
lng = float(g.lng)
print (g.postal)
print (lat,lng)
