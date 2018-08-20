from __future__ import print_function
from uszipcode import ZipcodeSearchEngine
search = ZipcodeSearchEngine()
from flask import Flask
app = Flask(__name__)
import requests
import geocoder

def zipcodelocation():
    g = geocoder.ip('me')
    zp = str(g.postal)
    return zp

def latitudelocation():
    g = geocoder.ip('me')
    lat = float(g.lat)
    return lat

def longitudelocation():
    g = geocoder.ip('me')
    lng = float(g.lng)
    return lng

def generateclosestziplist(lat,lng):
    ziplist = search.by_coordinate(lat, lng, radius=100, returns=55)
    res1 = []
    zipdistance = 0
    for num1 in ziplist:
        res1.append(ziplist[zipdistance]['Zipcode'])
        zipdistance += 1
    return res1

def findsunnyzip(zp,res1):
    num2 = 1
    zp = str(zp)
    while True:
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zp+',us&appid=c2b4563e38b579109a4696ba93973a93')
        json_object = r.json()
        sun = json_object['weather'][0]['main']
        if sun == "Clear":
            return zp
            break
        else:
            zp = res1[num2]
            num2 += 1
            if num2 < 50:
                continue
            else:
                return "No sunny coffee shops nearby"

def ziptolat(zp):
    zipcode = search.by_zipcode(zp)
    lat = zipcode.Latitude
    return lat

def ziptolng(zp):
    zipcode = search.by_zipcode(zp)
    lng = zipcode.Longitude
    return lng

def coffeeshop(lat,lng):
    r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+lng+'&radius=1500&type=restaurant&keyword=coffee&key=AIzaSyCzEUDKeEEkEWDkZc_rNskT3GVsgdf_Kf0')
    json_object = r.json()
    shop = json_object['results'][0]['name']
    return shop

@app.route("/")
def function():

    lat = 0
    lng = 0
    zp = 0
    res1 = []
    sunnylat = 0
    sunnylng = 0
    shop = ""

    lat = latitudelocation()
    lng = longitudelocation()
    zp = zipcodelocation()
    res1 = generateclosestziplist(lat,lng)
    sunnyzip = findsunnyzip(zp, res1)
    if len(sunnyzip) == 5: #statement ensures that only zip codes are returned.  If there is no sunny location, a string saying that is returned.
        sunnylat = str(ziptolat(sunnyzip))
        sunnylng = str(ziptolng(sunnyzip))
        shop = coffeeshop(sunnylat,sunnylng)
        return shop
    else:
        return sunnyzip

if __name__ == "__main__":
    app.run()
