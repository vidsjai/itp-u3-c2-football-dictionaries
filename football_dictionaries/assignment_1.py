from football_dictionaries import squads_data

def players_as_dictionaries(squads_list):
    users = []
    for user in squads_list:
        user_dict = {

            'number': user[0],
            'position': user[1],
            'name': user[2],
            'date_of_birth': user[3],
            'caps': user[4],
            'club': user[5],
            'country': user[6],
            'club_country': user[7],
            'year': user[8],
        }
        users.append(user_dict)
    return users