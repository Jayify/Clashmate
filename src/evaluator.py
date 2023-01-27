import requests
import config # config.py file with auth_key
import time

headers = {
    'Accept': 'application/json',
    'authorization': config.auth_key
}


def get_user(player_tag):
    player = player_tag.replace('#', '%23')
    # convert tag to correct format
    response = requests.get('https://api.clashofclans.com/v1/players/'+player, headers = headers)
    # convert object to json
    user_json = response.json() 
    # pull out useful stats
    hall = user_json['townHallLevel']
    trophies = user_json['trophies']
    war_stars = user_json['warStars']
    donations = user_json['donations']
    donations_received = user_json['donationsReceived']
    clan_capital = user_json['clanCapitalContributions']
    if 'league' not in user_json:
        league = 0
    else:
        league = user_json['league']['id']-29000000
    #set low default value for 0 values
    if donations == 0:
        donations = 1
    if war_stars == 0:
        war_stars = 1
    if clan_capital == 0:
        clan_capital = 1
    if league == 0:
        league = 1
    # calculate rating
    rating = round((hall)  + (trophies/300) +  (donations/100) + (war_stars/100) + (clan_capital/25000) + (league/3), 2)
    # print(user_json['name'], "hall", hall, "trophies", (trophies/300), "donations", (donations/100), "war", 
    #(war_stars/100), "capital", (clan_capital/25000), "league", (league/3))
    # return player name and rating
    return user_json['name'], rating


def sortFunc(e):
    return e[1]


def get_clan():
    response = requests.get('https://api.clashofclans.com/v1/clans/%2329R2GLL89', headers = headers)
    members = []
    print('----- Evaluating clan: "' + response.json()['name'] + '" with ' + str(len(response.json()['memberList'])) + ' members -----')
    for member in response.json()['memberList']:
        members.append(get_user(member['tag']))
    members.sort(key=sortFunc) # order by rating
    members.reverse() # highest rating first
    print()
    print('----- Sorted by rating -----')
    for member in members:
        print(member[0], ":", member[1])

start = time.time()
get_clan()
print(round(time.time() - start, 2), "seconds")