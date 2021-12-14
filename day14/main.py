import collections
import time

from day14.polymer import read_input, parse_all_pairs, apply_rules, find_matching_rules


def main():
    polymer_template, pair_insertions = read_input("input")
    pairs = parse_all_pairs(pair_insertions)

    for i in range(40):
        print("step: " + str(i))
        tic = time.perf_counter()
        matching_rules = find_matching_rules(polymer_template, pairs)
        polymer_template = apply_rules(matching_rules, polymer_template)
        toc = time.perf_counter()
        print(f"in {toc - tic:0.4f} seconds")

    common_sorted = collections.Counter(polymer_template).most_common()
    most_common = collections.Counter(polymer_template).most_common(1)[0]
    least_common = common_sorted[len(common_sorted) - 1]
    print(most_common, least_common)
    print(most_common[1] - least_common[1])


if __name__ == '__main__':
    main()
