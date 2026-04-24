
from core_commands.version import version, links
from assets.banner import title
from utils.ui import  show_command_list, choose_help_command
from utils.colors import BColor as colors
from utils.animations import type_text, loading_animation
import os
# ----- Commands -----
def request_command_error():
    print(f"{colors.Error}[!] >>> Unknown command syntax.{colors.ENDC}")
def too_many_command_requestes():
    print(f"{colors.Error}[!] >>> Too many commands requested.{colors.ENDC}")
def unknown_command():
    print(f"{colors.Error}[!] >>> Unknown command.{colors.ENDC}")

def cmd_clear(parts):
    if parts[0].lower() == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        title()
        print("Welcome Boss!")

def cmd_whoami(parts):
    if len(parts) > 2:
        too_many_command_requestes()
    elif len(parts) == 1:
        username = os.getenv("USERNAME")
        hostname = os.getenv("COMPUTERNAME")
        print(f"[{colors.lightgreen}+{colors.ENDC}]{colors.helping} >>> your: {username}@{hostname}{colors.ENDC}")
        return
    arg = parts[1]

    if arg in ("--hostname", "-hn"):
        hostname = os.getenv("COMPUTERNAME")
        print(f"[{colors.lightgreen}+{colors.ENDC}]{colors.helping} >>> your: {hostname}{colors.ENDC}")
    else: 
        print(f"{colors.Error}[!] >>> Unknown option '{arg}'.{colors.ENDC}")
