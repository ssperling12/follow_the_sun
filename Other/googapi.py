import requests
import geocoder

g = geocoder.ip('me')
lat = str(g.lat)
lng = str(g.lng)
r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+lng+'&radius=1500&type=restaurant&keyword=coffee&key=AIzaSyCzEUDKeEEkEWDkZc_rNskT3GVsgdf_Kf0')
json_object = r.json()
shop = json_object['results'][0]['name']
print (shop)
