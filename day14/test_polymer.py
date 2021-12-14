import collections
import unittest

from day14.polymer import read_input, parse_pair, find_index, insert_pair, find_matching_rules, parse_all_pairs, \
    apply_rules


class PolymerTestCase(unittest.TestCase):
    def test_polymer_input(self):
        polymer_template, pair_insertions = read_input("test_input")
        self.assertEqual("NNCB", polymer_template)
        self.assertEqual(16, len(pair_insertions))
        self.assertEqual("CH -> B", pair_insertions[0])

    def test_parse_pair_insertion(self):
        self.assertEqual(("CH", "B"), parse_pair("CH -> B"))
        self.assertEqual(("HH", "N"), parse_pair("HH -> N"))

    def test_find_index_of_insertion(self):
        index = find_index(parse_pair("NN -> C"), "NNCB")
        self.assertEqual(1, index)

        index2 = find_index(parse_pair("NN -> C"), "CBNN")
        self.assertEqual(3, index2)

    def test_single_insertion(self):
        template = "NNCB"
        pair = parse_pair("NN -> C")

        rules = find_matching_rules(template, [pair])

        result = insert_pair(rules[0], template)

        self.assertEqual("NCNCB", result)

    def test_multiple_insertions(self):
        pass

    # polymer_template, pair_insertions = read_input("test_input")
    # pairs = parse_all_pairs(pair_insertions)
    #
    # rules = find_matching_rules(polymer_template, pairs)
    #
    # result = insert_pair(rules[0], polymer_template)
    # result = insert_pair(rules[1], result)
    # self.assertEqual("NCNBCHB", result)

    def test_match_rule(self):
        polymer_template, pair_insertions = read_input("test_input")

        pairs = parse_all_pairs(pair_insertions)

        self.assertEqual([(1, "C"), (2, "B"), (3, "H")],
                         find_matching_rules(polymer_template, pairs))

    def test_find_match_and_apply_step_one(self):
        polymer_template, pair_insertions = read_input("test_input")
        pairs = parse_all_pairs(pair_insertions)
        matching_rules = find_matching_rules(polymer_template, pairs)
        polymer_template = apply_rules(matching_rules, polymer_template)

        self.assertEqual("NCNBCHB", polymer_template)

    def test_find_match_and_apply_step_two(self):
        polymer_template, pair_insertions = read_input("test_input")
        pairs = parse_all_pairs(pair_insertions)

        for i in range(2):
            matching_rules = find_matching_rules(polymer_template, pairs)
            polymer_template = apply_rules(matching_rules, polymer_template)

        self.assertEqual("NBCCNBBBCBHCB", polymer_template)

    def test_find_match_and_apply_step_three(self):
        polymer_template, pair_insertions = read_input("test_input")
        pairs = parse_all_pairs(pair_insertions)

        for i in range(3):
            matching_rules = find_matching_rules(polymer_template, pairs)
            polymer_template = apply_rules(matching_rules, polymer_template)

        self.assertEqual("NBBBCNCCNBBNBNBBCHBHHBCHB", polymer_template)

    def test_ten_steps(self):
        polymer_template, pair_insertions = read_input("test_input")
        pairs = parse_all_pairs(pair_insertions)

        for i in range(10):
            matching_rules = find_matching_rules(polymer_template, pairs)
            polymer_template = apply_rules(matching_rules, polymer_template)
        common_sorted = collections.Counter(polymer_template).most_common()
        most_common = collections.Counter(polymer_template).most_common(1)[0]
        least_common = common_sorted[len(common_sorted) - 1]
        self.assertEqual(1588, most_common[1] - least_common[1])

    def test_ten_step_real_data(self):
        polymer_template, pair_insertions = read_input("input")
        pairs = parse_all_pairs(pair_insertions)

        for i in range(10):
            matching_rules = find_matching_rules(polymer_template, pairs)
            polymer_template = apply_rules(matching_rules, polymer_template)

        common_sorted = collections.Counter(polymer_template).most_common()
        most_common = collections.Counter(polymer_template).most_common(1)[0]
        least_common = common_sorted[len(common_sorted) - 1]
        print(most_common, least_common)
        print(most_common[1] - least_common[1])

    # def test_40_step_real_data(self):
    #     polymer_template, pair_insertions = read_input("input")
    #     pairs = parse_all_pairs(pair_insertions)
    #
    #     for i in range(40):
    #         print("step: " + str(i))
    #         matching_rules = find_matching_rules(polymer_template, pairs)
    #         polymer_template = apply_rules(matching_rules, polymer_template)
    #
    #     common_sorted = collections.Counter(polymer_template).most_common()
    #     most_common = collections.Counter(polymer_template).most_common(1)[0]
    #     least_common = common_sorted[len(common_sorted) - 1]
    #     print(most_common, least_common)
    #     print(most_common[1] - least_common[1])


if __name__ == '__main__':
    unittest.main()
