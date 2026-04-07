import requests

API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key

city = input("Enter city name: ")   

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)


if response.status_code == 200:
    weather_data = response.json()
    weather_list = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']

    temp_min = weather_data['main']['temp_min']
    temp_max = weather_data['main']['temp_max']

    print(f"Weather in {city}: {weather_list}, Temperature: {temperature}°C")
    print(f"Min Temperature: {temp_min}°C, Max Temperature: {temp_max}°C")

else:
    print("city not found.")   