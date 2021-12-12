import math

from helpers.file_handling import raw_input_from_file


def most_common_bit(index: int, numbers: [int]):
    ones = 0
    for num in numbers:
        if num[index - 1] == '1':
            ones = ones + 1
    if math.ceil(len(numbers) / 2) <= ones:
        return 1
    else:
        return 0


def calculate_gamma_rate(binary_strings):
    gamma_rate = ""
    length = len(binary_strings[0])
    for index in range(length):
        gamma_rate += str(most_common_bit(index + 1, binary_strings))
    return int(gamma_rate, 2)


def calculate_epsilon_rate(binary_strings):
    epsilon_rate = ""
    length = len(binary_strings[0])
    for index in range(length):
        epsilon_rate += "0" if str(most_common_bit(index + 1, binary_strings)) == "1" else "1"

    return int(epsilon_rate, 2)


def parse_binary_strings(file_name):
    input_text = raw_input_from_file(file_name)
    return input_text.splitlines()


def find_oxygen_gen_rating(binary_strings):
    bin_list = list(binary_strings)
    index = 1
    while len(bin_list) != 1:
        most_common = most_common_bit(index, bin_list)
        if most_common == 1:
            bin_list = list(filter(lambda x: x[index - 1] == '1', bin_list))
        elif most_common == 0:
            bin_list = list(filter(lambda x: x[index - 1] == '0', bin_list))
        index = index + 1

    return int(bin_list[0], 2)


def find_co2_scrubber_rating(binary_strings):
    bin_list = list(binary_strings)
    index = 1
    while len(bin_list) != 1:
        most_common = most_common_bit(index, bin_list)
        if most_common == 1:
            bin_list = list(filter(lambda x: x[index - 1] == '0', bin_list))
        elif most_common == 0:
            bin_list = list(filter(lambda x: x[index - 1] == '1', bin_list))
        index = index + 1

    return int(bin_list[0], 2)
