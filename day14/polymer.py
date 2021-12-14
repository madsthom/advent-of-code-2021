from helpers.file_handling import raw_input_from_file


def read_input(file_name):
    raw = raw_input_from_file(file_name)
    lines = list(filter(lambda x: x != "", raw.splitlines()))
    polymer_template = lines[0]
    pair_insertions = lines[1:]
    return polymer_template, pair_insertions


def parse_pair(pair_insertion_text):
    return pair_insertion_text[0:2], pair_insertion_text[6:]


def parse_all_pairs(pair_insertions):
    return [parse_pair(pair) for pair in pair_insertions]


def insert_pair(rule, template: str):
    if rule[0]:
        template = template[:rule[0]] + rule[1] + template[rule[0]:]
    return template


def find_index(pair, template):
    for i in range(len(template) - 1):
        if template[i] + template[i + 1] == pair[0]:
            return i + 1


def find_matching_rules(polymer_template, pairs):
    rules = []
    for i in range(len(polymer_template) + 1):
        if len(polymer_template[i:i + 2]) != 1:
            matching_rules = [pair for pair in pairs if pair[0] == polymer_template[i:i + 2]]
            for rule in matching_rules:
                rules.append((i + 1, rule[1]))

    return rules


def apply_rules(matching_rules, polymer_template):
    count = 0
    for rule in matching_rules:
        polymer_template = insert_pair((rule[0] + count, rule[1]), polymer_template)
        count = count + 1
    return polymer_template
