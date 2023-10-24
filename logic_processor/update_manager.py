"""
    This module contains functions that update the data in the database.
"""


# Procedures
def add_war(manual_data):
    """
        This function updates the war data in the manual player data file.

        Parameters:
            manual_data (list): manual data
    """
    print('----- Adding Clan War Stats -----')
    print("For each player, enter the number of stars earned (leave the input empty if they didn't participate), then number of attacks used.")
    for player in manual_data:
        loop = True
        print(f'{player["name"]}:')
        while loop:
            response_1 = input(f'  stars earned: ')
            if response_1.lower() == '' or response_1[0].lower() == 'n':
                break
            elif response_1.isdigit() and int(response_1) >= 0 and int(response_1) <= 6:
                while loop:
                    response_2 = input(f'  attacks used: ')
                    if response_2.isdigit() and int(response_2) >= 0 and int(response_2) <= 2:
                        player['war'].insert(0, {'starsGained': int(response_1), 'attacksUsed': int(response_2)})
                        if len(player['war']) > 5:
                            player['war'].pop()
                        loop = False
    print('\nAdding War Stats Complete\n')


def add_cwl(manual_data):
    """
        This function updates the CWL data in the manual player data file.

        Parameters:
            manual_data (list): manual data
    """
    print('----- Adding Clan War League Stats -----')
    print("For each player, enter the number of stars earned (leave the input empty if they didn't participate), the number of attacks used. then the number of attacks they had available.")
    for player in manual_data:
        loop = True
        print(f'{player["name"]}:')
        while loop:
            response_1 = input(f'  stars earned: ')
            if response_1.lower() == '' or response_1[0].lower() == 'n':
                break
            elif response_1.isdigit() and int(response_1) >= 0 and int(response_1) <= 14:
                while loop:
                    response_2 = input(f'  attacks used: ')
                    if response_2.isdigit() and int(response_2) >= 0 and int(response_2) <= 7:
                        while loop:
                            response_3 = input(f'  attacks available: ')
                            if response_3.isdigit() and int(response_3) >= 0 and int(response_3) <= 7:
                                player['cwl'] = {'starsGained': int(response_1), 'attacksUsed': int(response_2), 'attacksAvailable': int(response_3)}
                                loop = False
    print('\nAdding CWL Stats Complete\n')


def add_clan_games(manual_data):
    """
        This function updates the clan games data in the manual player data file.

        Parameters:
            manual_data (list): manual data
    """
    print('----- Adding Clan Games Stats -----')
    print("For each player, enter the number of points earned (leave empty if they didn't participate).")
    for player in manual_data:
        loop = True
        while loop:
            response = input(f'{player["name"]} points: ')
            if response.isdigit() and int(response) >= 0 and int(response) <= 5000:
                player['clanGames'] = int(response)
                loop = False
            if response.lower() == '' or response[0].lower() == 'n':
                player['clanGames'] = 0
                loop = False
    print('\nAdding Clan Games Stats Complete\n')


def add_raid(manual_data):
    """
        This function updates the raid weekend data in the manual player data file.

        Parameters:
            manual_data (list): manual data
    """
    print('----- Adding Raid Weekend Stats -----')
    print("For each player, enter the number of stars earned (leave blank if they didn't participate), then number of attacks used, then the number of attacks they had available.")
    for player in manual_data:
        loop = True
        while loop:
            response = input(f'{player["name"]} capital gold: ')
            if response.isdigit() and int(response) >= 0 and int(response) <= 30000:
                player['raid'].insert(0, {'capitalGold': int(response)})
                loop = False
            elif response.lower() == '' or response[0].lower() == 'n':
                player['raid'].insert(0, {'capitalGold': 0})
                loop = False
            if len(player['raid']) > 4:
                    player['raid'].pop()
    print('\nAdding Raid Weekend Stats Complete\n')
    