import requests,json,os
from dotenv import load_dotenv
load_dotenv(dotenv_path="/workspaces/Python/Experiments/api-key.env")
key = os.getenv("API_KEY")
print(key)
if not key:
    print("Error : API key not found. Please set the api_weather key")
    exit()
city = input("Enter your City: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

response = requests.get(url)
result = response.json()
with open("myweather.json","w") as f1:
    json.dump(result,f1,indent=4)
with open("myweather.json","r") as f2:
    data = json.load(f2)
    celsius=data["main"]["temp"] - 273.15
    print(f"{city} temperature in Celsius is {celsius:.2f}°C")
    print(f"{city} humidity is {data["main"]["humidity"]}")
    print(f"{city} pressure is {data["main"]["pressure"]}")
    print(f"{city} wind speed is {data["wind"]["speed"]} Km/Hr")