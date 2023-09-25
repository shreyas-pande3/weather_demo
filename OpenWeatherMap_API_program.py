import requests #  to make HTTP requests to the OpenWeatherMap API

def get_weather(city, api_key): # function to get city name and fetching weather data from OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
        # "units" : "imperial" # for Fahrenheit
    }

    # Make an HTTP GET request to the OpenWeatherMap API with the specified parameters
    response = requests.get(base_url, params=params)

    if response.status_code == 200: # 200 indicates HTTP status code indicating the status as okay i.e. api request was successful and api has provided the requested data
        data = response.json() # Parsing the JSON response from the API
        weather_description = data['weather'][0]['description'] # Extracting weather description
        temperature = data['main']['temp'] # Extracting temperature
        humidity = data['main']['humidity'] # Extracting humidity %

        # Display weather data.
        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        # Print an error message if there was an issue with the request.
        print("Error fetching weather data. Possible causes include:")
        print("- The city name doesn't exist in the OpenWeatherMap database.")
        print("- There may be an issue with the provided API key.")
        print("- Network problems or the API service may be temporarily unavailable.")

try:
    api_key = "f93b081ce6fba39cb0ce4c7531991ce1"  # OpenWeatherMap API key
    city = input("Enter a city: ")  # Prompt the user to enter a city

    get_weather(city, api_key)  # Call the get_weather function directly

except Exception as e:
    print(f"An error occurred: {str(e)}")  # Handle exceptions and print an error message if necessary