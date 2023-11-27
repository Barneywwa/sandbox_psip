### BEAUTIFULSOUP4

from bs4 import BeautifulSoup
import requests
import re

nazwy_miejscowosci = ['Opoczno','Gdańsk','Lublin']
#POBRANIE STRONY INTERNETOWEJ
def get_coordinates_of(city:str)->list[float,float]:
    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')

    #POBRANIE WSPÓŁRZĘDNYCH Z TREŚCI STRONY INTERNETOWEJ

    res_html_latitude = (response_html.select('.latitude')[1].text) #'.' - class

    #ŁOPATOLOGICZNIE MOŻNA ZROBIĆ TAK: print(res_html_latitude[23:-7])

    res_html_latitude = float(res_html_latitude.replace(',','.'))

    #DRUGA WSPÓŁRZĘDNA

    res_html_longitude = response_html.select('.longitude')[1].text
    res_html_longitude = float(res_html_longitude.replace(',','.'))

    return [res_html_latitude, res_html_longitude]

for item in nazwy_miejscowosci:
    print(get_coordinates_of(item))