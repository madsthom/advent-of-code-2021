def int_input_from_file(file_name: str) -> [int]:
    with open(file_name) as f:
        return [int(line) for line in f]


def raw_input_from_file(file_name):
    with open(file_name) as f:
        return str(f.read())
