import requests
import config # config.py file with auth_key

headers = {
    'Accept': 'application/json',
    'authorization': config.auth_key
}

def get_clan():
    response = requests.get('https://api.clashofclans.com/v1/clans/%2329R2GLL89', headers = headers)
    for member in response.json()['memberList']:
        print(member['name'])

get_clan()