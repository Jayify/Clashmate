"""
    This module is responsible for handling file operations and data retrieval.

    Functions:
        get_file(): retrieve bulk data from file and convert to json
        in_dict_list(key, value, list): find if player is already in manual data
        update_members(clan_members, manual_data): update list of members in manual player data file
"""


# Imports
import json

import logic_processor.progress_tracker as progress_tracker


# Declare globals
file_path = "./database/player_data.txt"


# Procedures
def get_file():
    """
        This function is responsible for retrieving bulk data from file and converting to json.

        Returns:
            json_data (dict): the data from the file in json format
    """

    global file_path
    # Get file data
    with open(file_path, "r") as f:
        data = f.read()
    
    if data == "":
        data = "[]" # If file is empty, set to empty list
    json_data = json.loads(data)
    return json_data


def in_dict_list(key, value, list):
    """
        This function finds if a player is already in the manual data.

        Parameters:
            key (str): data in the manual data to match against
            value (str): clan member player tag
            list (list): manual data

        Returns:
            entry (dict): the entry in the manual data if found, otherwise None
    """
    for entry in list:
        if entry[key] == value:
            return entry
    return None


def update_members(clan_members, manual_data):   
    """
        This function updates the list of members in the manual player data file.

        Parameters:
            clan_members (list): list of clan members from the api
            manual_data (list): manual data
    """
    new_data = []
    x = 0

    for member in clan_members:
        x += 1
        progress_tracker.progress_bar(x, len(clan_members))
        search = in_dict_list('tag', member['tag'], manual_data)
        if search is None:
            new_data.append({"name": member['name'],"tag": member['tag'], "warAttacks": [0,0,0], "leagueAttacks": 0, "raidAttacks": 0, "clanGames": 0, "chat": 0})
        else:
            new_data.append(search)
    f = open("player_data.txt", "w")
    f.write(json.dumps(new_data, indent=2))
    f.close()