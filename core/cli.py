import os

from utils.colors import BColor as colors
from core.router import command1
from core.parser import parse_input

username = os.getenv("USERNAME")


def start_CLi():
    while True:
        cmd = input(f"{colors.helping}[${username}] >>> {colors.ENDC}")
        parts = parse_input(cmd)
        if not parts:
            continue

        command1(parts)
        