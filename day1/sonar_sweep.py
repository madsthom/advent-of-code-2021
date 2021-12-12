def increase_count(input_array: [int]) -> int:
    count = 0
    for index in range(len(input_array) - 1):
        if input_array[index + 1] > input_array[index]:
            count = count + 1
    return count


def sliding_increase_count(input_array: [int]) -> int:
    count = 0
    for index in range(len(input_array) - 1):
        window_sum = get_window_sum(input_array, index)
        next_window = get_window_sum(input_array, index + 1)
        if window_sum < next_window:
            count = count + 1
    return count


def get_window_sum(input_array: [int], index: int) -> int:
    one = 0
    two = 0
    three = 0
    if index < len(input_array):
        one = input_array[index]
    if index + 1 < len(input_array):
        two = input_array[index + 1]
    if index + 2 < len(input_array):
        three = input_array[index + 2]
    return one + two + three
