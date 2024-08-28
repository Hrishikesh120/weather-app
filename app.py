from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "ad96171a3f768a4396124d737403ac02"

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    return response.json()

@app.route('/', methods=['GET','POST'])

def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get('city')
        weather_data =  get_weather(city)

        if weather_data and 'main' not in weather_data:

            error_message = weather_data.get("message","City not found or some other error")
            return render_template('index.html',weather = weather_data, error = error_message)

    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)



             
