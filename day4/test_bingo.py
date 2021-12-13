import unittest

from day4.bingo import parse_numbers_drawn, parse_boards, update_boards, check_boards, calculate_score


class MyTestCase(unittest.TestCase):
    def test_parse_numbers_drawn(self):
        numbers_drawn = parse_numbers_drawn("input")
        self.assertEqual("27", numbers_drawn[0])
        self.assertEqual("14", numbers_drawn[1])
        self.assertEqual("28", numbers_drawn[len(numbers_drawn) - 1])

    def test_parse_boards(self):
        boards = parse_boards("input")
        first_board = boards[0]
        self.assertEqual(31, first_board[0, 0][0])

        second_board = boards[1]
        self.assertEqual(27, second_board[0, 0][0])

    def test_draw_number_updates_boards(self):
        numbers_drawn = parse_numbers_drawn("input")
        boards = parse_boards("input")
        boards = update_boards(boards, numbers_drawn, 0)
        second_board = boards[1]
        self.assertEqual(27, second_board[0, 0][0])
        self.assertEqual(1, second_board[0, 0][1])

        boards = parse_boards("input")
        winning_board, step = check_boards(boards, numbers_drawn)
        winning_number = numbers_drawn[step]
        print("winning num: " + str(winning_number))
        score = calculate_score(winning_number, winning_board)
        print(score)

    if __name__ == '__main__':
        unittest.main()
