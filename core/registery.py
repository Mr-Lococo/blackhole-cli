from core_commands.void import cmd_void
from commands.network import cmd_network
from commands.system import cmd_clear, cmd_whoami
from commands.files import cmd_cd, cmd_ls
# ----- list -----------

commands = {
    "clear": cmd_clear,
    "void": cmd_void,
    "whoami": cmd_whoami, #make a linux version
    "cd": cmd_cd,
    "network": cmd_network,
    "ls": cmd_ls
}
