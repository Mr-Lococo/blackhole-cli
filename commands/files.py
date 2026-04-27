import os
from utils.colors import BColor as colors
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