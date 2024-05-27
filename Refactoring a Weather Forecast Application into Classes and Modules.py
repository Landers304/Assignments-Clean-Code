#Task 1:



class WeatherDataFetcher:
    def fetch_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        return weather_data.get(city, {"city": city, "temperature": None, "condition": None, "humidity": None})


class WeatherDataParser:
    def parse_weather_data(self, data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data.get("city")
        temperature = data.get("temperature")
        condition = data.get("condition")
        humidity = data.get("humidity")
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"


class WeatherForecast:
    def __init__(self):
        self.data_fetcher = WeatherDataFetcher()
        self.data_parser = WeatherDataParser()

    def get_weather_forecast(self, city):
        data = self.data_fetcher.fetch_weather_data(city)
        return self.data_parser.parse_weather_data(data)


class UserInterface:
    def __init__(self):
        self.weather_forecast = WeatherForecast()

    def main(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.weather_forecast.get_weather_forecast(city)
            else:
                data = self.weather_forecast.data_fetcher.fetch_weather_data(city)
                forecast = self.weather_forecast.data_parser.parse_weather_data(data)
            print(forecast)


if __name__ == "__main__":
    ui = UserInterface()
    ui.main()
