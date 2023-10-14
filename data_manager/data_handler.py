"""
    This file is responsible for handling data operations.

    Functions:
        in_dict_list(key, value, list): find if player is already in manual data
        update_members(clan_members, manual_data): update list of members in manual player data file
"""


# Imports
import data_manager.file_handler as file_handler


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

    for member in clan_members:
        search = in_dict_list('tag', member['tag'], manual_data)
        if search is None:
            new_data.append({"name": member['name'],"tag": member['tag'], "warAttacks": [0,0,0], "leagueAttacks": 0, "raidAttacks": 0, "clanGames": 0, "chat": 0})
        else:
            new_data.append(search)
    file_handler.update_file(new_data)