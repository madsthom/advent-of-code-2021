def parse_commands(commands: str) -> dict:
    command_array = commands.split("\n")
    command_dict = {"forward": 0, "down": 0, "up": 0, "aim": 0}
    for command in command_array:
        parse_single_command(command, command_dict)
    return command_dict


def parse_single_command(command, command_dict):
    if command == "":
        return
    number = get_number(command)
    if "forward" in command:
        update_command("down", command_dict["aim"] * number, command_dict)
        update_command("forward", number, command_dict)
    if "down" in command:
        update_command("aim", number, command_dict)
    if "up" in command:
        update_command("aim", -number, command_dict)


def update_command(command_type, number, command_dict):
    command_dict[command_type] = command_dict[command_type] + number


def get_number(command):
    return [int(s) for s in command.split() if s.isdigit()][0]


def calculate_position(commands):
    return commands["forward"], commands["down"] - commands["up"]
