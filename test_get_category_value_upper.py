"""
Unit-test for get_category_value_upper

Aaron T.
"""


from unittest import TestCase
from yahtzee import get_category_value_upper


class TestGetCategoryValueUpper(TestCase):

    def test_threes_invalid_user_choice(self):
        dice_dict = {3: 3, 6: 2}
        user_selection = 1

        expected_output = 0
        actual_value = get_category_value_upper(dice_dict, user_selection)

        self.assertEqual(expected_output, actual_value)

    def test_sixes_invalid_user_choice(self):
        dice_dict = {6: 2, 1: 2, 5: 1}
        user_selection = 4

        expected_output = 0
        actual_value = get_category_value_upper(dice_dict, user_selection)

        self.assertEqual(expected_output, actual_value)

    def test_aces(self):
        dice_dict = {1: 3, 5: 1, 3: 1}
        user_selection = 1

        expected_output = 3
        actual_value = get_category_value_upper(dice_dict, user_selection)

        self.assertEqual(expected_output, actual_value)

    def test_aces_single(self):
        dice_dict = {1: 1, 2: 1, 3: 2, 5: 1}
        user_selection = 1

        expected_output = 1
        actual_value = get_category_value_upper(dice_dict, user_selection)

        self.assertEqual(expected_output, actual_value)

    def test_twos(self):
        dice_dict = {2: 3, 3: 1, 5: 1}
        user_selection = 2

        expected_output = 6
        actual_value = get_category_value_upper(dice_dict, user_selection)

        self.assertEqual(expected_output, actual_value)

    def test_threes(self):
        dice_dict = {6: 4, 3: 1}
        user_selection = 3

        expected_output = 3
        actual_value = get_category_value_upper(dice_dict, user_selection)

        self.assertEqual(expected_output, actual_value)

    def test_fours(self):
        dice_dict = {4: 4, 1: 1}
        user_selection = 4

        expected_output = 16
        actual_value = get_category_value_upper(dice_dict, user_selection)

        self.assertEqual(expected_output, actual_value)

    def test_fives(self):
        dice_dict = {3: 3, 2: 1, 5: 1}
        user_selection = 5

        expected_output = 5
        actual_value = get_category_value_upper(dice_dict, user_selection)

        self.assertEqual(expected_output, actual_value)

    def test_sixes(self):
        dice_dict = {6: 2, 3: 2, 5:1}
        user_selection = 6

        expected_output = 12
        actual_value = get_category_value_upper(dice_dict, user_selection)

        self.assertEqual(expected_output, actual_value)
