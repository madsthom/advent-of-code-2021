import unittest

from day1.sonar_sweep import input_from_file, increase_count, sliding_increase_count


class Day1TestCase(unittest.TestCase):
    def test_input_from_file(self):
        """Test that input_from_file returns a list of ints"""
        assert input_from_file("input_test") == [
            199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263
        ]

    def test_count_increase_one(self):
        count = increase_count([199, 200])
        assert count == 1

    def test_count_increase_two(self):
        count = increase_count([199, 200, 201])
        assert count == 2

    def test_count_increase_zero(self):
        count = increase_count([199, 198, 197])
        assert count == 0

    def test_count_increase_more(self):
        count = increase_count([199, 198, 201, 200, 210, 211, 198])
        assert count == 3

    def test_three_sliding_increase(self):
        count = sliding_increase_count([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
        print(count)
        assert count == 5
