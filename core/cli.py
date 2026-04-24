import os

from utils.colors import BColor as colors
from core.router import command1
from core.parser import parse_input

username = os.getenv("USERNAME")


def start_CLi():
    while True:
<<<<<<< HEAD
        cmd = input(f"{colors.helping}[{username}] >>> {colors.ENDC}")
=======
        cmd = input(f"{colors.helping}[${username}] >>> {colors.ENDC}")
>>>>>>> aba55f085592846928560db57b810dc7b00cd065
        parts = parse_input(cmd)
        if not parts:
            continue

        command1(parts)
        