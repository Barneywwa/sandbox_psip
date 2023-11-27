### BEAUTIFULSOUP4

from bs4 import BeautifulSoup
import requests
import folium
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

#for item in nazwy_miejscowosci:
    #print(get_coordinates_of(item))


#Zwrócić mapę z pinezką odnoszącą się do wskazanego użytkownika podanego z klawiatury

#Zwrócić mapę z wszystkimi użytkownikami z danej listy (znajomymi)

###RYSOWANIE MAPY
city = get_coordinates_of(city='Opoczno')
map = folium.Map(
    location=city,
    tiles="OpenStreetMap",
    zoom_start=7
)
for item in nazwy_miejscowosci:
    folium.Marker(
        location=get_coordinates_of(city=item),
        popup='GEOINFORMATYKA RZĄDZI OU YEAHH🚀'
    ).add_to(map)
map.save('mapka.html')