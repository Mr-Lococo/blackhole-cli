import os
import random
import platform
import time
from utils.colors import BColor as colors
from utils.animations import loading_animation
from commands.system import request_command_error, unknown_command, too_many_command_requestes

def cmd_cd(parts):
    if len(parts) < 2:
        request_command_error()
    elif len(parts) > 2:
        too_many_command_requestes()
    if len(parts) == 2:
        path = parts[1]
        try:
            os.chdir(path)
            print(f"{colors.helping}[+] >>> directory: {os.getcwd()}{colors.ENDC}")
        except FileNotFoundError:
            print(f"{colors.Error}[!] >>> Directory '{path}' not found.{colors.ENDC}")
        except NotADirectoryError:
            print(f"{colors.Error}[!] >>> '{path}' is not a directory.{colors.ENDC}")
        except PermissionError:
            print(f"{colors.Error}[!] >>> Permission denied for '{path}'.{colors.ENDC}")
        except Exception as e:
            print(f"{colors.Error}[!] >>> An error occurred: {str(e)}{colors.ENDC}")
            return
    
def cmd_secure(parts):
    if len(parts) < 2:
        request_command_error()
        return
    elif len(parts) > 3:
        too_many_command_requestes()
        return
        
    arg = parts[1]

    if arg in ("--remove", "-rm"):
        if len(parts) < 3:
            request_command_error()
            return
        target = parts[2]
        ask = input(f"{colors.WARNING}[?] >>> Are you sure you want to securely delete '{target}'? (y/n): {colors.ENDC}") #ask the user for confirmation before deleting the file
        if ask.lower() == "y" or ask.lower() == "yes":
            if os.path.isfile(target):
                print(f"{colors.helping}-[*] >>> Getting user's OS information...{colors.ENDC}")
                User_os = platform.system()
                if User_os == "Windows":
                    try:
                        with open(target, "ba+") as f:
                            length = f.tell()
                            print(f"{colors.helping}-[*] >>> Using 'TWO'...{colors.ENDC}")
                            f.seek(0)
                            time.sleep(0.5)
                            f.write(os.urandom(length))
                            time.sleep(0.5)
                            f.write(os.urandom(length))
                            time.sleep(0.5)
                            f.write(os.urandom(length))
                        os.remove(target)
                        print(f"{colors.lightgreen}[+] >>> '{target}' has been securely deleted.{colors.ENDC}")
                    except Exception as e:
                        print(f"{colors.Error}[!] >>> An error occurred: {str(e)}{colors.ENDC}")
            else:
                print(f"{colors.Error}[!] >>> '{target}' is not a file.{colors.ENDC}") #if the target is not a file, print an error message
        elif ask.lower() == "n" or ask.lower() == "no":
            print(f"{colors.helping}[+] >>> Operation cancelled.{colors.ENDC}") #if the user cancels the operation, print a cancellation message
                    
def cmd_ls(parts):
    if len(parts) > 2:
        too_many_command_requestes()
    elif len(parts) == 1:
        try:
            files = os.listdir()

            sorted_files = sorted(files, key=lambda x: (not os.path.isdir(x), x.lower()))

            for file in sorted_files:
                if os.path.isdir(file):
                    print(f"[Folder] - {file}")
                elif os.path.isfile(file):
                    print(f"[File] - {file}")
        except PermissionError:
            print(f"{colors.Error}[!] >>> Permission denied for the current directory.{colors.ENDC}")
    elif len(parts) == 2:

        arg = parts[1]

        if arg in ("--files", "-f"):
            try:
                files = os.listdir()
                for file in files:
                    if os.path.isfile(file):
                        print(f"[File] - {file}")
            except PermissionError:
                print(f"{colors.Error}[!] >>> Permission denied for the current directory.{colors.ENDC}")
        elif arg in ("--directories", "-d"):
            try:
                files = os.listdir()
                for files in files:
                    if os.path.isdir(files):
                        print(f"[Folder] - {files}")
            except PermissionError:
                print(f"{colors.Error}[!] >>> Permission denied for the current directory.{colors.ENDC}")
        else:
            print(f"{colors.Error}[!] >>> Unknown option '{parts[1]}'.{colors.ENDC}")