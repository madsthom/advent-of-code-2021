import unittest

from day4.bingo import parse_numbers_drawn, parse_boards


class MyTestCase(unittest.TestCase):
    def test_parse_numbers_drawn(self):
        numbers_drawn = parse_numbers_drawn("input")
        self.assertEqual("27", numbers_drawn[0])
        self.assertEqual("14", numbers_drawn[1])
        self.assertEqual("28", numbers_drawn[len(numbers_drawn) - 1])

    def test_parse_boards(self):
        boards = parse_boards("input")
        self.assertEqual("31 23 52 26 8", boards[0][1])


if __name__ == '__main__':
    unittest.main()
