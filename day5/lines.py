import numpy as np
import re

def raw_input_from_file(file_name):
    with open(file_name) as f:
        return str(f.read())


def parse_lines_input(file_name):
    line_descriptions = raw_input_from_file(file_name).splitlines()
    lines = []
    for line in line_descriptions:
        lines.append(parse_line(line))
    return lines

# function to parse line description of the form: 60,28 -> 893,861 to match group
def parse_line(line):
    pattern = r"(\d+),(\d+) -> (\d+),(\d+)"
    match = re.match(pattern, line)
    return ((int(match.group(1)), int(match.group(2))), (int(match.group(3)), int(match.group(4))))

def get_indicies(v1, v2, length):
    if v1 > v2:
        step = -1
        return [*range(v1, v2-1, step)]
    elif v1 < v2:
        return [*range(v1, v2+1)]
    else:
        return [v1] * length

def add_line(line, matrix):
    (x1, y1), (x2, y2) = line
    x_diff = abs(x1-x2)
    y_diff = abs(y1-y2)

    is_diagonal = x_diff != 0 and y_diff != 0

    length = max(x_diff, y_diff) + 1

    x_values = get_indicies(x1, x2, length)
    y_values = get_indicies(y1, y2, length)

    for idx, x in enumerate(x_values):
        matrix[x, y_values[idx]] += 1

    return matrix

def add_lines(lines, matrix):
    for line in lines:
        add_line(line, matrix)
    return matrix

def count_overlapping_tiles(matrix):
    return np.sum(matrix > 1)

def print_matrix(matrix):
    for row in matrix:
        string = [str(x) if x != 0 else '.' for x in row]
        print(''.join(string))

def main():
    lines = parse_lines_input("input")
    matrix = np.zeros((1001, 10001), dtype=int)

    matrix = add_lines(lines, matrix)
    
    #print_matrix(matrix)
    print(count_overlapping_tiles(matrix))

if __name__ == '__main__':
    main()



