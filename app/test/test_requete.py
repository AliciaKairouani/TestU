from app import requete
import pandas as pd

def test_request_city_api() :
    response = requete.request_city_api("Paris") 
    assert response.status_code == 200
    
    
def test_get_latitude_longitude() :
    lon,lat = requete.get_latitude_longitude("Paris")
    assert type(lon) == int or float
    assert type(lat) == int or float 


def test_request_weather_api():
    response = requete.request_weather_api("Paris")
    assert response.status_code == 200
 
 
def test_get_weather():
    response = requete.get_weather("Paris")
    assert isinstance(response, pd.DataFrame)
    
    
