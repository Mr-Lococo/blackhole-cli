from core.cli import start_CLi
from assets.banner import title

if __name__ == "__main__":
    title()
    print("Welcome Boss!\n    Type 'void --help' to see the command list.")
    start_CLi()