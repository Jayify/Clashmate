"""
    This module is responsible for making api calls to the clash of clans api.

    Functions:
        request_data(tag, type): request clan data from the api
"""


# Imports
import requests
import config


# Declare globals
headers = {
    'Accept': 'application/json',
    'authorization': config.auth_key
}


# Procedures
def request_data(tag, type):
    """
        This function is responsible for requesting clan data from the api.

        Parameters:
            tag (str): the clan or player tag to request data for
            type (str): the type of data to request ('clans' or 'players' )

        Returns:
            data (dict): the data from the api call
    """
    tag = tag.replace('#', '%23') # Replace # with %23 for api call
    response = requests.get(f'https://api.clashofclans.com/v1/{type}/'+tag, headers = headers)
    data = response.json() 
    return data
