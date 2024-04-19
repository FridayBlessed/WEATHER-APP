## API

An ```API``` or Application Programming Interface, is a framework of protocols and tools that enables software applications to communicate with each other, facilitating data exchange and integration between various systems and services...

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##                                                                              WEATHER APP PROJECT

Cases

- The weather application must have a fully functional backend, that stores weather information of different locations.

- The user is provided with a search feature, where he/she can make requests based on a request parameter as provided on the free weather api eg: longitude and latitude, city name, postal code etc.

- Every requested  weather data should be saved to the database, make new requests only when such data does not already exists in the database, or the existing data is at least one day old.

- Raise an error when an invalid location or data is provided.

### Optional

- Request and show the users weather data based on his/her location (Javascript is required for this)...

Free Weather Api: 

- [WeatherApi](https://www.weatherapi.com/)

Alternative Api:
- [OpenWeather](https://openweathermap.org/)

## GUIDE ON HOW TO GET THE APPLICATION RUNNING

- Make sure the Flask and python is already installed on your computer, if you dont have python, you can download from their official website https://www.python.org, and also install flask, using the command ```pip install Flask``` on your terminal

- Create a new file and name it ```weather.py```, import the following modules ```from flask import Flask```, ```render_template```, request
```import requests``` to make HTTP Requests
import json

- Then create an instance of the flask class using the code ```app = Flask(__name__)```

- Replace the ```API_KEY``` Variable, with your own personal API Key, after creation of account on the website Https://www.Openweathermap.org

- Create a new folder named `templates`, in the same directory as `weather.py`, this folder will now contain two files `Index.html` & results.html.

- ```@app.route('/')
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
    ```
- The following code above, retrieves weather data from OpenweatherMap API, and make HTTP request to OpenweatherMap API, 

- Run the flask application by inputting the code ```python weather.py``` on your command prompt or terminal. The application will now start running on your computer, you can access it on your preferred browser by running `http://localhost:5000`
