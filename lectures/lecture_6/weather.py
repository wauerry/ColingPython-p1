import requests


class WeatherForecast:

    def __init__(self):
        self._city_cache = {}

    def get(self, city):

        if city in self._city_cache:
            return self._city_cache[city]

        base_url = "https://www.metaweather.com/api/"
        woeid = requests.get(base_url + f"/location/search/?query={city}").json()[0]["woeid"]
        forecast = requests.get(base_url + f"/location/{woeid}").json()["consolidated_weather"]
        forecast = {item["applicable_date"]: item["max_temp"] for item in forecast}

        self._city_cache[city] = forecast

        return forecast


class CityInfo:

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or WeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)


def main():

    city = "St Petersburg"
    weather_forecast = WeatherForecast()
    for _ in range(5):
        city_info = CityInfo(city, weather_forecast)
        forecast = city_info.weather_forecast()
        print(forecast)


if __name__ == "__main__":
    main()
