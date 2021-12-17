def main():
    lines = load_file('input').split('\n')
    parsed_lines = parse_input_lines(lines)

    print(part_one(parsed_lines))
    print(part_two(parsed_lines))


def part_one(lines):
    summe = 0
    for numbers, digits in lines:
        summe += sum(1 for x in digits if x in [numbers[y] for y in [1, 4, 7, 8]])
    return summe


def part_two(lines):
    summe = 0
    for numbers, digits in lines:
        nums = find_correct_numbers(numbers)
        summe += int("".join([str(nums.index(x)) for x in digits]))
    return summe


def find_correct_numbers(numbers):
    n1 = [x for x in numbers if len(x) == 2][0]
    n4 = [x for x in numbers if len(x) == 4][0]
    n7 = [x for x in numbers if len(x) == 3][0]
    n8 = [x for x in numbers if len(x) == 7][0]
    n9 = [x for x in numbers if len(x) == 6 and all(y in x for y in n4)][0]
    n0 = [x for x in numbers if len(x) == 6 and x != n9 and all(y in x for y in n1)][0]
    n6 = [x for x in numbers if len(x) == 6 and x != n9 and x != n0][0]
    n3 = [x for x in numbers if len(x) == 5 and all(y in x for y in n1)][0]
    n5 = [x for x in numbers if len(x) == 5 and x != n3 and all(y in n9 for y in x)][0]
    n2 = [x for x in numbers if len(x) == 5 and x != n3 and x != n5][0]
    return [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]


def most_of_letter_in_arrays(seven_segments, letter):
    max_count = (0, 0)
    for i in seven_segments:
        count = seven_segments[i].count(letter)
        if count > max_count[0]:
            max_count = (count, i)
    return max_count


def load_file(file_name):
    with open(file_name) as f:
        return str(f.read())


def parse_input_lines(lines):
    lines = [[["".join(sorted(n)) for n in l.split(" ")] for l in line.split(' | ')] for line in lines]
    return lines


if __name__ == '__main__':
    main()
