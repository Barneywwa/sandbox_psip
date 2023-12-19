from bs4 import BeautifulSoup
import requests
import folium


def add_user_to(users_list: list) -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('Podaj imie ?')
    posts = input('Podaj liczbę postów ?')
    city = input('Podaj miasto?')
    users_list.append({'name': name, 'nick': 'dupa', 'posts': posts})


# add_user_to(users_list)


def remove_user_from(users_list: list) -> None:
    """
    remove object from list
    :param users_list: list - user list
    :return: None
    """
    tmp_list = []
    name = input('Podaj użytkownika do usunięcia: ')
    for user in users_list:
        if user["name"] == name:
            print(f'Znaleziono użytkownika: {user}')
            tmp_list.append(user)
    print('Znaleziono użytkowników: ')
    print('0: Usuń wszystkich znalezionych użytkowników.')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek + 1}: {user_to_be_removed}')
    numer = int(input(f'Wybierz numer użytkownika do usunięcia: '))
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer - 1])


# remove_user_from(users_list)

def show_users_from(users_list: list) -> None:
    for user in users_list:
        print(f'Twój znajomy {user["name"]} {user["nick"]} dodał {user["posts"]} postów!!!')


def update_user(users_list: list[dict, dict]) -> None:
    nick_of_user = input('podaj nick użytkownika do modyfikacji')
    print(nick_of_user)
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('Znaleziono!!!')
            user['name'] = input('podaj nowe imie: ')
            user['nick'] = input('podaj nową ksywkę: ')
            user['city'] = input('podaj nowe miasto')
            user['posts'] = int(input('podaj nową liczbę postów: '))


def get_coordinates_of(city: str) -> list[float, float]:
    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')

    # POBRANIE WSPÓŁRZĘDNYCH Z TREŚCI STRONY INTERNETOWEJ

    res_html_latitude = (response_html.select('.latitude')[1].text)  # '.' - class

    # ŁOPATOLOGICZNIE MOŻNA ZROBIĆ TAK: print(res_html_latitude[23:-7])

    res_html_latitude = float(res_html_latitude.replace(',', '.'))

    # DRUGA WSPÓŁRZĘDNA

    res_html_longitude = response_html.select('.longitude')[1].text
    res_html_longitude = float(res_html_longitude.replace(',', '.'))

    return [res_html_latitude, res_html_longitude]


# for item in nazwy_miejscowosci:
# print(get_coordinates_of(item))

user = {"city": "Lublin", "name": "Mateusz", "nick": "świetlik", "posts": 1234}


# Zwrócić mapę z pinezką odnoszącą się do wskazanego użytkownika podanego z klawiatury
def get_map_of_user(user: str) -> None:
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


# Zwrócić mapę z wszystkimi użytkownikami z danej listy (znajomymi)

###RYSOWANIE MAPY
def get_map_of(users: list[dict, dict]) -> None:
    map = folium.Map(
        location=[52.3, 21.0],
        tiles="OpenStreetMap",
        zoom_start=7
    )
    for user in users:
        folium.Marker(
            location=get_coordinates_of(city=user['city']),
            popup=f'Użytkownik {user["name"]} \n'
                  f'liczba postów {user["posts"]}'
        ).add_to(map)
    map.save('mapka.html')


############################## END OF MAP ELEMENT ##############################

def gui(users_list: list) -> None:
    while True:
        print(f'MENU: \n'
              f'0: Zakończ program \n'
              f'1: Wyświetl użytkowników  \n'
              f'2: Dodaj użytkownika \n'
              f'3: Usuń użytkownika \n'
              f'4: Modyfikuj użytkownika \n'
              f'5: Wygeneruj mapę z użytkownikiem \n'
              f'6: Wygeneruj mapę ze wszystkimi użytkownikami \n'
              )

        menu_option = input('Podaj funkcję do wywołania')
        print(f'Wybrano funkcję {menu_option}')

        match menu_option:
            case '0':
                print('Kończę pracę')
                break
            case '1':
                print('Lista Użytkowników: ')
                show_users_from(users_list)
            case '2':
                print('Dodaj użytkownika: ')
                add_user_to(users_list)
            case '3':
                print('Usuń użytkownika: ')
                remove_user_from(users_list)
            case '4':
                print('Modyfikuję użytkownika')
                update_user(users_list)
            case '5':
                print('Rysuję mapę z użytkownikiem')
                user = input('podaj nazwę użytkownika do modyfikacji')
                for item in users_list:
                    if item['name'] == user:
                        get_map_of_user(item)
            case '6':
                print('Rysuję mapę ze wszystkimi użytkownikami')
                get_map_of(users_list)
