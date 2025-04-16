# app.py

from flask import Flask, render_template, request 
import requests
import json

app = Flask(__name__)

# Replace with your OpenWeatherMap API key after creation of account.
API_KEY = "51b4a7b8fc33a5a0b779ba74ce4be0ea"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forecast', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    if not city:
        return "Error: Invalid location provided."

    # Fetch weather data from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = json.loads(response.content)

    # Process the data
    temperature = data['main']['temp']
    description = data['weather'][0]['description']

    return render_template('results.html', city=city, temperature=temperature, description=description)

if __name__ == '__main__':
    app.run(debug=True)
