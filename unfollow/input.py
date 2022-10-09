import requests
from sys import exit
from rich.console import Console


console = Console()

def get_input_username(panels=False, bubbles=False, simple=False):
    if panels or bubbles or simple:
        return
    user = console.input(":label:  [magenta]Please enter your GitHub username: [/magenta]")
    print("")
    if not user_exists(user):
        while not user_exists(user):
            console.print("[red]User invalid![/red]")
            try:
                user = console.input("[magenta]Please enter your GitHub username: [/magenta]")
                print("")
            except KeyboardInterrupt:
                print("\nYou have cancelled the username operation! If you are experiencing a bug, please report it.\n")
                exit(1)
    return user


def user_exists(user):
    url = f"https://api.github.com/users/{user}"
    try:
        r = requests.get(url.format(user)).json()
    except Exception as err:
        print(f"Error occurred while validating your username: {err}")
        exit(1)
    if "message" in r:
        if r["message"] == "Not Found":
            return False
    return True
