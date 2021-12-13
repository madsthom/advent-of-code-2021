from day1.sonar_sweep import increase_count, sliding_increase_count
from helpers.file_handling import int_input_from_file


def part_one():
    measurement_input = int_input_from_file("input")
    count = increase_count(measurement_input)
    print(count)


def part_two():
    measurement_input = int_input_from_file("input")
    count = sliding_increase_count(measurement_input)
    print(count)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
