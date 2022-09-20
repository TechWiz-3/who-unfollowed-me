from beautify import beautify_unfollows
import threading
import time
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.status import Status

# create a super pretty one with a --nerd-fonts option

panels = True
bubbles = False
simple = False

info = [("rafa", "https://github.com/rafa"), ("cortex", "https://github.com/cortex")]
info = []
console = Console()

def get_links():
    # pretend get links
    time.sleep(3)
    global stop_threads
    stop_threads = True
    tasks = range(10)


def print_get():
    global panels
    global bubbles
    global simple
    if not panels:
        print("")
    spinner = Status("Getting github followers")
    spinner.start()
    while True:
        if stop_threads:
            spinner.stop()
            if panels:
                txt = Panel.fit("[green]✔ [underline]Fetched github followers")
            elif not panels:
                print("")
                txt = "[green]✔ [underline]Fetched github followers"
            console.print(txt)
            return


def no_unfollows():
    # for super pretty version
    # console.print("[#026440 on black][/#026440 on black]Yay we all g bruh[#026440 on black]", style="white on #026440")
    from rich.style import Style
    a = Style(color="green")
    if panels:
        txt_a = Panel.fit("[white on #308012] No unfollows! [/white on #308012]                                ",
                          border_style=a
                         )
        console.print(txt_a)
        txt_b = Panel.fit(":fire: You have 80 followers. Keep up the good work\
\n", subtitle=":pray: Thanks for using this project", subtitle_align="left")
        console.print(txt_b)
        print("\n")
    elif not panels:
        print("")
        txt_a = ":raised_hands: [white on #308012]No unfollows![/white on #308012]                                "
        console.print(txt_a)
        print("")
        txt_b = Panel.fit(":fire: You have 80 followers. Keep up the good work\
\n", subtitle=":pray: Thanks for using this project", subtitle_align="left")
        console.print(txt_b)
        print("\n")



def start():
    if panels:
        txt = Panel.fit(
            ":dancer: [purple]Welcome to [/purple] [red]who-unfollowed-me[/red][blue] python implementation[/blue] by [#FFD700]Zac the Wise[#FFD700]"
        )
    elif not panels:
        print("")
        txt = ":dancer: [purple]Welcome to [/purple] [red]who-unfollowed-me[/red][blue] python implementation[/blue] by [#FFD700]Zac the Wise[#FFD700]"
    console.print(txt)


if __name__ == "__main__":
    start()
    stop_threads = False
    t1 = threading.Thread(target=get_links)
    t2 = threading.Thread(target=print_get)
    t1.start()
    t2.start()
    while True:
        if stop_threads:
            time.sleep(1)  # give time for the functions to exit
            if info:
                beautify_unfollows(info)
            else:
                no_unfollows()
            break
