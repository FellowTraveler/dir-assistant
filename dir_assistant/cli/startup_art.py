import sys

from colorama import Fore, Style


def display_startup_art(commit_to_git):
    sys.stdout.write(
        f"""{Style.BRIGHT}{Fore.GREEN}
  _____ _____ _____                                              
 |  __ \_   _|  __ \                                             
 | |  | || | | |__) |                                            
 | |  | || | |  _  /                                             
 | |__| || |_| | \ \                                             
 |_____/_____|_|_ \_\__ _____  _____ _______       _   _ _______ 
     /\    / ____/ ____|_   _|/ ____|__   __|/\   | \ | |__   __|
    /  \  | (___| (___   | | | (___    | |  /  \  |  \| |  | |   
   / /\ \  \___ \\\___ \  | |  \___ \   | | / /\ \ | . ` |  | |   
  / ____ \ ____) |___) |_| |_ ____) |  | |/ ____ \| |\  |  | |   
 /_/    \_\_____/_____/|_____|_____/   |_/_/    \_\_| \_|  |_|   
{Style.RESET_ALL}\n\n"""
    )
    sys.stdout.write(
        f"{Style.BRIGHT}{Fore.BLUE}Type 'exit' to quit the conversation.\n"
    )
    if commit_to_git:
        sys.stdout.write(
            f"{Style.BRIGHT}{Fore.BLUE}Type 'undo' to roll back the last commit.\n"
        )
    sys.stdout.write("\n")