import requests
import time
import json
import config # config.py file

# api request headers
headers = {
    'Accept': 'application/json',
    'authorization': config.auth_key
}


# retrieve bulk data from file and convert to json
def get_file():
    # get file data
    f = open("player_data.txt", "r")
    data = f.read()
    f.close()
    if data == "":
        data = "[]" # if file is empty, set to empty list
    json_data = json.loads(data)
    return json_data

# retrieve values from json data for individual player
def retrieve_data(player_tag, manual_data):
    data = []
    for player in manual_data:
        if player_tag == player["tag"]:
            return player["warAttacks"], player["leagueAttacks"], player["raidAttacks"], player["clanGames"], player["chat"]
        else:
                return 0, 0, 0, 0, 0

# find if player is already in manual data
def in_dict_list(key, value, list):
    for entry in list:
        if entry[key] == value:
            return entry
    return None

# sort players by rating
def sortFunc(e):
    return e[1]

# progress bar from https://stackoverflow.com/a/37630397
def progress_bar(current, total, bar_length=20):
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '
    ending = '\n' if current == total else '\r'
    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)

# get individual player data and calculate rating
def calculate_user(player_tag, manual_data):
    player = player_tag.replace('#', '%23')# convert tag to correct format
    response = requests.get('https://api.clashofclans.com/v1/players/'+player, headers = headers)
    user_json = response.json() # convert object to json
    
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

    #set low default value for 0 values to avoid divide by 0 error
    if donations == 0:
        donations = 0.1
    if war_stars == 0:
        war_stars = 0.1
    if clan_capital == 0:
        clan_capital = 0.1
    if league == 0:
        league = 0.1

    # get manual data
    if manual_data == []:
        warAttacks, leagueAttacks, raidAttacks, clanGames, chat = 0, 0, 0, 0.1, 0 # set clan games to 1 to avoid divide by 0 error
    else:
        warAttacks, leagueAttacks, raidAttacks, clanGames, chat = retrieve_data(player_tag, manual_data)

    # calculate rating
    rating = round(hall  + (trophies/300) + (donations/100) + (clan_capital/50000) + (leagueAttacks*1.5) + (warAttacks*5) + raidAttacks + (clanGames/500) + chat)

    # print(user_json['name'], "hall:", hall, "trophies:", (trophies/300), "donations:", (donations/100), "capital gold:", (clan_capital/50000), 
    # "league:", (leagueAttacks*1.5), "war attacks:", (warAttacks*5), "raid attacks:", raidAttacks, "clan games:", (clanGames/500), "chat", chat)
    
    # return player name and rating
    return user_json['name'], rating

# update list of members in manual player data file
def update_members(clan_members, manual_data):   
    new_data = []
    x = 0

    for member in clan_members:
        x += 1
        progress_bar(x, len(clan_members))
        search = in_dict_list('tag', member['tag'], manual_data)
        if search is None:
            new_data.append({"name": member['name'],"tag": member['tag'], "warAttacks": 0, "leagueAttacks": 0, "raidAttacks": 0, "clanGames": 0, "chat": 0})
        else:
            new_data.append(search)
    f = open("player_data.txt", "w")
    f.write(json.dumps(new_data, indent=2))
    f.close()
    print("\nClan members have been updated. You may now edit the player_data.txt file to add or update manual data.")

# iterate through clan members, calculate rating and sort by rating
def evaluate(clan, manual_data):    
    print('\n----- Evaluating clan: "' + clan['name'] + '" with ' + str(len(clan['memberList'])) + ' members -----')
    members = []
    x = 0

    # get rating for each player
    for member in clan['memberList']:
        x += 1
        progress_bar(x, len(clan['memberList']))
        members.append(calculate_user(member['tag'], manual_data))

    # sort players by rating
    print("\nSorting by rating")
    members.sort(key=sortFunc) # order by rating value
    members.reverse() # highest rating first

    # output results
    print()
    print('----- Sorted by rating -----')
    for member in members:
        print(member[0], ":", member[1])


# main program
def main(old_clan_tag):
    run = True
    print("Starting CoC Clanmate Evaluator program")

    # get clan data
    print("\nRetrieving clan data")
    progress_bar(1, 100, bar_length=20)
    clan_tag = old_clan_tag.replace('#', '%23') # replace # with %23 for api call
    response = requests.get('https://api.clashofclans.com/v1/clans/'+clan_tag, headers = headers)
    clan_data = response.json() 
    progress_bar(100, 100, bar_length=20)

    # get manual player data
    print("\nRetrieving manual data")
    progress_bar(1, 100, bar_length=20)
    manual_data = get_file()
    progress_bar(100, 100, bar_length=20)

    # user input to choose action
    while run:
        print()
        input_num = input("Enter a command number: \n - 1: Evaluate clan\n - 2: Update manual data\n - 3: Quit:\n")
        if input_num == "1":
            # evaluate clan
            start = time.time()
            evaluate(clan_data, manual_data)
            print("\n(runtime:", round(time.time() - start, 2), "second)")
            run = False
        elif input_num == "2":
            # update manual data
            print("\nUpdating manual data\n")
            update_members(clan_data["memberList"], manual_data)
        elif input_num == "3":
            # quit
            print("\nQuitting")
            run = False
        else:
            # error
            print("\nWARNING: Enter a valid command number")
    print("Program ended")

# start code
if __name__ == '__main__':
    main(config.clan_tag)