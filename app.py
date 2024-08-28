from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "ad96171a3f768a4396124d737403ac02"

def get_weatherofcity(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    return response.json()

def get_forecast(city):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

def get_weather_by_coordinates(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'     
    response = requests.get(url)
    return response.json()



@app.route('/', methods=['GET','POST'])

def index():
    weather_data = None
    forecast_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get('city')
        weather_data =  get_weatherofcity(city)
        forecast_data = get_forecast(city)

        if weather_data and 'main' not in weather_data:

            error_message = weather_data.get("message","City not found or some other error")
            weather_data = None
            forecast_data = None

    return render_template('index.html', weather=weather_data, forecast = forecast_data, error = error_message)

@app.route('/location', methods=['GET','POST'])

def location_weather():
    if request.method == 'POST':
        data = request.json
        lat = data['latitude']
        lon = data['longitude']
        weather_data = get_weather_by_coordinates(lat, lon)
    
        return jsonify(weather_data)
    else:
        return render_template('location.html')

if __name__ == '__main__':
    app.run(debug=True)



             
