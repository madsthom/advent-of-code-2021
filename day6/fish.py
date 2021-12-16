def read_input_from_file(file_name):
    with open(file_name) as f:
        return str(f.read())

def split_on_commas(input_string):
    strings = input_string.split(',')
    ints = [int(s) for s in strings]
    return ints

def tick_backwards(input_list):
    number_of_new_fish = 0
    for i in range(len(input_list)):
        if input_list[i] == 0:
            input_list[i] = 6
            number_of_new_fish += 1
        else:
            input_list[i] = input_list[i] - 1
    return input_list + [8] * number_of_new_fish

def tick_backwards_for_n_times(input_list, n):
    for i in range(n):
        print(i)
        input_list = tick_backwards(input_list)
    return input_list

def insert_ages_in_dict(input_list, fish_ages):
    for i in range(len(input_list)):
        if input_list[i] in fish_ages:
            fish_ages[input_list[i]] += 1

def tick_ages_in_dict(fish_ages):
    new_fish = fish_ages[0]
    fish_ages[0] = fish_ages[1]
    fish_ages[1] = fish_ages[2]
    fish_ages[2] = fish_ages[3]
    fish_ages[3] = fish_ages[4]
    fish_ages[4] = fish_ages[5]
    fish_ages[5] = fish_ages[6]
    fish_ages[6] = fish_ages[7]
    fish_ages[7] = fish_ages[8]
    fish_ages[8] = new_fish
    fish_ages[6] += new_fish

def tick_ages_in_dict_for_n_times(fish_ages, n):
    for i in range(n):
        tick_ages_in_dict(fish_ages)

def sum_all_fish_ages(fish_ages):
    return sum(fish_ages.values())

def main():
    fish_ages = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    ages = split_on_commas(read_input_from_file('test_input'))
    insert_ages_in_dict(ages, fish_ages)
    tick_ages_in_dict_for_n_times(fish_ages, 256)
    print(sum_all_fish_ages(fish_ages))

if __name__ == "__main__":
    main()