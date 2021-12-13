from helpers.file_handling import raw_input_from_file


def parse_numbers_drawn(file_name):
    raw_input = raw_input_from_file(file_name)
    numbers_string = raw_input.splitlines()[0]
    numbers_to_be_drawn = numbers_string.split(",")

    return numbers_to_be_drawn


def parse_boards(file_name):
    raw_input = raw_input_from_file(file_name)
    lines = raw_input.splitlines()
    board_lines = list(filter(lambda x: x != "", lines[1:len(lines)]))
    boards = []
    board = []
    for index in range(len(board_lines)):
        numbers = board_lines[index].split()
        board.append(numbers)
        if index % 5 == 0:
            boards.append(board)
            board = []
    return boards
