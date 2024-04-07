import unittest
from src.location_weather import get_weather_code, get_side_of_town

class TestLocationWeather(unittest.TestCase):
    def test_get_weather_code(self):
        # Define test location and date_time
        loc = "2400 W BROOKS ST"
        date_time = "3/3/2024 0:04"

        # Call the function
        weather_code = get_weather_code(loc, date_time)

        # Assertions
        self.assertEqual(weather_code, 1)  # Check if weather code is equal to 1

    def test_get_side_of_town(self):
        # Define test location
        loc = "1898 LEGACY PARK DR"

        # Call the function
        side_of_town = get_side_of_town(loc)

        # Assertions
        self.assertEqual(side_of_town, "NW")  # Check if side of town is "NW"

if __name__ == '__main__':
    unittest.main()
