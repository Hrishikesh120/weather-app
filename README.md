# Weather App

## Overview
The Weather App is a simple web application built using Python and Flask that allows users to get current weather information for any city and their current location. The app also provides a 5-day weather forecast and displays relevant weather icons to enhance the user experience.

## Features
- **Current Weather by City**: Enter a city name to get the current weather, including temperature, humidity, wind speed, and a brief description.
- **Location-Based Weather**: Fetch the current weather based on the user's geographic location using the browser's geolocation API.
- **5-Day Weather Forecast**: View a 5-day forecast with detailed weather information updated every 3 hours.
- **Info Button**: Provides information about the Product Manager Accelerator program.

## Developer
Developed by: **Hrishikesh Karanth Puttur**

## How to Run the Project

### Clone the Repository:
```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app

### Set Up a Virtual Environment:
```bash
python -m venv weather-app-env
source weather-app-env/bin/activate
# On Windows: weather-app-env\Scripts\activate

Install Required Libraries:
```bash pip install -r requirements.txt ```

Run the Application:
```bash python app.py ```

Open the app in your browser: Navigate to http://127.0.0.1:5000/ to access the weather app.

Dependencies
Python 3.x
Flask
Requests
How It Works
City-Based Weather: The user inputs a city name, and the app fetches weather data from the OpenWeatherMap API.
Location-Based Weather: The user clicks a button to fetch weather data based on their current location using the browser's geolocation API.
5-Day Forecast: The app retrieves a 5-day forecast from the OpenWeatherMap API, displaying temperature, humidity, and a brief weather description.
Info Button: Clicking the info button displays a description of the PM Accelerator program.
API Used
This application uses the OpenWeatherMap API to fetch current weather data and forecasts.

License
This project is licensed under the MIT License. ```
