from day2.dive import parse_commands, calculate_position
from helpers.file_handling import raw_input_from_file


def main():
    part_one_and_two()
    

def part_one_and_two():
    input_string = raw_input_from_file("input")
    commands = parse_commands(input_string)
    position = calculate_position(commands)
    print(position)
    print(position[0] * position[1])


if __name__ == '__main__':
    main()
