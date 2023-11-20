def add_user_to(users_list:list) -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('Podaj imie ?')
    posts = input('Podaj liczbę postów ?')
    users_list.append({'name': name, 'nick':'dupa', 'posts': posts})

#add_user_to(users_list)


def remove_user_from(users_list:list) -> None:
    """
    remove object from list
    :param users_list: list - user list
    :return: None
    """
    tmp_list=[]
    name = input('Podaj użytkownika do usunięcia: ')
    for user in users_list:
        if user ["name"] == name:
            print(f'Znaleziono użytkownika: {user}')
            tmp_list.append(user)
    print('Znaleziono użytkowników: ')
    print('0: Usuń wszystkich znalezionych użytkowników.')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek+1}: {user_to_be_removed}')
    numer = int(input(f'Wybierz numer użytkownika do usunięcia: '))
    if numer == 0:
        for user in tmp_list:
             users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer-1])

#remove_user_from(users_list)

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
            user['posts'] = int(input('podaj liczbę postów: '))

def gui(users_list:list) -> None:
    while True:
        print(f'MENU: \n'
              f'0: Zakończ program \n'
              f'1: Wyświetl użytkowników  \n'
              f'2: Dodaj użytkownika \n'
              f'3: Usuń użytkownika \n'
              f'4: Modyfikuj użytkownika'
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

