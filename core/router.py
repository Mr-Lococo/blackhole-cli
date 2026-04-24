from core.registery import commands
from commands.system import request_command_error, too_many_command_requestes, unknown_command


# ----- cmds -----------
def command1(parts):
    cmd = parts[0].lower()

    if cmd in commands:
        commands[cmd](parts)
    else:
        unknown_command()
