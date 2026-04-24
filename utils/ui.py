from utils.colors import BColor as colors 
    
def show_help_Void():
    print(f"""BlackHole CLI v0.1.0-beta1          
{colors.helping}Usage:
    void [options]{colors.ENDC}

options:
    --help [command] // -h [command]    Show the command's prefix and usage
    --help // -h                        Show the comand list
    --version // -v                     Show the version of the tool""")

def show_help_ls():
    print(f"""BlackHole CLI v0.1.0-beta1
{colors.helping}Usage:
    ls [options]{colors.ENDC}

options:
    --diractory // -d                  Show only the directories
    --files // -f                      Show only the files""")

def show_help_whoami():
    print(f"""BlackHole CLI v0.1.0-beta1
          
{colors.helping}Usage:
    whoami [options]{colors.ENDC}

options:
    --hostname // -hn                   Show only the hostname""")

def show_help_secure():
    print(f"""BlackHole CLI v0.1.0-beta1
          
{colors.helping}Usage:
    secure [options]{colors.ENDC}

options:
    --remove // -rm [target]             Securely delete a file""")

def show_command_list():
    print("""Available commands:
          cd          Change the current directory
          clear       Clear the terminal screen
          ls          List the contents of the current directory
          secure      file secure menu
          whoami      Display the current username and hostname""")
    
def choose_help_command(command):
    if command == "void":
        show_help_Void()
    elif command == "whoami":
        show_help_whoami()
    elif command == "ls":
        show_help_ls()
    elif command == "secure":
        show_help_secure()
    else:
        print(f"{colors.Error}>>> [!] No help available for '{command}'.{colors.ENDC}")