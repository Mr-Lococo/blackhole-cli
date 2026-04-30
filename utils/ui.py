from utils.colors import BColor as colors 
    
BANNER = "BlackHole CLI v0.1.0-beta1"

def print_header(command: str):
    print(f"""{BANNER}

{colors.helping}Usage:{colors.ENDC}
  {command}
""")

def show_help_void():
    print_header("void [options]")
    print("""Options:
  --help [command], -h [command]   Show command usage
  --help, -h                      Show command list
  --version, -v                   Show tool version
""")

def show_help_ls():
    print_header("ls [options]")
    print("""Options:
  --directory, -d   Show only directories
  --files, -f       Show only files
""")

def show_help_whoami():
    print_header("whoami [options]")
    print("""Options:
  --hostname, -hn   Show only the hostname
""")

def show_help_secure():
    print_header("secure [options]")
    print("""Options:
  --remove, -rm <target>   Securely delete a file
""")

def show_command_list():
    print("""Available commands:

  void     CLI main menu
  cd       Change the current directory
  clear    Clear the terminal screen
  ls       List directory contents
  secure   File security tools
  net      Network tools
  whoami   Show username and hostname
""")
    
def choose_help_command(command):
    if command == "void":
        show_help_void()
    elif command == "whoami":
        show_help_whoami()
    elif command == "ls":
        show_help_ls()
    elif command == "secure":
        show_help_secure()
    else:
        print(f"{colors.Error}>>> [!] No help available for '{command}'.{colors.ENDC}")