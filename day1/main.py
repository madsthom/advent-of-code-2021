from day1.sonar_sweep import input_from_file, increase_count, sliding_increase_count


def part_one():
    measurement_input = input_from_file("input")
    count = increase_count(measurement_input)
    print(count)


def part_two():
    measurement_input = input_from_file("input")
    count = sliding_increase_count(measurement_input)
    print(count)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
