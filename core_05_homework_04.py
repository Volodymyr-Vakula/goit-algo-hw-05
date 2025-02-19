from typing import Callable
from functools import wraps
from random import choice
from colorama import Fore

# A decorator to handle input errors
def input_error(func: Callable):
    """
    Handles 3 types of input errors: ValueError, IndexError, and KeyError

    Parameters:
        func (callable): a function processing user input
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"{Fore.RED}\nGive me name and phone please."
        except IndexError:
            return f"{Fore.RED}\nEnter argument for the command please."
        except KeyError:
            return f"{Fore.RED}\nContact doesn't exist"
    return inner

# Function to parse user's input
def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Extracts data from user's input

    Parameters:
        user input (str): user's input as a single string
    
    Returns:
        tuple[str, list[str]]: a tuple with command as first element and list of arguments
            as second element
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Function to add contact
@input_error
def add_contact(args: list[str], contacts: dict[str: str]) -> str:
    """
    Creates a new contact (or overwrites an existing one)

    Parameters:
        args (list[str]): new contact data (name, phone)
        contacts (dict[str: str]): existing contacts
    
    Returns:
        str: formatted string with notification
    """
    name, phone = args
    contacts[name] = phone
    return f"{Fore.GREEN}\nContact added/updated: {Fore.WHITE}{name} {phone}"

# Function to change contact
@input_error
def change_contact(args: list[str], contacts: dict[str: str]) -> str:
    """
    Changes phone number of an existing contact

    Parameters:
        args (list[str]): new contact data (name, phone)
        contacts (dict[str: str]): existing contacts
    
    Returns:
        str: formatted string with notification
    """
    name, phone = args
    contacts[name] = phone
    return f"{Fore.GREEN}\nPhone changed: {Fore.WHITE}{name} {phone}"

# Function to show contact
@input_error
def show_phone(args: list[str], contacts: dict[str: str]) -> str:
    """
    Shows phone number of a contact

    Parameters:
        args (list[str]): contact data (name)
        contacts (dict[str]): existing contacts
    
    Returns:
        str: formatted string with notification
    """
    name = args[0]
    return f"{Fore.GREEN}\n{name}: {contacts[name]}"

# Function to show all contacts
def show_all_contacts(contacts: dict[str: str]) -> str:
    """
    Shows all contacts

    Parameters:
        contacts (dict[str]): existing contacts
    
    Returns:
        str: formatted string with information/notification
    """
    if len(contacts) == 0:
        return Fore.GREEN + "\nThere are no contacts yet"
    all_contacts = ""
    for name, phone in contacts.items():
        all_contacts += f"\n{Fore.GREEN}{name}: {phone}"
    return all_contacts

# Main function
def main():
    """
    Handles phone bot operations
    """
    colours = (Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE)
    bot_banner = f"""{choice(colours)}\
 ██▓███   ██░ ██  ▒█████   ███▄    █ ▓█████     ▄▄▄▄    ▒█████  ▄▄▄█████▓
▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀    ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███      ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄    ▒██░ █▀  ▒██   ██░░ ▓██▓ ░ 
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░   ▒░▒   ░   ░ ▒ ▒░     ░    
░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░       ░    ░ ░ ░ ░ ▒    ░      
          ░  ░  ░    ░ ░           ░    ░  ░    ░          ░ ░           
                                                     ░                   """
    print(bot_banner + "\n")
    print(Fore.GREEN + "Welcome to the assistant bot!".upper())
    command_list = f"""
    {Fore.BLUE + "List of available commands".upper()}:

    {Fore.WHITE}hello {Fore.BLUE}- say hello to the bot
    {Fore.WHITE}help {Fore.BLUE}- show list of commands
    {Fore.WHITE}add <username> <phone> {Fore.BLUE}- add a new contact
    {Fore.WHITE}change <username> <phone> {Fore.BLUE}- change phone number
    {Fore.WHITE}phone <username> {Fore.BLUE}- show phone number
    {Fore.WHITE}all {Fore.BLUE}- show all contacts
    {Fore.WHITE}exit {Fore.BLUE}- exit the bot
    {Fore.WHITE}close {Fore.BLUE}- exit the bot
    """
    print(command_list, end="")
    contacts = {}
    while True:
        user_input = input(Fore.YELLOW + "\nEnter a command: " + Fore.WHITE)
        command, *args = parse_input(user_input)
        # 'Exit' or 'close' commands
        if command in ("exit", "close"):
            print(Fore.GREEN + "\nGoodbye!".upper())
            break
        # 'Hello' command
        if command == "hello":
            print(Fore.WHITE + "\nHow can I help you?")
        # 'Help' command
        elif command == "help":
            print(command_list, end="")
        # 'Add' command
        elif command == "add":
            print(add_contact(args, contacts))
        # 'Change' command
        elif command == "change":
            print(change_contact(args, contacts))
        # 'Phone' command
        elif command == "phone":
            print(show_phone(args, contacts))
        # 'All' command
        elif command == "all":
            print(show_all_contacts(contacts))
        # Command absent from command list
        else:
            print(Fore.RED + "\nInvalid command")
    print(Fore.RESET, end="")

if __name__ == "__main__":
    main()
