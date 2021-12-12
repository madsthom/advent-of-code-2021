from day3.power_consumption import parse_binary_strings, calculate_gamma_rate, calculate_epsilon_rate, \
    find_oxygen_gen_rating, find_co2_scrubber_rating


def main():
    part_one()
    part_two()


def part_one():
    binary_strings = parse_binary_strings("input")
    gamma_rate = calculate_gamma_rate(binary_strings)
    epsilon_rate = calculate_epsilon_rate(binary_strings)
    print(gamma_rate * epsilon_rate)


def part_two():
    binary_strings = parse_binary_strings("input")
    oxy = find_oxygen_gen_rating(binary_strings)
    co2 = find_co2_scrubber_rating(binary_strings)
    print(oxy * co2)


if __name__ == '__main__':
    main()
