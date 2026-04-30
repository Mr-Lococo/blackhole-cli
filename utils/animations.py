from utils.colors import BColor as colors
import time
import random
import sys
import os


def type_text(text, speed=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()  # Move to the next line after printing the text
#-----------------------------------------
def loading_animation(text2, text):
    for i in range(0, 101, 2):
        Prefix = "[+]" if i == 100 else "[*]"
        sys.stdout.write(f"\r{Prefix} {text2} {text} ... {i}%")
        sys.stdout.flush()
        time.sleep(0.01)
    print(f"\n[{colors.lightgreen} OK {colors.ENDC}] {text2} {text} ... Done" )  # Move to the next line after the animation is complete
#----------------------------------------

# Main function
loading_animation("starting", "BlackHole")
time.sleep(0.01)
loading_animation("requesting", "user-licente")
time.sleep(0.01)
loading_animation("extracting", "user-licente")
time.sleep(0.01)
loading_animation("extracting", "terminal-commands")
time.sleep(0.01)
loading_animation("reading", "user-licente")
time.sleep(0.01)
loading_animation("reading", "terminal-commands")
time.sleep(0.01)
loading_animation("requesting", "tools")
time.sleep(0.01)
loading_animation("requesting", "admin-access")
type_text(f"{colors.purple}Welcome Master.{colors.ENDC}")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')