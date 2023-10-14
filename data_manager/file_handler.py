"""
    This module is responsible for handling file operations and data retrieval.

    Functions:
        read_file(): read data from file
        update_file(json_data): update file with new data
"""


# Imports
import json


# Declare globals
file_path = "./database/player_data.txt"


# Procedures
def read_file():
    """
        This function is responsible for retrieving bulk data from file and converting to json.

        Returns:
            json_data (dict): the data from the file in json format
    """
    global file_path
    with open(file_path, "r") as f:
        data = f.read()
    if data == "":
        data = "[]" # If file is empty, set to empty list
    json_data = json.loads(data)
    return json_data


def update_file(json_data):
    """
        This function is responsible for updating the file with new data.

        Parameters:
            json_data (dict): the data to write to the file
    """
    global file_path
    with open(file_path, "w") as f:
        f.write(json.dumps(json_data, indent=2))