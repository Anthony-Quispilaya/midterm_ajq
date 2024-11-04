def parse_command(user_input):
    tokens = user_input.strip().split()
    if not tokens:
        raise ValueError("No input provided.")
    command_name = tokens[0]
    args = tokens[1:]
    return command_name, args
