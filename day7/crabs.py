def read_test_input(file_name):
    with open(file_name) as f:
        return str(f.read())


def split_on_commas(input_string):
    strings = input_string.split(',')
    ints = [int(s) for s in strings]
    return ints


def positions_to_dict(positions):
    positions_dict = {}
    for i in range(len(positions)):
        if positions[i] in positions_dict:
            positions_dict[positions[i]] += 1
        else:
            positions_dict[positions[i]] = 1
    return positions_dict


def main():
    input_string = read_test_input('input')
    positions = split_on_commas(input_string)

    one = part_one(positions)
    print(one)
    two = path_two(positions)
    print(two)


def path_two(positions):
    smallest = 1000000000
    for i in range(max(positions)):
        s = 0
        for j in range(len(positions)):
            n = int((abs(positions[j] - i) * (abs(positions[j] - i) + 1)) / 2)
            s = s + n
        smallest = min(smallest, s)
    return smallest


def part_one(positions):
    smallest = 1000000000
    for i in range(max(positions)):
        s = 0
        for j in range(len(positions)):
            s = s + abs(positions[j] - i)
        smallest = min(smallest, s)
    return smallest


if __name__ == "__main__":
    main()
