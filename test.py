from flask import Flask, render_template, request
import requests
import geocoder

app = Flask(__name__)

@app.route('/differentlocation', methods=['POST'])
def differentlocation():
    return render_template('differentlocation.html')

@app.route('/')
def index():
    g = geocoder.ip('me')
    zp = str(g.postal)
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?='+zp+',us&appid=c2b4563e38b579109a4696ba93973a93')
    json_object = r.json()
    print (json_object)
    sun = json_object['weather'][0]['main']
    if sun == "clear":
        return render_template('index.html',sunny = sun)
    else:
        return render_template('index.html',sunny = "X")

if __name__ == '__main__':
    app.run(debug=True)
