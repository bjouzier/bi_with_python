import pandas as pd
import requests
from bs4 import BeautifulSoup

URL_TABLEAU='https://fr.wikipedia.org/wiki/Dijon'

try:
    resp=requests.get(URL_TABLEAU)
    resp.raise_for_status()
    """
    print (type(resp))
    print (type(resp.text))
    print (resp)
    with open("data/webscrapping-output.txt", "w", encoding="utf-8") as f:
        print(resp.text, file=f)
    """
except requests.exceptions.HTTPError as err:
    print(err)

soup = BeautifulSoup(resp.text, 'html.parser')
tableau = soup.find_all(name='table', attrs={'class': 'wikitable centre'})
dataframe = pd.read_html(str(tableau), thousands=' ', decimal=',')
print(tableau)
print(dataframe)




 
    