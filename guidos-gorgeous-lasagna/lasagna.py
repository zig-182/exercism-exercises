"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.

EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.

def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    remaining_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_time





#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.

#number_of_layers = 4
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Function that adds together the time already spent preparing, as well as how long the lasagne has currently been cooking
    """
    total_preparation_time = number_of_layers * 2
    return total_preparation_time

    
#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.

    Function that works out the total time spent making the lasagne, which includes the prep time and time spent cooking so far
    """    
    total_elapsed_time = elapsed_bake_time + (number_of_layers * 2)
    return total_elapsed_time