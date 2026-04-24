def parse_input(cmd: str):
    if not cmd.strip():
        return []
    return cmd.strip().split()