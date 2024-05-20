"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
    
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    elif card == '2':
        return 2
    elif card == '3':
        return 3
    elif card == '4':
        return 4
    elif card == '5':
        return 5
    elif card == '6':
        return 6
    elif card == '7':
        return 7
    elif card == '8':
        return 8
    elif card == '9':
        return 9
    elif card == '10':
        return 10
    else:
        return None
    
    
def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
       
    
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_two) > value_of_card(card_one):
        return card_two
    else:
        return card_one, card_two
    # Consider whether you need to add an else statement if someone typed in something they weren't supposed to. (Applies above too.)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
                 
    if value_of_card(card_one) + value_of_card(card_two) >= 11:
        return 1
    elif value_of_card(card_one) + value_of_card(card_two) <= 10:
        return 11
    elif card_two == 'A' or card_one == 'A':
        return 1
    #in this one, I don't think i've done anything about drawing an Ace
    
   
def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    
    if value_of_card(card_one) + value_of_card(card_two) == 21:
        return True
    else:
        return False
    
    #if value_of_card(card_one) == 'A' and value_of_card(card_two) == 10:
    #    return True
    #elif value_of_card(card_two) == 'A' and value_of_card(card_one) == 10:
    #    return True
    #else:
    #    return False



def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    #value_of_card()
    if card_one == card_two:
        return True
    else:
        return False
    
    #This is not correct - need to find a way to make J == Q e.g.
    



def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    #value_of_card()
    
    if card_one + card_two == '9' or '10' or '11':
        return True
    else:
        return False
    
