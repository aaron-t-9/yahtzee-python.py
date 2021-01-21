"""
Yahtzee
Final Exam

Aaron T.
"""

import random


def YAHTZEE() -> int:
    """
    Constant value, returns the integer 50 representing a large straight.

    :param: N/A, no parameters accepted.
    :return: An integer.
    """
    return 50


def LARGE_STRAIGHT() -> int:
    """
    Constant value, returns the integer 40 representing a large straight.

    :param: N/A, no parameters accepted.
    :return: An integer.
    :return:
    """
    return 40


def SMALL_STRAIGHT() -> int:
    """
    Constant value, returns the integer 30 representing a small straight.

    :param: N/A, no parameters accepted.
    :return: An integer.
    :return:
    """
    return 30


def FULL_HOUSE() -> int:
    """
    Constant value, returns the integer 25 representing a full house.

    :param: N/A, no parameters accepted.
    :return: An integer.
    :return:
    """
    return 25


def NO_SCORE() -> int:
    """
    Constant value, returns the integer 0 representing an invalid selection of category by
    the player.

    :param: N/A, no parameters accepted.
    :return: An integer.
    """
    return 0


def NUMBERED_CATEGORIES():
    """
    Constant value, returns nothing, prints out the categories that the player can select from.

    :param: N/A, no parameters accepted.
    :return: Nothing is returned, prints multiple strings.
    """
    print("\n#1 ---> Aces")
    print("#2 ---> Twos")
    print("#3 --->  Threes")
    print("#4 ---> Fours")
    print("#5  ---> Fives")
    print("#6 ---> Sixes")
    print("#7 ---> 3 Of a Kind")
    print("#8 ---> 4 Of a Kind")
    print("#9 ---> Full House")
    print("#10 ---> Small Straight")
    print("#11 ---> Large Straight")
    print("#12 ---> Yahtzee")
    print("#13 ---> Chance")


def generate_score_sheet(player_number) -> dict:
    """
    Returns a dictionary containing the score sheet for Yahtzee.

    Creates the score board represented as a dictionary and returns this dictionary.

    :param: No parameters accepted.
    :precondition: N/A, no paramters accepted.
    :postcondition: Returns a dictionary representing the score sheet for Yahtzee.
    :return: A dictionary.

    >>> test_player_number = "Player 1"
    >>> generate_score_sheet(test_player_number)
    {'player': 'Player 1', 'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, \
'Fives': -1, 'Sixes': -1, '3 of a kind': -1, '4 of a kind': -1, \
'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1, \
'Chance': -1, 'Yahtzee Bonus': [], 'Total of Upper': '0', \
'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}

    >>> test_player_number = "Player 2"
    >>> generate_score_sheet(test_player_number)
    {'player': 'Player 2', 'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, \
'Fives': -1, 'Sixes': -1, '3 of a kind': -1, '4 of a kind': -1, \
'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1, \
'Chance': -1, 'Yahtzee Bonus': [], 'Total of Upper': '0', \
'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}
    """
    score_sheet = {'player': player_number, 'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1,
                   'Fives': -1, 'Sixes': -1, '3 of a kind': -1, '4 of a kind': -1,
                   'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1,
                   'Chance': -1, 'Yahtzee Bonus': [], 'Total of Upper': '0',
                   'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}

    return score_sheet


def score_sheet_printer(score_sheet: dict):
    """
    Returns nothing, prints out the player's score sheet.

    Accepts a dictionary representing the player's score sheet and prints the first 15 key value
    pairs representing the player's Yahtzee scores.

    :param score_sheet: A dictionary.
    :precondition score_sheet: A dictionary with the key, value, pairs representing the player's
                               Yahtzee score sheet.
    :postcondition: Nothing is returned. Multiple strings are printed out displaying the player's
                    Yahtzee score sheet.
    :return: Nothing is returned. Multiple strings are printed

    >>> player_score_sheet_empty = {'player': 'Player 1', 'Aces': -1, 'Twos': -1, \
'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, \
'3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, \
'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1, \
'Yahtzee Bonus': [], 'Total of Upper': '0', 'Total of Lower': '0', \
'Upper Bonus': '0', 'Grand Total': '0'}
    >>> score_sheet_printer(player_score_sheet_empty)
    <BLANKLINE>
    Player 1's Score sheet
    ------------------------------
    Aces:
    Twos:
    Threes:
    Fours:
    Fives:
    Sixes:
    =====
    3 of a kind:
    4 of a kind:
    Full House:
    Small Straight:
    Large Straight:
    Yahtzee:
    Chance:
    Yahtzee Bonus: []
    ------------------------------
    <BLANKLINE>

    >>> player_score_sheet_fifth_turn = {'player': 'Player 1', 'Aces': '4', 'Twos': -1, \
'Threes': -1, 'Fours': '8', 'Fives': '15', 'Sixes': -1, \
'3 of a kind': -1, '4 of a kind': -1, 'Full House': '25', \
'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1, \
'Yahtzee Bonus': [], 'Total of Upper': '0', 'Total of Lower': '0', \
'Upper Bonus': '0', 'Grand Total': '0'}
    >>> score_sheet_printer(player_score_sheet_fifth_turn)
    <BLANKLINE>
    Player 1's Score sheet
    ------------------------------
    Aces: 4
    Twos:
    Threes:
    Fours: 8
    Fives: 15
    Sixes:
    =====
    3 of a kind:
    4 of a kind:
    Full House: 25
    Small Straight:
    Large Straight:
    Yahtzee:
    Chance:
    Yahtzee Bonus: []
    ------------------------------
    <BLANKLINE>

    >>> player_score_sheet_Yahtzee_bonus = {'player': 'Player 1', 'Aces': '2', 'Twos': '8', \
'Threes': -1, 'Fours': -1, 'Fives': '10', 'Sixes': -1, \
'3 of a kind': -1, '4 of a kind': '25', 'Full House': '25', \
'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': '50', 'Chance': -1, \
'Yahtzee Bonus': ['Y'], 'Total of Upper': '0', 'Total of Lower': '0', \
'Upper Bonus': '0', 'Grand Total': '0'}
    >>> score_sheet_printer(player_score_sheet_Yahtzee_bonus)
    <BLANKLINE>
    Player 1's Score sheet
    ------------------------------
    Aces: 2
    Twos: 8
    Threes:
    Fours:
    Fives: 10
    Sixes:
    =====
    3 of a kind:
    4 of a kind: 25
    Full House: 25
    Small Straight:
    Large Straight:
    Yahtzee: 50
    Chance:
    Yahtzee Bonus: ['Y']
    ------------------------------
    <BLANKLINE>

    >>> player_score_sheet_second_Yahtzee_bonus = {'player': 'Player 1', 'Aces': '2', 'Twos': '8', \
'Threes': -1, 'Fours': -1, 'Fives': '10', 'Sixes': -1, \
'3 of a kind': -1, '4 of a kind': '25', 'Full House': '25', \
'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': '50', 'Chance': -1, \
'Yahtzee Bonus': ['Y', 'Y'], 'Total of Upper': '0', 'Total of Lower': '0', \
'Upper Bonus': '0', 'Grand Total': '0'}
    >>> score_sheet_printer(player_score_sheet_second_Yahtzee_bonus)
    <BLANKLINE>
    Player 1's Score sheet
    ------------------------------
    Aces: 2
    Twos: 8
    Threes:
    Fours:
    Fives: 10
    Sixes:
    =====
    3 of a kind:
    4 of a kind: 25
    Full House: 25
    Small Straight:
    Large Straight:
    Yahtzee: 50
    Chance:
    Yahtzee Bonus: ['Y', 'Y']
    ------------------------------
    <BLANKLINE>
    """
    print(f"\n{score_sheet['player']}'s Score sheet")
    print("------------------------------")

    for key in score_sheet.keys():

        if key == "player":
            pass

        elif score_sheet[key] == -1:
            print(f"{key}:")

            if key == "Sixes":
                print("=====")

        elif key == "Yahtzee Bonus":
            print(f"{key}: {score_sheet[key]}")

        elif key == "Total of Upper":
            break

        else:
            print(f"{key}: {score_sheet[key]}")

    print("------------------------------\n")


def dice_list_to_dict(dice_list: list) -> dict:
    """
    Returns a dictionary containing with the keys representing the side of the die, and the value
    representing the frequency of that specific die.

    Accepts a list of five random integers representing random 6-sided dice rolls, and returns
    a dictionary with the key representing the side of the die, and the value representing the
    frequency of that particular die.

    :param dice_list: A list.
    :precondition dice_list: A list of integers containing five integers ranging from 1-6
                             representing the player's dice rolls.
    :postcondition: Returns a dictionary with the key representing the side of the die, and the
                    value representing the frequency of that particular die.
    :return: A dictionary.

    # Doc-test
    """
    dice_dict = {}
    temp_dice_set = set()

    for dice in dice_list:
        temp_dice_set.add(dice)

    for dice in temp_dice_set:
        dice_dict[dice] = dice_list.count(dice)

    return dice_dict


def full_house_checker(dice_dict: dict) -> int:
    """
    Returns an integer representing the value of a full house if the hand of the player's dice
    is valid, or else it returns 0.

    :param dice_dict: A dictionary.
    :preconditon dice_dict: Returns a dictionary with the key representing the side of the die,
                            and the value representing the frequency of that particular die
    :postcondition: An integer is returned representing the value of a full house if the player's
                    hand of dice is valid, or else 0 is returned.
    :return: An integer.

    >>> dice_dict_3_OfAKind = {1: 3, 3: 1, 4: 1}
    >>> full_house_checker(dice_dict_3_OfAKind)
    0

    >>> dice_dict_sixes = {6: 3, 2: 1, 4: 1}
    >>> full_house_checker(dice_dict_sixes)
    0

    >>> dice_dict_yahtzee = {2: 5}
    >>> full_house_checker(dice_dict_yahtzee)
    25

    >>> dice_dict_full_house = {5: 3, 1: 2}
    >>> full_house_checker(dice_dict_yahtzee)
    25
    """
    if len(dice_dict) == 2 or len(dice_dict) == 1:
        return FULL_HOUSE()
    else:
        return NO_SCORE()


def three_and_four_of_a_kind_checker(dice_list: list, dice_dict: dict, user_selection: int) -> int:
    """
    Returns an integer representing the appropriate sum value for a 3 of a kind,
    or a 4 of a kind, if the player's hand of die is valid, or else 0 is returned.


    :param dice_list: A list.
    :param dice_dict: A dictionary.
    :param user_selection: An int.
    :precondition dice_list: A list of integers containing five integers ranging from 1-6
                             representing the player's dice rolls.
    :precondition dice_dict: Returns a dictionary with the key representing the side of the die,
                            and the value representing the frequency of that particular die.
    :precondition user_selection: An integer of the category that the player would like to fill
                                  in on their score sheet. The user selection must be
                                  between 1 and 6.
    :postcondition: Returns the appropriate integer sum value of the hand of dice of the player
                    for 3, and 4, of a kind if the player's hand of dice is valid.
                    Otherwise 0 is returned.
    :return: A integer.

    >>> dice_list_invalid = [1, 2, 3, 4, 4]
    >>> test_dict_dict = {1: 1, 2: 1, 3: 1, 4: 2}
    >>> user_selection_3_OfAKind = 7
    >>> three_and_four_of_a_kind_checker(dice_list_invalid, test_dict_dict, \
    user_selection_3_OfAKind)
    0

    >>> dice_list_invalid = [2, 3, 4, 5, 6]
    >>> test_dict_dict = {5: 1, 2: 1, 3: 1, 4: 1, 6: 1}
    >>> user_selection_3_OfAKind = 7
    >>> three_and_four_of_a_kind_checker(dice_list_invalid, test_dict_dict, \
    user_selection_3_OfAKind)
    0

    >>> dice_list_invalid = [5, 5, 4, 5, 6]
    >>> test_dict_dict = {5: 3, 4: 1, 6: 1}
    >>> user_selection_4_OfAKind = 8
    >>> three_and_four_of_a_kind_checker(dice_list_invalid, test_dict_dict, \
    user_selection_4_OfAKind)
    0

    >>> dice_list_valid = [2, 2, 2, 2, 2]
    >>> test_dict_dict = {2: 5}
    >>> user_selection_3_OfAKind = 7
    >>> three_and_four_of_a_kind_checker(dice_list_valid, test_dict_dict, \
    user_selection_3_OfAKind)
    10

    >>> dice_list_valid = [2, 2, 2, 2, 2]
    >>> test_dict_dict = {2: 5}
    >>> user_selection_3_OfAKind = 8
    >>> three_and_four_of_a_kind_checker(dice_list_valid, test_dict_dict, \
    user_selection_3_OfAKind)
    10

    >>> dice_list_valid = [6, 6, 5, 6, 6]
    >>> test_dict_dict = {6: 4, 5: 1}
    >>> user_selection_3_OfAKind = 8
    >>> three_and_four_of_a_kind_checker(dice_list_valid, test_dict_dict, \
    user_selection_3_OfAKind)
    29
    """

    if user_selection == 7:
        for value in dice_dict.values():
            if value >= 3:
                return sum(dice_list)
            else:
                return NO_SCORE()

    elif user_selection == 8:
        for value in dice_dict.values():
            if value >= 4:
                return sum(dice_list)
            else:
                return NO_SCORE()


def small_large_straight_checker(dice_dict: dict, user_selection: int) -> int:
    """
    Returns an integer representing the value of a small, or large, straight if the player's hand
    of dice is valid, otherwise 0 is returned.

    :param dice_dict: A dictionary.
    :param user_selection: An integer.
    :preconditon dice_dict: Returns a dictionary with the key representing the side of the die,
                            and the value representing the frequency of that particular die
                                and the value representing the frequency of that particular die.
    :precondition user_selection: An integer of the category that the player would like to fill
                                  in on their score sheet. The user selection must be
                                  between 1 and 6.
    :postcondition: An integer is returned representing the value of a full house if the player's
                    hand of dice is valid, otherwise 0 is returned.
    :return: An integer.

    >>> invalid_dice_dict = {1: 2, 2: 3}
    >>> user_selection_small_straight = 10
    >>> small_large_straight_checker(invalid_dice_dict, user_selection_small_straight)
    0

    >>> invalid_dice_dict = {1: 2, 4: 2, 6: 1}
    >>> user_selection_large_straight = 11
    >>> small_large_straight_checker(invalid_dice_dict, user_selection_large_straight)
    0

    >>> invalid_dice_dict = {5: 5}
    >>> user_selection_large_straight = 11
    >>> small_large_straight_checker(invalid_dice_dict, user_selection_large_straight)
    0

    >>> valid_dice_dict = {1: 1, 2: 1, 3: 1, 4: 2}
    >>> user_selection_small_straight = 10
    >>> small_large_straight_checker(valid_dice_dict, user_selection_small_straight)
    30

    >>> valid_dice_dict = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    >>> user_selection_large_straight = 11
    >>> small_large_straight_checker(valid_dice_dict, user_selection_large_straight)
    40
    """
    values_list = list(dice_dict.values())

    if user_selection == 10:
        if len(dice_dict) in [4, 5]:
            if 1 in values_list or 2 in values_list or 3 in values_list:
                return SMALL_STRAIGHT()

        else:
            return NO_SCORE()

    elif user_selection == 11:
        if len(dice_dict) == 5:
            if 1 in values_list or 2 in values_list:
                return LARGE_STRAIGHT()

        else:
            return NO_SCORE()


def yahtzee_checker(dice_dict: dict) -> int:
    """
    Returns an integer representing the value of a Yahtzee if the player's hand
    of dice is valid, otherwise 0 is returned.

    :param dice_dict: A dictionary.
    :preconditon dice_dict: Returns a dictionary with the key representing the side of the die,
                            and the value representing the frequency of that particular die
                                and the value representing the frequency of that particular die.
    :postcondition: An integer is returned representing the value of a Yahtzee if the player's
                    hand of dice is valid, otherwise 0 is returned.
    :return: An integer.

    >>> dice_dict_invalid = {1: 4, 6: 1}
    >>> yahtzee_checker(dice_dict_invalid)
    0

    >>> dice_dict_invalid = {1: 1, 6: 1, 4: 1, 3: 2}
    >>> yahtzee_checker(dice_dict_invalid)
    0

    >>> dice_dict_valid = {6: 5}
    >>> yahtzee_checker(dice_dict_valid)
    50

    >>> dice_dict_valid = {2: 5}
    >>> yahtzee_checker(dice_dict_valid)
    50
    """
    if len(dice_dict) == 1:
        return YAHTZEE()
    else:
        return NO_SCORE()


def yahtzee_bonus_checker(score_sheet: dict) -> dict or None:
    """
    Adds a string to a list within the key "Yahtzee Bonus" in the score_sheet dictionary if the
    player's hand of dice is valid and they already have a regular valid Yahtzee on
    their score sheet. Returns the dictionary with the updated value.

    :param score_sheet: A dictionary.
    :preconditon dice_dict: Returns a dictionary with the key representing the side of the die,
                            and the value representing the frequency of that particular die
                                and the value representing the frequency of that particular die.
    :postcondition: Adds a string to the Yahtzee Bonus category and returns a dictionary if
                    the player's hand of dice is valid and they have already scored a valid Yahtzee.
    :return: A dictionary.

    >>> test_score_sheet = {'player': 'Player 1', 'Aces': -1, 'Twos': -1, 'Threes': -1, \
    'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1, '4 of a kind': -1, \
'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1, \
'Chance': -1, 'Yahtzee Bonus': [], 'Total of Upper': '0', \
'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}
    >>> yahtzee_bonus_checker(test_score_sheet)


    >>> test_score_sheet_valid = {'player': 'Player 1', 'Aces': -1, 'Twos': -1, 'Threes': -1, \
    'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1, '4 of a kind': -1, \
'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': 50, \
'Chance': -1, 'Yahtzee Bonus': [], 'Total of Upper': '0', \
'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}
    >>> yahtzee_bonus_checker(test_score_sheet_valid)
    {'player': 'Player 1', 'Aces': -1, 'Twos': -1, 'Threes': -1, \
'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1, '4 of a kind': -1, \
'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': 50, \
'Chance': -1, 'Yahtzee Bonus': ['Y'], 'Total of Upper': '0', \
'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}

    >>> test_score_sheet_valid = {'player': 'Player 1', 'Aces': -1, 'Twos': -1, 'Threes': -1, \
    'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1, '4 of a kind': -1, \
'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': 50, \
'Chance': -1, 'Yahtzee Bonus': ["Y"], 'Total of Upper': '0', \
'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}
    >>> yahtzee_bonus_checker(test_score_sheet_valid)
    {'player': 'Player 1', 'Aces': -1, 'Twos': -1, 'Threes': -1, \
'Fours': -1, 'Fives': -1, 'Sixes': -1, '3 of a kind': -1, '4 of a kind': -1, \
'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': 50, \
'Chance': -1, 'Yahtzee Bonus': ['Y', 'Y'], 'Total of Upper': '0', \
'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}

    """
    if score_sheet["Yahtzee"] == 50:
        temp_list = score_sheet["Yahtzee Bonus"]
        temp_list.append("Y")

        score_sheet['Yahtzee Bonus'] = temp_list

        return score_sheet

    else:
        return


def get_category_value_lower(score_sheet: dict, dice_list: list, dice_dict: dict,
                             user_selection: int) -> int or list or dict:
    """
    An integer, or list, is returned representing the value to be filled into a category
    on the player's score sheet, depending on the validity of the player's hand of dice and the
    player's selection. A dictionary containing an updated score sheet is updated with the filled
    in Yahtzee bonus if the player has a valid hand and has previously scored a Yahtzee.

    :param score_sheet: A dictionary.
    :param dice_list: A list.
    :param dice_dict: A dictionary.
    :param user_selection: An integer.
    :precondition score_sheet: A dictionary with the key, value, pairs representing the player's
                               Yahtzee score sheet.
    :precondition dice_list: A list of integers containing five integers ranging from 1-6
                             representing the player's dice rolls.
    :precondition dice_dict: Returns a dictionary with the key representing the side of the die,
                            and the value representing the frequency of that particular die.
    :precondition user_selection: An integer of the category that the player would like to fill
                                  in on their score sheet. The user selection must be
                                  between 1 and 6.
    :postcondition: An integer is returned representing the value to be filled into
                    a category of the upper section of the player's Yahtzee score sheet.
    :postcondition: A list is returned containing a string of a character if the player
                    rolls their Yahtzee bonus.
    :return: An integer or list.
    """
    if user_selection == 7 or user_selection == 8:
        category_value = three_and_four_of_a_kind_checker(dice_list, dice_dict, user_selection)
        return category_value

    elif user_selection == 9:
        category_value = full_house_checker(dice_dict)
        return category_value

    elif user_selection == 10 or user_selection == 11:
        category_value = small_large_straight_checker(dice_dict, user_selection)
        return category_value

    elif user_selection == 12:
        category_value = yahtzee_checker(dice_dict)
        return category_value

    elif user_selection == 13:
        return sum(dice_list)

    else:
        updated_score_sheet = yahtzee_bonus_checker(score_sheet)
        return updated_score_sheet


def get_category_value_upper(dice_dict: dict, user_selection: int) -> int:
    """
    An integer is returned representing the value to be filled into a category on the player's
    score sheet.

    Returns an integer representing the value to be filled into the player
    specified category based on the player's list of dice rolls. Only calculates the category value
    for the upper section of the Yahtzee score sheet.

    :param dice_dict: A dictionary.
    :param user_selection: An integer.
    :precondition dice_dict: Returns a dictionary with the key representing the side of the die,
                            and the value representing the frequency of that particular die
    :precondition user_selection: An integer of the category that the player would like to fill
                                  in on their score sheet. The user selection must be
                                  between 1 and 6.
    :postcondition: An integer is returned representing the value to be filled into
                    a category of the upper section of the player's Yahtzee score sheet.
    :return: An integer.

    >>> test_dice_dict_invalid = {2: 3, 3: 2}
    >>> user_selection_aces = 1
    >>> get_category_value_upper(test_dice_dict_invalid, user_selection_aces)
    0

    >>> test_dice_dict_invalid = {1: 3, 2: 2}
    >>> user_selection_fives= 5
    >>> get_category_value_upper(test_dice_dict_invalid, user_selection_fives)
    0

    >>> test_dice_dict_valid = {6: 3, 2: 2}
    >>> user_selection_sixes = 6
    >>> get_category_value_upper(test_dice_dict_valid, user_selection_sixes)
    18

        >>> test_dice_dict_valid = {3: 4, 1: 1}
    >>> user_selection_threes = 3
    >>> get_category_value_upper(test_dice_dict_valid, user_selection_threes)
    12

    """
    if user_selection == 1:
        if 1 in dice_dict.keys():
            return 1 * dice_dict[1]

    if user_selection == 2:
        if 2 in dice_dict.keys():
            return 2 * dice_dict[2]

    if user_selection == 3:
        if 3 in dice_dict.keys():
            return 3 * dice_dict[3]

    if user_selection == 4:
        if 4 in dice_dict.keys():
            return 4 * dice_dict[4]

    if user_selection == 5:
        if 5 in dice_dict.keys():
            return 5 * dice_dict[5]

    if user_selection == 6:
        if 6 in dice_dict.keys():
            return 6 * dice_dict[6]

    else:
        return NO_SCORE()


def re_roll_dice(dice_list: list, dice_to_re_roll: list) -> list:
    """
    Returns a list of integers containing new random integers simulating a re-roll of the 6-sided
    dice rolls specified by the user.

    Accepts a list of integers representing the player's dice rolls, and a list
    containing the number(s) of the dice that the player would like to re-roll.

    :param dice_list: A list.
    :param dice_to_re_roll: A list.
    :precondition dice_list: A list of integers containing five integers ranging from 1-6
                             representing the player's dice rolls.
    :precondition dice_to_re_roll: A list of integers representing the number of the dice
                                  that the user would like to re-roll
    :postcondition: Returns a list containing five integers ranging from 1-6 representing the
                    the player's dice rolls and/or the re-rolls specified by the user.
    :return: A list.
    """
    for dice in range(0, len(dice_to_re_roll)):
        dice_list.pop(dice_to_re_roll[dice] - (dice + 1))

    new_rolls = roll_dice(len(dice_to_re_roll))
    new_rolls.extend(dice_list)

    return new_rolls


def dice_list_printer(dice_list: list):
    """
    Nothing is returned, prints out multiple strings.

    Accepts a list of random integers representing the player's current hand of dice, and prints
    multiple strings to display the player's dice.

    :param dice_list: A list.
    :precondition dice_list: A list of integers containing five integers ranging from 1-6
                             representing the player's dice rolls.
    :postcondition: Multiple strings are printed displaying the player's hand of dice.
    :return: Nothing is returned, multiple strings are printed.

    >>> dice_list_all_ones = [1, 1, 1, 1, 1]
    >>> dice_list_printer(dice_list_all_ones)
    <BLANKLINE>
    Here is your current hand of dice:
    <BLANKLINE>
    --------------------
    Dice #1 -----> 1
    Dice #2 -----> 1
    Dice #3 -----> 1
    Dice #4 -----> 1
    Dice #5 -----> 1
    -------------------
    <BLANKLINE>

    >>> dice_list_unique_rolls = [5, 6, 2, 1, 3]
    >>> dice_list_printer(dice_list_unique_rolls)
    <BLANKLINE>
    Here is your current hand of dice:
    <BLANKLINE>
    --------------------
    Dice #1 -----> 5
    Dice #2 -----> 6
    Dice #3 -----> 2
    Dice #4 -----> 1
    Dice #5 -----> 3
    -------------------
    <BLANKLINE>

    >>> dice_list_some_duplicate_rolls = [5, 6, 5, 6, 3]
    >>> dice_list_printer(dice_list_some_duplicate_rolls)
    <BLANKLINE>
    Here is your current hand of dice:
    <BLANKLINE>
    --------------------
    Dice #1 -----> 5
    Dice #2 -----> 6
    Dice #3 -----> 5
    Dice #4 -----> 6
    Dice #5 -----> 3
    -------------------
    <BLANKLINE>
    """
    print("\nHere is your current hand of dice:\n")
    print("--------------------")

    for roll in range(1, 5 + 1):
        print(f"Dice #{roll} -----> {dice_list[roll - 1]}")

    print("-------------------\n")


def roll_dice(num_of_rolls: int) -> list:
    """
    Returns a list containing a specified amount of random integers representing
    simulated 6-sided dice rolls.

    :param num_of_rolls: An integer.
    :precondition: An integer representing the number of 6-sided dice rolls to be simulated.
    :postcondition: Returns a list of a specified amount of random integers representing simulated
                    6-sided dice rolls.
    :return: A list.
    """
    dice_list = random.choices([1, 2, 3, 4, 5, 6], k=num_of_rolls)

    return dice_list


def is_valid_re_roll_choice() -> str:
    """
    Returns a string representing valid player input.

    Uses a while loop to ensure that the player's input is valid. Returns the validated string
    representing the player's choice to re-roll their hand of dice.

    :param: N/A, no parameters accepted.
    :precondition: N/A, no parameters accepted.
    :postcondition: A string that represents valid input from the player for deciding if they would
                    like to keep their current hand of dice, or re-roll it.
    :return: A string.
    """
    player_re_roll_choice = input("\nEnter 0 if you want to keep your hand of dice, or 1 if you"
                                  " would like to re-roll dice: ").strip()

    valid_input = False
    while not valid_input:

        if player_re_roll_choice in ["0", "1"]:
            valid_input = True

        else:
            player_re_roll_choice = input("\nPlease enter either a 0 or 1: ")

    return player_re_roll_choice


def get_valid_dice_to_re_roll(num_of_dice_to_re_roll: int) -> list:
    """
    Returns a list representing the player's dice that they would like to re-roll.

    Accepts an integer representing the number of dice the player would like to re-roll, and
    prompts, and validates, the dice that the player would like to re-roll.

    :param num_of_dice_to_re_roll: An integer.
    :precondition: An integer between 1 and 4 representing the dice that the player would like to
                   re-roll.
    :postconditon: A list containing integers representing the validated input of the dice that
                   the player would like to re-roll.
    :return: A list.
    """
    valid_input = False

    while not valid_input:
        dice_to_re_roll_set = set()

        counter = 0
        continue_loop = True
        while counter < num_of_dice_to_re_roll and continue_loop is True:
            player_choice = input("\nPlease enter the number associated with the dice you would like to re-roll (1 to 5)."
                                  "\nDuplicate entries will be deleted!: ")

            if player_choice not in ["1", "2", "3", "4", "5"]:
                print("\nInvalid input!")
                continue_loop = False

            else:
                dice_to_re_roll_set.add(player_choice)
                counter += 1

        valid_input = True

    dice_to_re_roll = list(map(int, dice_to_re_roll_set))

    return dice_to_re_roll


def get_valid_num_of_dice_to_re_roll() -> int:
    """
    No parameters accepted, returns an integers representing the number of dice that the player
    would like to re-roll.

    Returns an integer representing the player's selection for how many dice they would
    like to re-roll. While loops ensure that the player's selection is valid.

    :param: N/A, no parameters accepted.
    :precondition: N/A, no parameters accepted.
    :postcondition: A valid integer is returned representing the player's choice for how many dice
                    they would like to re-roll,
    :return: An integer.
    """
    valid_input = False
    while not valid_input:

        num_of_dice_to_re_roll = input(
            "\nHow many dice would you like to re-roll?"
            "\nSelect a number from 1 to 5, or type 0 to continue with your"
            " current hand of dice: ").strip()

        if num_of_dice_to_re_roll not in ["1", "2", "3", "4", "5", "0"]:
            print("\nInvalid input!")

        else:
            valid_input = True

    return int(num_of_dice_to_re_roll)


def dice_re_roll_handler(dice_list: list) -> list:
    """
    Returns a list representing the player's re-rolled hand of dice.

    Accepts a list representing the current hand of dice for the player, and calls on a series
    of helper functions to ensure valid input from the player, and to allow the player to re-roll
    which ever dice they specify in their hand. Returns a list containing the new rolls specified
    by the player.

    :param dice_list: A list.
    :precondition: A list containing the random integers representing the random 6-sided dice rolls
                   of the player.
    :postconditon: Returns a list containing five random integers containing the
                   new dice rolls specified by the player.
    :return: A list.
    """
    re_rolls = 0
    while re_rolls < 3:

        num_of_dice_to_re_roll = get_valid_num_of_dice_to_re_roll()

        if num_of_dice_to_re_roll in [1, 2, 3, 4]:
            dice_to_re_roll = get_valid_dice_to_re_roll(num_of_dice_to_re_roll)
            dice_list = re_roll_dice(dice_list, dice_to_re_roll)
            dice_list_printer(dice_list)

            re_rolls += 1

        elif num_of_dice_to_re_roll == 0:
            break

        else:
            dice_list = roll_dice(5)
            dice_list_printer(dice_list)

            re_rolls += 1

    return dice_list


def update_score_sheet(score_sheet: dict, user_category_selection: int, category_value: int) -> dict:
    """
    Returns a dictionary representing the updated score sheet of a player.

    Updates the player's score sheet based on their choice represented by a tuple and returns a
    dictionary of the updated player's score sheet.

    :param score_sheet: A dictionary.
    :param user_category_selection: A string.
    :param category_value: A string.
    :precondition score_sheet: A dictionary with the key, value, pairs representing the player's
                               Yahtzee score sheet.
    :precondition user_selection: A string containing the number of the category that the player
                                  would like to fill in on their score sheet. The user selection
                                  must be between 1 and 14.
    :precondition category_value: A string containing the value to be updated in the specified
                                  category for the player score sheet.
    :postcondition: A dictionary containing the updated score sheet of the player.
    :return: A dictionary.

    >>> player_score_sheet_add_sixes = {'player': 'Username', 'Aces': -1, 'Twos': -1, \
'Threes': -1, 'Fours': -1, 'Fives': -1, \
'Sixes': -1, '3 of a kind': -1, '4 of a kind': -1, \
'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1, \
'Chance': -1, 'Yahtzee Bonus': [], 'Total of Upper': '0', \
'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}
    >>> test_user_selection = 6
    >>> test_category_value = 18
    >>> update_score_sheet(player_score_sheet_add_sixes, test_user_selection, \
    test_category_value)
    {'player': 'Username', 'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, \
'Fives': -1, 'Sixes': 18, '3 of a kind': -1, '4 of a kind': -1, \
'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1, \
'Chance': -1, 'Yahtzee Bonus': [], 'Total of Upper': '0', \
'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}

    >>> player_score_sheet_add_full_house = {'player': 'Username', 'Aces': 3, 'Twos': 6, \
'Threes': 17, 'Fours': -1, 'Fives': -1, \
'Sixes': -1, '3 of a kind': -1, '4 of a kind': -1, \
'Full House': -1, 'Small Straight': -1, 'Large Straight': 40, 'Yahtzee': -1, \
'Chance': -1, 'Yahtzee Bonus': [], 'Total of Upper': '0', \
'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}
    >>> test_user_selection = 9
    >>> test_category_value = 25
    >>> update_score_sheet(player_score_sheet_add_full_house, test_user_selection, \
    test_category_value)
    {'player': 'Username', 'Aces': 3, 'Twos': 6, \
'Threes': 17, 'Fours': -1, 'Fives': -1, \
'Sixes': -1, '3 of a kind': -1, '4 of a kind': -1, \
'Full House': 25, 'Small Straight': -1, 'Large Straight': 40, 'Yahtzee': -1, \
'Chance': -1, 'Yahtzee Bonus': [], 'Total of Upper': '0', \
'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}
    """
    keys_list = list(score_sheet.keys())
    category = keys_list[user_category_selection]

    score_sheet[category] = category_value
    return score_sheet


def final_score_calculator(score_sheet: dict) -> int:
    """
    Returns an integer representing the final and total score of the provided player's score sheet.

    :param score_sheet: A dictionary.
    :precondition score_sheet: A dictionary with the key, value, pairs representing player one's
                               score sheet.
    :postcondition: An integer representing the total and final score for a provided player's
                    Yahtzee's score sheet.
    :return: An integer.
    """
    keys_list = list(score_sheet.keys())
    temp_list_filled_categories = []

    for category_num in range(1, 13 + 1):
        category = keys_list[category_num]

        temp_list_filled_categories.append(score_sheet[category])

    return sum(temp_list_filled_categories)


def check_scores_filled(score_sheet: dict) -> bool:
    """
    Returns a boolean if depending if all of the categories for the score sheet has been filled out.

    Checks if the score sheet is filled out. Returns true if the score sheet is filled out,
    otherwise False is returned.

    :param: A dictionary.
    :precondition: A dictionary containing the keys and values of the player's Yahtzee score sheet.
    :postcondition: A boolean value is returned depending if the player's score sheet has been
                    filled.
    :return: A boolean.

    >>> player_score_sheet_none_filled = {'player': 'Username', 'Aces': -1, 'Twos': -1, \
'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, \
'3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, 'Small Straight': -1, \
'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1, 'Yahtzee Bonus': [], \
'Total of Upper': '0', 'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}
    >>> check_scores_filled(player_score_sheet_none_filled)
    False

    >>> player_score_sheet_fifth_turn = {'player': 'Username', 'Aces': '3', 'Twos': -1, \
'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, \
'3 of a kind': -1, '4 of a kind': -1, 'Full House': '25', 'Small Straight': -1, \
'Large Straight': '40', 'Yahtzee': '50', 'Chance': -1, 'Yahtzee Bonus': [], \
'Total of Upper': '0', 'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}
    >>> check_scores_filled(player_score_sheet_fifth_turn)
    False

    >>> player_score_sheet_one_turn_left = {'player': 'Username', 'Aces': '3', 'Twos': '6', \
'Threes': '3', 'Fours': '16', 'Fives': '5', 'Sixes': '12', \
'3 of a kind': '18', '4 of a kind': '27', 'Full House': '25', 'Small Straight': '30', \
'Large Straight': -1, 'Yahtzee': '0', 'Chance': '17', 'Yahtzee Bonus': [], \
'Total of Upper': '0', 'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}
    >>> check_scores_filled(player_score_sheet_one_turn_left)
    False

    >>> player_score_sheet_filled = {'player': 'Username', 'Aces': '4', 'Twos': '6', \
'Threes': '3', 'Fours': '16', 'Fives': '10', 'Sixes': '18', \
'3 of a kind': '22', '4 of a kind': '27', 'Full House': '25', 'Small Straight': '30', \
'Large Straight': '40', 'Yahtzee': '0', 'Chance': '17', 'Yahtzee Bonus': [], \
'Total of Upper': '0', 'Total of Lower': '0', 'Upper Bonus': '0', 'Grand Total': '0'}
    >>> check_scores_filled(player_score_sheet_filled)
    True
    """
    keys_list = list(score_sheet.keys())
    temp_list_filled_categories = []

    for category_num in range(1, 13 + 1):
        category = keys_list[category_num]
        if score_sheet[category] != -1:
            temp_list_filled_categories.append("1")

    if len(temp_list_filled_categories) == 13:
        return True
    else:
        return False


def get_valid_user_category_choice() -> int:
    valid_input = False
    while not valid_input:

        user_category_choice = input("\nPlease enter a number associated with the category you"
                                     " would like to fill in on your score sheet (1 - 13): ")

        if user_category_choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]:
            print("\nInvalid input!")

        else:
            valid_input = True

    return int(user_category_choice)


def player_two_turn_handler(score_sheet: dict):
    """
    Returns nothing. Calls on helper functions to carry out player two's turn.

    :param score_sheet: A dictionary.
    :precondition score_sheet: A dictionary with the key, value, pairs representing player one's
                               score sheet.
    :postcondition: Calls on helper functions to carry out player two's turn of Yahtzee.
    :return: Nothing is returned.
    """
    print("Player 2's turn!")

    score_sheet_printer(score_sheet)

    dice_list = roll_dice(5)
    dice_list_printer(dice_list)

    player_re_roll_choice = is_valid_re_roll_choice()

    if player_re_roll_choice == "1":
        dice_re_roll_handler(dice_list)

    dice_dict = dice_list_to_dict(dice_list)
    NUMBERED_CATEGORIES()

    player_category_choice = get_valid_user_category_choice()
    if player_category_choice in [1, 2, 3, 4, 5, 6]:
        category_value = get_category_value_upper(dice_dict, player_category_choice)
    else:
        category_value = get_category_value_lower(score_sheet, dice_list, dice_dict,
                                                  player_category_choice)

    score_sheet = update_score_sheet(score_sheet, player_category_choice, category_value)

    return score_sheet


def player_one_turn_handler(score_sheet: dict):
    """
    Returns nothing. Calls on helper functions to carry out player one's turn.

    :param score_sheet: A dictionary.
    :precondition score_sheet: A dictionary with the key, value, pairs representing player one's
                               score sheet.
    :postcondition: Calls on helper functions to carry out player one's turn of Yahtzee.
    :return: Nothing is returned.
    """
    print("Player 1's turn!")

    score_sheet_printer(score_sheet)

    dice_list = roll_dice(5)
    dice_list_printer(dice_list)

    player_re_roll_choice = is_valid_re_roll_choice()

    if player_re_roll_choice == "1":
        dice_re_roll_handler(dice_list)

    dice_dict = dice_list_to_dict(dice_list)
    NUMBERED_CATEGORIES()

    player_category_choice = get_valid_user_category_choice()
    if player_category_choice in [1, 2, 3, 4, 5, 6]:
        category_value = get_category_value_upper(dice_dict, player_category_choice)
    else:
        category_value = get_category_value_lower(score_sheet, dice_list, dice_dict,
                                                  player_category_choice)

    score_sheet = update_score_sheet(score_sheet, player_category_choice, category_value)

    return score_sheet


def who_won(player1_score_sheet, player2_score_sheet):
    """
    Manages the turn order of both players and ends the game when both player's scorecards have
    been filled out.

    Calls on a series of helper functions to run the turn orders. Uses a while loop to check if
    both player's scorecards have been filled, and ends if both scorecards have been filled.

    :param player1_score_sheet: A dictionary.
    :param player2_score_sheet: A dictionary.

    :return: Nothing is returned.
    """
    player1_score = final_score_calculator(player1_score_sheet)
    player2_score = final_score_calculator(player2_score_sheet)

    if player1_score > player2_score:
        print("Player 1 wins the game, congratulations!")
    else:
        print("Player 2 wins the game, congratulations!")


def game():
    """
    Loops until the game is over, calls on helper functions to drive the game.

    Calls on a series of helper functions to run the Yahtzee game. Uses a while loop to run the game
    until the player has completed their game of Yahtzee.

    :param: None, no parameters accepted.
    :precondition: N/A, no parameters accepted.
    :postcondition: Runs the Yahtzee game until the player has completed their game.
    :return: Nothing is returned.
    """
    print("Hello and welcome to Yahtzee! (all rights reserved by Hasbro)")

    player1_score_sheet = generate_score_sheet("Player 1")
    player2_score_sheet = generate_score_sheet("Player 2")

    player1_score_sheet_filled = False
    player2_score_sheet_filled = False

    while not player1_score_sheet_filled or not player2_score_sheet_filled:

        if not player1_score_sheet_filled:
            player1_score_sheet = player_one_turn_handler(player1_score_sheet)
            score_sheet_printer(player1_score_sheet)

        if not player2_score_sheet_filled:
            player2_score_sheet = player_two_turn_handler(player2_score_sheet)
            score_sheet_printer(player2_score_sheet)

    who_won(player1_score_sheet, player2_score_sheet)


def main():
    """Executes the Program"""
    game()


if __name__ == "__main__":
    main()
