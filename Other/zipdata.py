from __future__ import print_function
from uszipcode import ZipcodeSearchEngine
search = ZipcodeSearchEngine()
import geocoder

g = geocoder.ip('me')
lat = float(g.lat)
lng = float(g.lng)
res = search.by_coordinate(lat, lng, radius=100, returns=30)
res1 = []
num2 = 0
for num1 in res:
    res1.append(res[num2]['Zipcode'])
    num2 += 1
print (res1)

zipcode = search.by_zipcode("60022")
print (zipcode)
print (zipcode.Latitude)
