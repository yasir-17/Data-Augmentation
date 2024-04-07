import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry
from geopy.geocoders import Nominatim
from datetime import datetime
import math

def get_lat_long(address):
    import requests

    # Replace YOUR_API_KEY with your actual API key. Sign up and get an API key on https://www.geoapify.com/ 
    API_KEY = "621feb2db48748e8ad1044b2a9acb331"

    # Build the API URL
    url = f"https://api.geoapify.com/v1/geocode/search?text={address}&limit=1&apiKey={API_KEY}"

    # Send the API request and get the response
    response = requests.get(url)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()

        # Extract the first result from the data
        if (len(data["features"]) == 0):
            latitude = None
            longitude = None
        else :    
            result = data["features"][0]
            # Extract the latitude and longitude of the result
            latitude = result["geometry"]["coordinates"][1]
            longitude = result["geometry"]["coordinates"][0]
        return latitude, longitude
    else:
        print(f"Request failed with status code {response.status_code}")
        return None, None

    
def get_side_of_town(loc, center_latitude=35.220833, center_longitude=-97.443611):
    
    latitude, longitude = get_lat_long(loc)
    if (latitude == None or longitude == None):
        return "Cannot extract latitude or longitude"
    # Calculate the difference in latitude and longitude
    delta_lat = float(latitude) - center_latitude
    delta_lon = float(longitude) - center_longitude
    
    # Calculate the angle relative to the center of town
    angle = math.degrees(math.atan2(delta_lon, delta_lat))
    
    # Convert angle to compass direction
    compass_directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
    direction_index = round(angle / 45) % 8
    return compass_directions[direction_index]

def get_weather_code(loc, date_time):
    lat, lon = get_lat_long(loc)
    
    # Set the start and end dates for the Open-Meteo API
    incident_time = datetime.strptime(date_time, "%m/%d/%Y %H:%M")
    start_date = incident_time.date()
    end_date = incident_time.date()
    time = incident_time.hour 

    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": "26.27332703176929",
        "longitude": "-81.6216394463461",
        "start_date": start_date,
        "end_date": end_date,
        "hourly": ["temperature_2m", "precipitation", "weather_code"]
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]

    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_precipitation = hourly.Variables(1).ValuesAsNumpy()
    hourly_weather_code = hourly.Variables(2).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
        end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "left"
    )}
    hourly_data["temperature_2m"] = hourly_temperature_2m
    hourly_data["precipitation"] = hourly_precipitation
    hourly_data["weather_code"] = hourly_weather_code

    hourly_dataframe = pd.DataFrame(data = hourly_data)
    return int(hourly_dataframe.iloc[time]['weather_code'])


