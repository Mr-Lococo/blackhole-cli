from core_commands.help import cmd_void
from commands.system import cmd_clear, cmd_whoami
from commands.files import cmd_cd, cmd_ls
# ----- list -----------

commands = {
    "clear": cmd_clear,
    "void": cmd_void,
    "whoami": cmd_whoami,
    "cd": cmd_cd,
    "ls": cmd_ls
}
