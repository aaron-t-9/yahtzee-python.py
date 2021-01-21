"""
Unit-test for roll_dice

Aaron T.
"""

from unittest import TestCase
from unittest.mock import patch
from yahtzee import roll_dice


class TestRollDice(TestCase):

    @patch('random.choices', return_value=[1, 2, 3, 4, 5])
    def test_consecutive_roll_5_rolls(self, random_number_generator):

        expected_output = [1, 2, 3, 4, 5]

        num_of_rolls = 5
        actual_value = roll_dice(num_of_rolls)

        self.assertEqual(expected_output, actual_value)

    @patch('random.choices', return_value=[1, 1, 1, 1, 1])
    def test_yahtzee_roll_5_rolls(self, random_number_generator):

        expected_output = [1, 1, 1, 1, 1]

        num_of_rolls = 5
        actual_value = roll_dice(num_of_rolls)

        self.assertEqual(expected_output, actual_value)

    @patch('random.choices', return_value=[3, 2, 3, 2, 3])
    def test_full_house_roll_5_rolls(self, random_number_generator):

        expected_output = [3, 2, 3, 2, 3]

        num_of_rolls = 5
        actual_value = roll_dice(num_of_rolls)

        self.assertEqual(expected_output, actual_value)

    @patch('random.choices', return_value=[1, 2, 5, 2])
    def test_4_rolls(self, random_number_generator):

        expected_output = [1, 2, 5, 2]

        num_of_rolls = 4
        actual_value = roll_dice(num_of_rolls)

        self.assertEqual(expected_output, actual_value)

    @patch('random.choices', return_value=[6, 1])
    def test_2_rolls(self, random_number_generator):

        expected_output = [6, 1]

        num_of_rolls = 2
        actual_value = roll_dice(num_of_rolls)

        self.assertEqual(expected_output, actual_value)

    @patch('random.choices', return_value=[5])
    def test_1_roll(self, random_number_generator):
        expected_output = [5]

        num_of_rolls = 1
        actual_value = roll_dice(num_of_rolls)

        self.assertEqual(expected_output, actual_value)


