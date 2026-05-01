from core_commands.void import cmd_void
from commands.system import cmd_clear, cmd_whoami, cmd_Exit
from commands.files import cmd_cd, cmd_ls, cmd_pwd
# ----- list -----------

commands = {
    "clear": cmd_clear,
    "void": cmd_void,
    "whoami": cmd_whoami, #make a linux version
    "cd": cmd_cd,
    "exit": cmd_Exit,
    "pwd": cmd_pwd,
    "ls": cmd_ls
}
