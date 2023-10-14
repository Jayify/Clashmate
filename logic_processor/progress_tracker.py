"""
    This module is responsible for displaying and updating progress bars.

    Functions:
        progress_bar(current, total, bar_length): display a progress bar
"""


# Procedures
def progress_bar(current, total, bar_length=20):
    """
        This function is responsible for displaying a progress bar.

        Parameters:
            current (int): the current progress
            total (int): the total progress
            bar_length (int): the length of the progress bar
    """
    # Progress bar from https://stackoverflow.com/a/37630397
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '
    ending = '\n' if current == total else '\r'
    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)