"""
Unit-test for re_roll_dice

Aaron T.
"""

from unittest import TestCase
from unittest.mock import patch
from yahtzee import re_roll_dice


class TestReRollDice(TestCase):

    @patch('random.choices', return_value=[])
    def test_re_roll_empty(self, random_number_generator):
        dice_list = [6, 2, 1, 2, 3]
        die_to_re_roll = []

        expected_output = [6, 2, 1, 2, 3]
        actual_value = re_roll_dice(dice_list, die_to_re_roll)

        self.assertEqual(expected_output, actual_value)

    @patch('random.choices', return_value=[2])
    def test_re_roll_third_die(self, random_number_generator):
        dice_list = [6, 2, 1, 2, 3]
        die_to_re_roll = [3]

        expected_output = [2, 6, 2, 2, 3]
        actual_value = re_roll_dice(dice_list, die_to_re_roll)

        self.assertEqual(expected_output, actual_value)

    @patch('random.choices', return_value=[6, 6, 6])
    def test_re_roll_first_middle_last_die(self, random_number_generator):
        dice_list = [1, 2, 3, 4, 6]
        die_to_re_roll = [1, 3, 5]

        expected_output = [6, 6, 6, 2, 4]
        actual_value = re_roll_dice(dice_list, die_to_re_roll)

        self.assertEqual(expected_output, actual_value)

    @patch('random.choices', return_value=[6, 6])
    def test_re_roll_first_last_die(self, random_number_generator):
        dice_list = [1, 2, 3, 4, 6]
        die_to_re_roll = [1, 5]

        expected_output = [6, 6, 2, 3, 4]
        actual_value = re_roll_dice(dice_list, die_to_re_roll)

        self.assertEqual(expected_output, actual_value)

    @patch('random.choices', return_value=[3, 5, 3, 1, 4])
    def test_re_roll_all_die(self, random_number_generator):
        dice_list = [6, 3, 3, 4, 2]
        die_to_re_roll = [1, 2, 3, 4, 5]

        expected_output = [3, 5, 3, 1, 4]
        actual_value = re_roll_dice(dice_list, die_to_re_roll)

        self.assertEqual(expected_output, actual_value)
