import time
import os
from utils.ui import  show_command_list, choose_help_command
from utils.colors import BColor as colors
from core_commands.version import version, links
from utils.animations import type_text, loading_animation
from commands.system import request_command_error, too_many_command_requestes

def cmd_void(parts):
    if len(parts) < 2:
        request_command_error()
        return
    
    arg = parts[1]

    if arg in ("--help", "-h"):
        if len(parts) == 2:
            show_command_list()
        elif len(parts) == 3:
            choose_help_command(parts[2])
        elif len(parts) > 3:
            too_many_command_requestes()
    elif arg in ("--version", "-v"):
        print(f"{colors.helping}BlackHole CLI v{colors.ENDC}{version}")
    else:
        print(f"{colors.Error}[!] >>> Unknown option '{arg}'.{colors.ENDC}")
