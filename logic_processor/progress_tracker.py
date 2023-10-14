"""
    This module is responsible for displaying and updating progress bars.

    Functions:
        progress_bar(current, total, bar_length): display a progress bar
"""


# Procedures
def progress_bar(current, total, activity_message, task_message, bar_length):
    """
        This function is responsible for displaying a progress bar.

        Parameters:
            current (int): the current progress
            total (int): the total progress
            activity_message (str): the message to display before the progress bar
            task_message (str): the message to display after the progress bar
            bar_length (int): the length of the progress bar
    """
    # Progress bar from https://stackoverflow.com/a/37630397
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '
    ending = '\n' if current == total else '\r'
    print(f'{activity_message}: [{arrow}{padding}] {int(fraction*100)}% {task_message} {" "*24}', end=ending)
    # " "*X is necessary to include then replacing the old message
    # as if the new line is shorter than the previous line, the end of the previous line will still be displayed