import numpy as np

from helpers.file_handling import raw_input_from_file


def parse_numbers_drawn(file_name):
    raw_input = raw_input_from_file(file_name)
    numbers_string = raw_input.splitlines()[0]
    numbers_to_be_drawn = numbers_string.split(",")

    return numbers_to_be_drawn


def parse_boards(file_name):
    raw_input = raw_input_from_file(file_name)
    lines = raw_input.splitlines()
    board_lines = lines[2:len(lines)]
    boards = []
    board = np.zeros((5, 5), dtype='2i')
    count = 0
    for index in range(len(board_lines)):
        if board_lines[index] == "":
            boards.append(board)
            board = np.zeros((5, 5), dtype='2i')
            count = 0
        else:
            numbers = [(int(num), 0) for num in board_lines[index].split()]
            board[count, :] = numbers
            count = count + 1
    return boards


def update_boards(boards, numbers_drawn, step):
    drawn_number = int(numbers_drawn[step])
    for board in boards:
        for row in board:
            for num in row:
                if num[0] == drawn_number:
                    num[1] = 1
    return boards


def find_last(boards, numbers_drawn):
    last = None
    last_num = 0
    while len(boards) != 0:
        board, number = check_boards(boards, numbers_drawn)
        boards = list(filter(lambda x: not np.array_equal(x, board), boards))
        if len(boards) == 1:
            last = boards[0]
        if len(boards) == 0:
            last_num = number

    return last, last_num


def check_boards(boards, numbers_drawn):
    bingo = False
    step = -1
    winning_board = None
    winning_number = 0
    while not bingo:
        step = step + 1
        boards = update_boards(boards, numbers_drawn, step)
        for board in boards:
            for row in board:
                if [r[1] for r in row] == [1, 1, 1, 1, 1]:
                    winning_board = board
                    winning_number = int(numbers_drawn[step])
                    return winning_board, winning_number

        for board in boards:
            for elm in range(5):
                fill_count = 0
                for col in board:
                    if col[elm][1] == 1:
                        fill_count = fill_count + 1
                if fill_count == 5:
                    winning_board = board
                    winning_number = int(numbers_drawn[step])
                    return winning_board, winning_number


def calculate_score(winning_number, winning_board):
    sumb = 0
    for row in winning_board:
        for number in row:
            if int(number[1]) == 0:
                sumb = sumb + int(number[0])

    return sumb * winning_number
