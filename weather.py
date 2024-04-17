import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    city = "Islamabad"
    api_key = "https://api.openweathermap.org/data/2.5/weather?q=Islamabad&appid=YOUR_API_KEY&units=metric"  # Replace "YOUR_API_KEY" with your actual API key from OpenWeatherMap
    weather_data = get_weather(api_key, city)

    if weather_data["cod"] == 200:
        # Print weather data
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        print(f"Weather in {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
   

if __name__ == "__main__":
    main()
