import requests
import time
import json
import config # config.py file with auth_key

headers = {
    'Accept': 'application/json',
    'authorization': config.auth_key
}

def get_user(player_tag, manual_data):
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
    # get manual data
    warAttacks, leagueAttacks, raidAttacks, clanGames, chat = retrieve_data(player_tag, manual_data)
    # calculate rating
    rating = round(hall  + (trophies/300) + (donations/100) + (clan_capital/50000) + (leagueAttacks*1.5) + (warAttacks*5) + raidAttacks + (clanGames/500) + chat)

    print(user_json['name'], "hall:", hall, "trophies:", (trophies/300), "donations:", (donations/100), "capital gold:", (clan_capital/50000), 
    "league:", (leagueAttacks*1.5), "war attacks:", (warAttacks*5), "raid attacks:", raidAttacks, "clan games:", (clanGames/500), "chat", chat) 
    # return player name and rating
    return user_json['name'], rating

def sortFunc(e):
    return e[1]

# progress bar from https://stackoverflow.com/a/37630397
def progress_bar(current, total, bar_length=20):
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '
    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)

def get_file():
    # get file data
    f = open("player_data.txt", "r")
    data = f.read()
    f.close()
    json_data = json.loads(data)
    return json_data

def retrieve_data(player_tag, manual_data):
    data = []
    for player in manual_data:
        if player_tag == player["tag"]:
            return player["warAttacks"], player["leagueAttacks"], player["raidAttacks"], player["clanGames"], player["chat"]
        else:
                return 0, 0, 0, 0, 0

def main():
    # get clan data
    response = requests.get('https://api.clashofclans.com/v1/clans/%2329R2GLL89', headers = headers)
    clan = response.json() 

    # get manual player data
    print("Getting manual data")
    manual_data = get_file()
    
    members = []
    print('----- Evaluating clan: "' + clan['name'] + '" with ' + str(len(clan['memberList'])) + ' members -----')
    x = 0

    # get rating for each player
    for member in clan['memberList']:
        x += 1
        progress_bar(x, len(clan['memberList']))
        members.append(get_user(member['tag'], manual_data))

    # sort players by rating
    members.sort(key=sortFunc) # order by rating value
    members.reverse() # highest rating first

    # output results
    print()
    print('----- Sorted by rating -----')
    for member in members:
        print(member[0], ":", member[1])

# start code
if __name__ == '__main__':
    start = time.time()
    main()
    print(round(time.time() - start, 2), "seconds")