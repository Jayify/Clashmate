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
        This function updates the list of members in the manual player data file to match with the API data.

        Parameters:
            clan_members (list): list of clan members from the api
            manual_data (list): manual data
    """
    # Add new members to manual data
    for member in clan_members:
        search = in_dict_list('tag', member['tag'], manual_data)
        if search is None:
            manual_data.insert(clan_members.index(member), {"name": member['name'],"tag": member['tag'], "war": [], "cwl": {"stars": 0, "attacks": 0, "maxAttacks": 0}, "raid": [], "clanGames": 0})
    # Remove members that left the clan from manual data
    for member in manual_data:
        search = in_dict_list('tag', member['tag'], clan_members)
        if search is None:
            manual_data.remove(member)
    file_handler.update_file(manual_data)
