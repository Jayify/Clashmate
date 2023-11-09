"""
    This file is responsible for handling the main loop and interaction of the program.

    Functions:
        setup(config_clan_tag): set up the program
        event_handler(clan_data, manual_data, filters): main loop
"""


# Imports
import time

import data_manager.file_handler as file_handler
import logic_processor.evaluator as evaluator
import logic_processor.api_caller as api_caller
import logic_processor.progress_tracker as progress_tracker
import data_manager.data_handler as data_handler
import logic_processor.update_manager as update_manager


# Procedures
def setup(config_clan_tag):
    """	
        This function is responsible for setting up the program.

        Parameters:
            config_clan_tag (str): the clan tag from the config file

        Returns:
            clan_data (dict): the clan data, or False if there is an error
            manual_data (dict): the manual data from the file
    """
    print("\n\nStarting Clashmate\n")

    # Get clan data
    progress_tracker.progress_bar(1, 100, "Setup", "Retrieving clan data", 20)
    clan_data = api_caller.request_data(config_clan_tag, "clans")
    
    # Check for access error
    progress_tracker.progress_bar(20, 100, "Setup", "Validating API key", 20)
    if "reason" in clan_data:
        print(f"\n\nAPI ERROR: {clan_data['reason']}. Message: {clan_data['message']}")
        print("Suggestion: check that your auth key is correct. You may need to generate a new one from the Clash of Clans developer page as key's are IP locked.")
        return False, None
    
    # Get manual player data
    progress_tracker.progress_bar(40, 100, "Setup", "Retrieving manual data", 20)
    manual_data = file_handler.read_file()

    # Update clan members in manual data
    progress_tracker.progress_bar(60, 100, "Setup", "Refreshing manual data", 20)
    data_handler.update_members(clan_data["memberList"], manual_data)

    # Get updated manual player data
    progress_tracker.progress_bar(80, 100, "Setup", "Retrieving updated manual data", 20)
    manual_data = file_handler.read_file()
    progress_tracker.progress_bar(100, 100, "Setup", "Complete", 20)

    print("\nWelcome to Clashmate!")
    return clan_data, manual_data


def update_handler(manual_data):
    """
        This function is responsible for handling the update loop. It is called when the user wants to add manual data.

        Returns:
            manual_data (dict): the updated manual data from the file
    """
    loop = True

    # User input to choose action
    while loop:
        input_num = input("\nEnter a command number:\n - 1: Add war\n - 2: Add CWL\n - 3: Add clan games\n - 4: Add raid weekend\n - 5: Return\n\nInput: ")
        if input_num == "1":
            # Add war
            return update_manager.add_war(manual_data)
        elif input_num == "2":
            # Add CWL
            return update_manager.add_cwl(manual_data)
        elif input_num == "3":
            # Add clan games
            return update_manager.add_clan_games(manual_data)
        elif input_num == "4":
            # Add raid weekend
            return update_manager.add_raid(manual_data)
        elif input_num == "5":
            # Return
            loop = False
            print("\nReturning to main menu")
        else:
            # Error
            print("\nWARNING: Enter a valid command number")


def event_handler(clan_data, manual_data, filters):
    """
        This function is responsible for running the main loop.

        Parameters:
            clan_data (dict): the clan data
            manual_data (dict): the manual data from the file
            filters (dict): the filters from the config file

        Returns:
            clan_data (dict): the clan data
            manual_data (dict): the manual data from the file
    """
    loop = True
    stored_data = manual_data

    # User input to choose action
    while loop:
        input_num = input("\nEnter a command number:\n - 1: Evaluate clan\n - 2: Add manual data\n - 3: Config\n - 4: Quit\n\nInput: ")
        if input_num == "1":
            # Evaluate clan
            start = time.time()
            evaluator.evaluate(clan_data, stored_data, filters)
            print("\n(runtime:", round(time.time() - start, 2), "second)")
        elif input_num == "2":
            # Add manual data
            stored_data = update_handler(manual_data)
        elif input_num == "3":
            # Edit configuration
            print("\nTo be added")
        elif input_num == "4":
            # Quit
            print("\nQuitting")
            loop = False
            file_handler.update_file(manual_data)
        else:
            # Error
            print("\nWARNING: Enter a valid command number")
    print("Program ended")