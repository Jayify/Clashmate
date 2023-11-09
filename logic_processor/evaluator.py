"""
    This file contains the logic for evaluating a clan's members and outputting the results.

    Functions:
        retrieve_data(player_tag, manual_data): retrieve values from json data for individual player
        calculate_user(player_tag, manual_data, filters): get individual player data and calculate rating
        sortFunc(e): sort players by rating
        evaluate(clan, manual_data, filters): iterate through clan members, calculate rating and sort by rating
"""


# Imports
import logic_processor.api_caller as api_caller
import logic_processor.progress_tracker as progress_tracker


# Procedures
def retrieve_data(player_tag, manual_data):
    """
        This function retrieves values from json data for individual player.
        
        Parameters:
            player_tag (str): the player's tag
            manual_data (dict): the manual data from the file
            
        Returns:
            warAttacks (list): the player's war attacks
            leagueAttacks (int): the player's league attacks
            raidAttacks (int): the player's raid attacks
            clanGames (int): the player's clan games
            chat (int): the player's chat
    """
    for player in manual_data:
        if player_tag == player["tag"]:
            return player["war"], player["cwl"], player["raid"], player["clanGames"]
    return [], 0, 0, 0.1


def calculate_user(player_tag, manual_data, filters):
    """
        This function gets individual player data and calculates rating.

        Parameters:
            player_tag (str): the player's tag
            manual_data (dict): the manual data from the file
            filters (dict): the filters from the config file

        Returns:
            user_json['name'] (str): the player's name
            rating (int): the player's rating
    """
    user_data = api_caller.request_data(player_tag, "players")
    
    # Pull out useful stats
    hall = user_data['townHallLevel']
    trophies = user_data['trophies']
    donations = user_data['donations']
    clan_capital = user_data['clanCapitalContributions']

    # Penalty if unranked
    leaguePenalty = 0
    if 'league' not in user_data:
            leaguePenalty = -20

    # Set low default value for 0 values to avoid divide by 0 error
    if donations == 0:
        donations = 0.1
    if clan_capital == 0:
        clan_capital = 0.1

    # Get manual data
    war_list, cwl_dict, raid_list, clanGames = retrieve_data(player_tag, manual_data)

    # Handle lists and dicts
    war = (sum(war_list)/len(war_list))+len(war_list) # Average war attacks plus bonus for being in more wars
    cwl = (cwl_dict['stars']/cwl_dict['maxAttacks']) + (cwl_dict['attacks']/cwl_dict['maxAttacks']) # Stars plus attack ratio
    raid = (sum(raid_list)/len(raid_list)) + (len(raid_list)*1000) # Average raid attacks plus bonus for being in more raids

    # Calculate rating
    rating = round(hall + (trophies/300) + (donations/100) - (leaguePenalty) + (clan_capital/20000) + (cwl) + (war*1.5) + raid + (clanGames/400))

    # print(user_data['name'], "hall:", hall, "trophies:", (trophies/300), "donations:", (donations/100), "league:", (league/2), 
    #      "capital gold:", (clan_capital/50000), "cwl:", (cwl*1.5), "war attacks:", (warAttacks*5), "raid attacks:", raid, "clan games:", (clanGames/500))

    # return player name and rating
    return user_data['name'], rating


def sortFunc(info):
    """
        This function is responsible for sorting players by rating.

        Parameters:
            info (tuple): the player's name and rating

        Returns:
            info[1] (int): the player's rating
    """
    return info[1]


def evaluate(clan, manual_data, filters):    
    """	
        This function iterates through clan members, calculates rating and sorts by rating.

        Parameters:
            clan (dict): the clan data
            manual_data (dict): the manual data from the file
            filters (dict): the filters from the config file
    """
    members = []
    x = 0
    print()

    # Get rating for each player
    for member in clan['memberList']:
        x += 1
        progress_tracker.progress_bar(x, len(clan['memberList']), "Evaluating", f"Evaluating clan '{clan['name']}' with {str(len(clan['memberList']))} members", 20)
        result = calculate_user(member['tag'], manual_data, filters)
        if result == None:
            continue
        else:
            members.append(result)

    # Sort players by rating
    members.sort(key=sortFunc) # Order by rating value
    members.reverse() # Highest rating first

    # Output results
    print()
    print('----- Members by Highest Evaluation Score -----')
    print('- Filters: limit', filters['displayNumber'], 'players, display unranked players:', filters['displayUnranked'], '-')
    x = 1
    for member in members:
            print(member[0], ":", member[1])
            x += 1
            if x > filters['displayNumber']:
                break