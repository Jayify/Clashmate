import requests
import config # config.py file with auth_key

headers = {
    'Accept': 'application/json',
    'authorization': config.auth_key
}


def get_user(player_tag):
    player = player_tag.replace('#', '%23')
    response = requests.get('https://api.clashofclans.com/v1/players/'+player, headers = headers)
    user_json = response.json() # convert object to json
    return user_json['name']



def get_clan():
    response = requests.get('https://api.clashofclans.com/v1/clans/%2329R2GLL89', headers = headers)
    for member in response.json()['memberList']:
        print(get_user(member['tag']))

get_clan()