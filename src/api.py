import requests

# Get the weather forecast for Paris
"""
response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=48.8534&longitude=2.3488&hourly=temperature_2m')
if response.status_code == 200:
    print(response.json())
"""
response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Saint-Jean-de-Luz&appid=fd5616b0f7f4515eb3c352aa850dfb54')
print(response.status_code)
if response.status_code == 200:
    print(response.json())
