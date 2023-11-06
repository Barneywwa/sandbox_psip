from dane import users_list

def add_user_to(users_list:list) -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('Podaj imie ?')
    posts = input('Podaj liczbę postów ?')
    users_list.append({'name': name, 'nick':'dupa', 'posts': posts})

#   add_user_to(users_list)

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

remove_user_from(users_list)

for user in users_list:
    print(f'Twój znajomy {user["name"]} {user["nick"]} dodał {user["posts"]} postów!!!')