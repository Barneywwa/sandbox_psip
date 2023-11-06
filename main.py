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

add_user_to(users_list)
add_user_to(users_list)
add_user_to(users_list)

for user in users_list:
    print(f'Twój znajomy {user["name"]} {user["nick"]} dodał {user["posts"]} postów!!!')