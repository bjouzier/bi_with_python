import requests

with requests.Session() as session:
    try:
        response = session.get('http://api.openweathermap.org/data/2.5/weather?q=Saint-Jean-de-Luz&appid=fd5616b0f7f4515eb3c352aa850dfb54')
        response.raise_for_status()
        if response.status_code == 200:
            print(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
