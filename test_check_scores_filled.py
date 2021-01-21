"""
Unit-test for check_scores_filled

Aaron T.
"""

from unittest import TestCase
from yahtzee import check_scores_filled


class TestCheckScoresFilled(TestCase):

    def test_empty_score_sheet(self):
        score_sheet = {'player': 'Username', 'Aces': 'None', 'Twos': 'None',
                       'Threes': 'None', 'Fours': 'None', 'Fives': 'None',
                       'Sixes': 'None', '3 of a kind': 'None',
                       '4 of a kind': 'None', 'Full House': 'None',
                       'Small Straight': 'None', 'Large Straight': 'None',
                       'Yahtzee': 'None', 'Chance': 'None', 'Yahtzee Bonus': [],
                       'Total of Upper': '0', 'Total of Lower': '0',
                       'Upper Bonus': '0', 'Grand Total': '0'}
        expected_output = True
        actual_value = check_scores_filled(score_sheet)

        self.assertEqual(expected_output, actual_value)

    def test_partially_full_score_sheet(self):
        score_sheet = {'player': 'Username', 'Aces': '3', 'Twos': '8',
                       'Threes': '12', 'Fours': 'None', 'Fives': 'None',
                       'Sixes': 'None', '3 of a kind': 'None',
                       '4 of a kind': 'None', 'Full House': '25',
                       'Small Straight': '30', 'Large Straight': 'None',
                       'Yahtzee': 'None', 'Chance': 'None', 'Yahtzee Bonus': [],
                       'Total of Upper': '0', 'Total of Lower': '0',
                       'Upper Bonus': '0', 'Grand Total': '0'}
        expected_output = True
        actual_value = check_scores_filled(score_sheet)

        self.assertEqual(expected_output, actual_value)

    def test_one_category_empty_score_sheet(self):
        score_sheet = {'player': 'Username', 'Aces': '3', 'Twos': '8',
                       'Threes': '12', 'Fours': '8', 'Fives': '15',
                       'Sixes': '12', '3 of a kind': '16',
                       '4 of a kind': '21', 'Full House': '25',
                       'Small Straight': '30', 'Large Straight': 'None',
                       'Yahtzee': '0', 'Chance': '17', 'Yahtzee Bonus': [],
                       'Total of Upper': '0', 'Total of Lower': '0',
                       'Upper Bonus': '0', 'Grand Total': '0'}
        expected_output = True
        actual_value = check_scores_filled(score_sheet)

        self.assertEqual(expected_output, actual_value)

    def test_one_category_empty_score_sheet_with_yahtzee_bonus(self):
        score_sheet = {'player': 'Username', 'Aces': '3', 'Twos': '8',
                       'Threes': '12', 'Fours': '8', 'Fives': '15',
                       'Sixes': '12', '3 of a kind': '16',
                       '4 of a kind': '21', 'Full House': 'None',
                       'Small Straight': '0', 'Large Straight': '40',
                       'Yahtzee': '50', 'Chance': '17', 'Yahtzee Bonus': ['Y'],
                       'Total of Upper': '0', 'Total of Lower': '0',
                       'Upper Bonus': '0', 'Grand Total': '0'}
        expected_output = True
        actual_value = check_scores_filled(score_sheet)

        self.assertEqual(expected_output, actual_value)

    def test_one_category_empty_score_sheet_with_two_yahtzee_bonus(self):
        score_sheet = {'player': 'Username', 'Aces': '3', 'Twos': '0',
                       'Threes': '12', 'Fours': '8', 'Fives': '15',
                       'Sixes': '12', '3 of a kind': '16',
                       '4 of a kind': '0', 'Full House': '25',
                       'Small Straight': 'None', 'Large Straight': '40',
                       'Yahtzee': '50', 'Chance': '17', 'Yahtzee Bonus': ['Y', 'Y'],
                       'Total of Upper': '0', 'Total of Lower': '0',
                       'Upper Bonus': '0', 'Grand Total': '0'}
        expected_output = True
        actual_value = check_scores_filled(score_sheet)

        self.assertEqual(expected_output, actual_value)

    def test_filled_score_sheet_no_yahtzee_bonus(self):
        score_sheet = {'player': 'Username', 'Aces': '3', 'Twos': '8',
                       'Threes': '12', 'Fours': '8', 'Fives': '15',
                       'Sixes': '12', '3 of a kind': '16',
                       '4 of a kind': '0', 'Full House': '25',
                       'Small Straight': '30', 'Large Straight': '0',
                       'Yahtzee': '0', 'Chance': '17', 'Yahtzee Bonus': [],
                       'Total of Upper': '0', 'Total of Lower': '0',
                       'Upper Bonus': '0', 'Grand Total': '0'}
        expected_output = False
        actual_value = check_scores_filled(score_sheet)

        self.assertEqual(expected_output, actual_value)

    def test_filled_score_sheet_with_two_yahtzee_bonus(self):
        score_sheet = {'player': 'Username', 'Aces': '3', 'Twos': '8',
                       'Threes': '12', 'Fours': '8', 'Fives': '15',
                       'Sixes': '12', '3 of a kind': '16',
                       '4 of a kind': '0', 'Full House': '25',
                       'Small Straight': '30', 'Large Straight': '0',
                       'Yahtzee': '50', 'Chance': '17', 'Yahtzee Bonus': ['Y', 'Y'],
                       'Total of Upper': '0', 'Total of Lower': '0',
                       'Upper Bonus': '0', 'Grand Total': '0'}
        expected_output = False
        actual_value = check_scores_filled(score_sheet)

        self.assertEqual(expected_output, actual_value)
