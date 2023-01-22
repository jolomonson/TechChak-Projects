# from django.shortcuts import render
import requests
import geoip2.webservice

# Create your views here.
def weather(request):
  api_key = 'd17a1f5e7da5101c9409e9f5747b6c64'
  location = ''

  weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

  response = requests.get(weather_url)
  data = response.json()
  temperature = data["main"]["temp"]
  humidity = data["main"]["humidity"]
  weather_condition = data["weather"][0]["main"]

  client = geoip2.Client(client_id, client_secret)
  location = client.city(ip_address)

  context = {"temperature": temperature, "humidity": humidity, "weather_condition": weather_condition}
  