"""
Unit-test for update_score_sheet

Aaron T.
"""

from unittest import TestCase
from yahtzee import update_score_sheet


class TestUpdateScoreSheet(TestCase):

    def test_add_sixes(self):
        score_sheet = {'player': 'Player', 'Aces': -1, 'Twos': -1,
                       'Threes': -1, 'Fours': -1, 'Fives': -1,
                       'Sixes': -1, '3 of a kind': -1,
                       '4 of a kind': -1,
                       'Full House': -1, 'Small Straight': -1,
                       'Large Straight': -1, 'Yahtzee': -1,
                       'Chance': -1, 'Yahtzee Bonus': [],
                       'Total of Upper': '0',
                       'Total of Lower': '0', 'Upper Bonus': '0',
                       'Grand Total': '0'}
        user_category_selection = 6
        category_value = 18

        expected_output = {'player': 'Player', 'Aces': -1, 'Twos': -1,
                           'Threes': -1, 'Fours': -1, 'Fives': -1,
                           'Sixes': 18, '3 of a kind': -1,
                           '4 of a kind': -1,
                           'Full House': -1, 'Small Straight': -1,
                           'Large Straight': -1, 'Yahtzee': -1,
                           'Chance': -1, 'Yahtzee Bonus': [],
                           'Total of Upper': '0',
                           'Total of Lower': '0', 'Upper Bonus': '0',
                           'Grand Total': '0'}
        actual_value = update_score_sheet(score_sheet, user_category_selection, category_value)

        self.assertEqual(expected_output, actual_value)

    def test_add_aces(self):
        score_sheet = {'player': 'Player', 'Aces': -1, 'Twos': -1,
                       'Threes': -1, 'Fours': -1, 'Fives': -1,
                       'Sixes': -1, '3 of a kind': -1,
                       '4 of a kind': -1,
                       'Full House': -1, 'Small Straight': -1,
                       'Large Straight': -1, 'Yahtzee': -1,
                       'Chance': -1, 'Yahtzee Bonus': [],
                       'Total of Upper': '0',
                       'Total of Lower': '0', 'Upper Bonus': '0',
                       'Grand Total': '0'}
        user_category_selection = 1
        category_value = 4

        expected_output = {'player': 'Player', 'Aces': 4, 'Twos': -1,
                           'Threes': -1, 'Fours': -1, 'Fives': -1,
                           'Sixes': -1, '3 of a kind': -1,
                           '4 of a kind': -1,
                           'Full House': -1, 'Small Straight': -1,
                           'Large Straight': -1, 'Yahtzee': -1,
                           'Chance': -1, 'Yahtzee Bonus': [],
                           'Total of Upper': '0',
                           'Total of Lower': '0', 'Upper Bonus': '0',
                           'Grand Total': '0'}
        actual_value = update_score_sheet(score_sheet, user_category_selection, category_value)

        self.assertEqual(expected_output, actual_value)

    def test_add_3_of_a_kind(self):
        score_sheet = {'player': 'Player', 'Aces': -1, 'Twos': -1,
                       'Threes': -1, 'Fours': -1, 'Fives': -1,
                       'Sixes': -1, '3 of a kind': -1,
                       '4 of a kind': -1,
                       'Full House': -1, 'Small Straight': -1,
                       'Large Straight': -1, 'Yahtzee': -1,
                       'Chance': -1, 'Yahtzee Bonus': [],
                       'Total of Upper': '0',
                       'Total of Lower': '0', 'Upper Bonus': '0',
                       'Grand Total': '0'}
        user_category_selection = 7
        category_value = 25

        expected_output = {'player': 'Player', 'Aces': -1, 'Twos': -1,
                           'Threes': -1, 'Fours': -1, 'Fives': -1,
                           'Sixes': -1, '3 of a kind': 25,
                           '4 of a kind': -1,
                           'Full House': -1, 'Small Straight': -1,
                           'Large Straight': -1, 'Yahtzee': -1,
                           'Chance': -1, 'Yahtzee Bonus': [],
                           'Total of Upper': '0',
                           'Total of Lower': '0', 'Upper Bonus': '0',
                           'Grand Total': '0'}
        actual_value = update_score_sheet(score_sheet, user_category_selection, category_value)

        self.assertEqual(expected_output, actual_value)

    def test_add_yahtzee(self):
        score_sheet = {'player': 'Player', 'Aces': 3, 'Twos': 8,
                       'Threes': -1, 'Fours': 8, 'Fives': -1,
                       'Sixes': 12, '3 of a kind': -1,
                       '4 of a kind': 22,
                       'Full House': -1, 'Small Straight': 30,
                       'Large Straight': -1, 'Yahtzee': -1,
                       'Chance': -1, 'Yahtzee Bonus': [],
                       'Total of Upper': '0',
                       'Total of Lower': '0', 'Upper Bonus': '0',
                       'Grand Total': '0'}
        user_category_selection = 12
        category_value = 50

        expected_output = {'player': 'Player', 'Aces': 3, 'Twos': 8,
                           'Threes': -1, 'Fours': 8, 'Fives': -1,
                           'Sixes': 12, '3 of a kind': -1,
                           '4 of a kind': 22,
                           'Full House': -1, 'Small Straight': 30,
                           'Large Straight': -1, 'Yahtzee': 50,
                           'Chance': -1, 'Yahtzee Bonus': [],
                           'Total of Upper': '0',
                           'Total of Lower': '0', 'Upper Bonus': '0',
                           'Grand Total': '0'}
        actual_value = update_score_sheet(score_sheet, user_category_selection, category_value)

        self.assertEqual(expected_output, actual_value)
