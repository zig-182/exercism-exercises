"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    number = [number, number +1, number + 2]
    return number


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    all_in_one = rounds_1 + rounds_2
    return all_in_one
    


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    length = len(hand)
    total = sum(hand)
    answer = total / length
    return answer


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    #not sure if i call the function above (as i don't need the return part)
    length = len(hand)
    total = sum(hand)
    answer = total / length
    
    middle_index = length // 2
    middle_card = hand[middle_index]
    
    new = hand[0] + hand[-1]
    if new / 2 == answer:
        return True
    elif middle_card == answer:
        return True
    else:
        return False
    


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd = hand[0::2]
    even = hand[1::2]
    
    odd_answer = sum(odd) / len(odd)
    even_answer = sum(even) / len(even)
    if even_answer == odd_answer:
        return True
    else:
        return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand and hand[-1] == 11:
        hand[-1] = hand[-1] * 2
    return hand
 