"""
    This is the main file for the Clashmate project. It is responsible for starting the program.

    Functions:
        main(config_clan_tag, filters): main program
"""


# Import modules
import config
import logic_processor.event_handler as event_handler


# Main program
def main(config_clan_tag, filters):
    """
        This is the main function for the Clashmate project. It is responsible for running the program.
        
        Parameters:
            config_clan_tag (str): the clan tag from the config file
            filters (dict): the filters from the config file
    """
    # Set up
    clan_data, manual_data = event_handler.setup(config_clan_tag)

    # Main loop
    event_handler.event_handler(clan_data, manual_data, filters)


if __name__ == '__main__':
    main(config.clan_tag, config.filters)