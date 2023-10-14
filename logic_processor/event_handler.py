"""
    This file is responsible for handling the main loop and interaction of the program.

    Functions:
        setup(config_clan_tag): set up the program
        event_handler(clan_data, manual_data, filters): main loop
"""


# Imports
import time

import config # config.py file
import data_manager.file_handler as file_handler
import logic_processor.evaluator as evaluator
import logic_processor.api_caller as api_caller
import logic_processor.progress_tracker as progress_tracker


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
    print("\n\nStarting Clashmate")

    # Get clan data
    print("\nRetrieving clan data")
    progress_tracker.progress_bar(1, 100, bar_length=20)
    clan_data = api_caller.request_data(config_clan_tag, "clans")
    
    # Check for access error
    if "reason" in clan_data:
        print(f"\n\nAPI ERROR: {clan_data['reason']}. Message: {clan_data['message']}")
        print("Suggestion: check that your auth key is correct. You may need to generate a new one from the Clash of Clans developer page as key's are IP locked.")
        return False, None
        progress_tracker.progress_bar(100, 100, bar_length=20)
    
    # Get manual player data
    print("\nRetrieving manual data")
    progress_tracker.progress_bar(1, 100, bar_length=20)
    manual_data = file_handler.get_file()
    progress_tracker.progress_bar(100, 100, bar_length=20)
    
    # Update clan members in manual data
    print("\nUpdating manual data")
    file_handler.update_members(clan_data["memberList"], manual_data)

    # Get updated manual player data
    print("\nRetrieving updated manual data")
    progress_tracker.progress_bar(1, 100, bar_length=20)
    manual_data = file_handler.get_file()
    progress_tracker.progress_bar(100, 100, bar_length=20)
    return clan_data, manual_data


# Main loop
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
    run = True

    # User input to choose action
    while run:
        print()
        input_num = input("Enter a command number: \n - 1: Evaluate clan\n - 2: Quit\n\nInput: ")
        if input_num == "1":
            # Evaluate clan
            start = time.time()
            evaluator.evaluate(clan_data, manual_data, filters)
            print("\n(runtime:", round(time.time() - start, 2), "second)")
            run = False
        elif input_num == "2":
            # Quit
            print("\nQuitting")
            run = False
        else:
            # Error
            print("\nWARNING: Enter a valid command number")
    print("Program ended")