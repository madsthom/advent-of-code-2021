import unittest

from day3.power_consumption import most_common_bit, calculate_gamma_rate, calculate_epsilon_rate, parse_binary_strings, \
    find_oxygen_gen_rating, find_co2_scrubber_rating


class PowerConsumptionTestCase(unittest.TestCase):

    def setUp(self):
        self.binary_strings = parse_binary_strings("test_input")

    def test_input_of_binary_numbers(self):
        self.assertEqual("00100", self.binary_strings[0])
        self.assertEqual("11110", self.binary_strings[1])
        self.assertEqual("01010", self.binary_strings[len(self.binary_strings) - 1])

    def test_most_common_first_bit(self):
        self.assertEqual(1, most_common_bit(1, self.binary_strings))
        self.assertEqual(0, most_common_bit(2, self.binary_strings))
        self.assertEqual(1, most_common_bit(3, self.binary_strings))
        self.assertEqual(1, most_common_bit(4, self.binary_strings))
        self.assertEqual(0, most_common_bit(5, self.binary_strings))

    def test_calculate_gamma_rate(self):
        self.assertEqual(22, calculate_gamma_rate(self.binary_strings))

    def test_calculate_epsilon_rate(self):
        self.assertEqual(9, calculate_epsilon_rate(self.binary_strings))

    def test_oxygen_gen_rating(self):
        self.assertEqual(23, find_oxygen_gen_rating(self.binary_strings))
        self.assertEqual(10, find_co2_scrubber_rating(self.binary_strings))


if __name__ == '__main__':
    unittest.main()
