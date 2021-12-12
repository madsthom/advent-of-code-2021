import unittest

from day2.dive import parse_commands, calculate_position


class Day2TestCase(unittest.TestCase):
    def test_parse_forward(self):
        commands = parse_commands("forward 2\n")
        self.assertEqual({"forward": 2, "down": 0, "up": 0, "aim": 0}, commands)

    def test_parse_down(self):
        commands = parse_commands("down 2\n")
        self.assertEqual({"down": 0, "forward": 0, "up": 0, "aim": 2}, commands)

    def test_parse_up(self):
        commands = parse_commands("up 2\n")
        self.assertEqual({"up": 0, "down": 0, "forward": 0, "aim": -2}, commands)

    def test_multiple_commands(self):
        commands = parse_commands("forward 2\ndown 2\nforward 3\n")
        self.assertEqual({"forward": 5, "down": 6, "up": 0, "aim": 2}, commands)

    def test_multiple_commands_with_up(self):
        commands = parse_commands("forward 2\ndown 5\nforward 3\nup 2\n")
        self.assertEqual({"forward": 5, "down": 15, "up": 0, "aim": 3}, commands)

    def test_calculate_position(self):
        commands = parse_commands("forward 2\ndown 5\nforward 3\nup 2\n")
        self.assertEqual((5, 15), calculate_position(commands))

    def test_example(self):
        test_input = """forward 5
                    down 5
                    forward 8
                    up 3
                    down 8
                    forward 2"""
        # {"forward": 5, "down": 0, "up": 0, "aim": 5}
        commands = parse_commands(test_input)
        position = calculate_position(commands)
        self.assertEqual((15, 60), position)
        self.assertEqual(900, position[0] * position[1])


if __name__ == '__main__':
    unittest.main()
