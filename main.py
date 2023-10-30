from dane import users_list

for user in users_list:
    print(f'Twój znajomy {user["name"]} {user["nick"]} dodał {user["posts"]} postów!!!')