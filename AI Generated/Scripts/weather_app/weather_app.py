import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("TOMORROW_IO_API_KEY")
if not API_KEY:
    raise EnvironmentError(
        "API key not found. Please set the TOMORROW_IO_API_KEY environment variable."
    )

BASE_URL = "https://api.tomorrow.io/v4/weather/forecast"

# Updated weather code to description mapping
WEATHER_CODE_MAP = {
    0: "Unknown",
    1000: "Clear, Sunny",
    1001: "Cloudy",
    1100: "Mostly Clear",
    1101: "Partly Cloudy",
    1102: "Mostly Cloudy",
    2000: "Fog",
    2100: "Light Fog",
    3000: "Light Wind",
    3001: "Wind",
    3002: "Strong Wind",
    4000: "Drizzle",
    4001: "Rain",
    4200: "Light Rain",
    4201: "Heavy Rain",
    5000: "Snow",
    5001: "Flurries",
    5100: "Light Snow",
    5101: "Heavy Snow",
    6000: "Freezing Drizzle",
    6001: "Freezing Rain",
    6200: "Light Freezing Rain",
    6201: "Heavy Freezing Rain",
    7000: "Ice Pellets",
    7101: "Heavy Ice Pellets",
    7102: "Light Ice Pellets",
    8000: "Thunderstorm",
}


def get_weather(location):
    """
    Fetch the weather forecast for a given location using Tomorrow.io API.

    Args:
        location (str): The location for which to fetch the weather forecast.

    Returns:
        dict: The weather data.
    """
    url = f"{BASE_URL}?location={location}&apikey={API_KEY}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        weather_data = response.json()
        print(weather_data)  # Print the entire JSON response for debugging
        return weather_data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def parse_forecast_data(forecast):
    """
    Parse forecast data to extract and map relevant information.

    Args:
        forecast (dict): The forecast data to parse.

    Returns:
        list: A list of parsed forecast data with descriptions.
    """
    parsed_data = []
    for interval in ["minutely", "hourly", "daily"]:
        if interval in forecast:
            for data in forecast[interval]:
                time = data.get("time")
                values = data.get("values", {})
                temp_min = values.get("temperatureMin")
                temp_max = values.get("temperatureMax")
                temperature = values.get("temperature")
                weather_code = values.get("weatherCode")
                description = WEATHER_CODE_MAP.get(weather_code, "Unknown")
                parsed_data.append(
                    {
                        "time": time,
                        "temperatureMin": temp_min,
                        "temperatureMax": temp_max,
                        "temperature": temperature,
                        "description": description,
                        "weatherCode": weather_code,
                    }
                )
    return parsed_data


def display_weather(weather_data):
    """
    Display the weather forecast in a user-friendly manner.

    Args:
        weather_data (dict): The weather data to display.
    """
    if weather_data:
        print("Weather Forecast:")
        parsed_data = parse_forecast_data(weather_data.get("timelines", {}))
        for data in parsed_data:
            print(f"Date: {data['time']}")
            if (
                data["temperatureMin"] is not None
                and data["temperatureMax"] is not None
            ):
                print(
                    f"Temperature: {data['temperatureMin']}°C - {data['temperatureMax']}°C"
                )
            elif data["temperature"] is not None:
                print(f"Temperature: {data['temperature']}°C")
            print(f"Description: {data['description']}")
            print(f"Weather Code: {data['weatherCode']}")
            print("-" * 20)
    else:
        print(
            "Unable to fetch weather data. Please check the location or try again later."
        )


def main():
    """
    Main function to run the CLI weather app.
    """
    location = input("Enter location for weather forecast: ")
    weather_data = get_weather(location)
    display_weather(weather_data)


if __name__ == "__main__":
    main()
