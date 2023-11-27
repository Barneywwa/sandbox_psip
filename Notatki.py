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

user = {"city": "Lublin", "name":"Mateusz", "nick": "świetlik", "posts": 1234}
#Zwrócić mapę z pinezką odnoszącą się do wskazanego użytkownika podanego z klawiatury
def get_map_of(user:str)->None:
    city = get_coordinates_of(user["city"])
    map = folium.Map(
        location=city,
        tiles="OpenStreetMap",
        zoom_start=14
    )
    folium.Marker(
        location=city,
        popup=f'Tu rządzi {user["name"]} z GEOINFORMATYKI 2023\n OU YEEEEAAAAHHHH🚀'
        ).add_to(map)
    map.save(f'mapka_{user["name"]}.html')

get_map_of(user)
#Zwrócić mapę z wszystkimi użytkownikami z danej listy (znajomymi)

###RYSOWANIE MAPY
city = get_coordinates_of(city='Opoczno')
map = folium.Map(
    location=city,
    tiles="OpenStreetMap",
    zoom_start=14
)
for item in nazwy_miejscowosci:
    folium.Marker(
        location=get_coordinates_of(city=user['city']),
        popup=f'Użytkownik {user["name"]} \n'
            f'liczba postów {user["posts"]}'
    ).add_to(map)
map.save('mapka.html')

from dane import users_list

get_map_of(users_list)

from dane import users_list