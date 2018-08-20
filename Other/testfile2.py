from __future__ import print_function
from uszipcode import ZipcodeSearchEngine
search = ZipcodeSearchEngine()
import requests
import geocoder


zp = 94110
res1 = ['94114', '94117', '94110', '94131', '94102', '94103', '94115', '94122', '94118', '94107', '94127', '94112', '94109', '94108', '94129', '94104', '94158', '94123', '94134', '94105', '94111', '94116', '94124', '94133', '94121', '94132', '94005', '94014', '94130', '94015']

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
            print (num2)
            zp = res1[num2]
            num2 += 1
            if num2 < 25:
                continue
            else:
                return "No sunny coffee shops nearby"

print (findsunnyzip(zp,res1))
