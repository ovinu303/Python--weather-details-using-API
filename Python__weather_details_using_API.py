import requests

api_key = "YOUR_API_KEY_HERE"
weather_url = "https://weatherapi-com.p.rapidapi.com/current.json"

city_name = input("Enter city name: ")

headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
}

params = {
    "q": city_name,
}

weather_response = requests.get(weather_url, headers=headers, params=params)

weather_data = weather_response.json()

if "error" not in weather_data:
    location = weather_data["location"]
    current = weather_data["current"]
    temp_c = current["temp_c"]
    feelslike_c = current["feelslike_c"]
    humidity = current["humidity"]
    pressure_mb = current["pressure_mb"]
    condition = current["condition"]
    text = condition["text"]
    localtime = location["localtime"]
    currentLocation = location["name"]
    country = location["country"]

    print(f"\nLocation: {currentLocation}")
    print(f"Country: {country}\n")
    print(f"Current Time: {localtime}")
    print(f"Temperature: {temp_c}\u00B0C")
    print(f"Feels Like: {feelslike_c}\u00B0C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure_mb} hPa")
    print(f"Weather Description: {text}")
else:
    print("City not found")
