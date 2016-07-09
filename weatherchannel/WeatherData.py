from flask import Flask
from flask import request
from flask import render_template
from geopy.geocoders import Nominatim
from forecastiopy import *
from flask import json
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("myForm.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    geolocator = Nominatim()
    location = geolocator.geocode(text)
    api_key='03ee3543d316fc61792a04415a108cda'
    lat=location.latitude
    long=location.longitude
    fio = ForecastIO.ForecastIO(api_key, latitude=lat, longitude=long)
    current = FIOCurrently.FIOCurrently(fio)
    processed_text = location.address
    temperature=current.temperature
    data=lat,long,temperature
    data=json.dumps(data)
    return render_template('display.html', data=data)

if __name__ == '__main__':
    app.run()