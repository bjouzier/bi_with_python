import json
import requests

url = 'https://api-adresse.data.gouv.fr/search/?q=Tuiliers&limit=3'
with requests.Session() as session:
    try:
        response = session.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            data=response.json()['query']
            print(type(data))
            print(json.dumps(data, indent=4))
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
