import unittest

from day5.lines import parse_lines_input, parse_line


class LinesTestCase(unittest.TestCase):
    def test_can_parse_test_input(self):
        lines = parse_lines_input("test_input")
        self.assertEqual(10, len(lines))

    def test_can_parse_line_description(self):
        line = parse_line("9,0 -> 9,5")
        self.assertEqual(((9, 0), (9, 5)), line)


if __name__ == '__main__':
    unittest.main()
