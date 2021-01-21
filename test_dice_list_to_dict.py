"""
Unit-test for dice_list_to_dict

Aaron T.
"""

from unittest import TestCase
from yahtzee import dice_list_to_dict


class DiceListToDict(TestCase):

    def dice_list(self):
        dice_list = [3, 2, 4, 3, 5]

        expected_output = {3: 2, 2: 1, 4: 1, 5: 1}
        actual_value = dice_list_to_dict(dice_list)

        self.assertEqual(expected_output, actual_value)

    def all_ones(self):
        dice_list = [1, 1, 1, 1, 1]

        expected_output = {1: 5}
        actual_value = dice_list_to_dict(dice_list)

        self.assertEqual(expected_output, actual_value)

    def different_dice(self):
        dice_list = [2, 1, 6, 3, 5]

        expected_output = {1: 5, 2: 1, 5: 1, 6: 1, 3: 1}
        actual_value = dice_list_to_dict(dice_list)

        self.assertEqual(expected_output, actual_value)

