import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')



def request_city_api(city = "Paris"):
    # Define the city and endpoint URL
    endpoint_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
    
    # Make the request
    response = requests.get(endpoint_url)
    
    return response

def get_latitude_longitude(city) :
    
    response = request_city_api(city)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        lon = data[0]["lon"]
        lat = data[0]["lat"]
        return lon, lat
        
    else:
        print(f"Failed with status code: {response.status_code}")
        return response.status_code
        


def request_weather_api(city):
    lon,lat = get_latitude_longitude(city)
    endpoint_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    # Make the request
    response = requests.get(endpoint_url)
    
    return response
 
def get_weather(city):
    
    response = request_weather_api(city)
   
    # Check if the request was successful
    if response.status_code == 200:
        weather_data = response.json()
        description = weather_data["weather"][0]["description"]
        temp = int(round(weather_data["main"]["temp"],0))
        temp_feels_like = int(round(weather_data["main"]["feels_like"],0))
        temp_min = int(round(weather_data["main"]["temp_min"],0))
        temp_max = int(round(weather_data["main"]["temp_max"],0))
        humidity = weather_data["main"]["humidity"]
        
    
            # Create a dataframe
        df = pd.DataFrame({
            "Description": [description],
            "Temperature": [temp],
            "Feels Like": [temp_feels_like],
            "Min Temperature": [temp_min],
            "Max Temperature": [temp_max],
            "Humidity": [humidity]
        })
        print(df)
        return df
        
    else:
        print(f"Failed with status code: {response.status_code}")
        return response.status_code
    
get_weather(city = "Paris")