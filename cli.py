#!/usr/bin/evn python3

from beautify import beautify_unfollows
import threading
import time
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.status import Status
import sys
import argparse
from unfollow import main as unfollow_main

# create a super pretty one with a --nerd-fonts option

parser = argparse.ArgumentParser()
parser.add_argument('style', nargs='?')

args = parser.parse_args(sys.argv[1:])

panels = False
bubbles = False
simple = False  # no colour


if args.style == "panels":
    panels = True
elif args.style == "bubbles":
    bubbles = True
elif args.style == "simple":
    simple = True  # no colour


#info = [("rafa", "https://github.com/rafa"), ("cortex", "https://github.com/cortex")]
#info = []
info = unfollow_main()
console = Console()

def get_inverse(bg_col, txt):
    circle_style=f"[{bg_col}]"
    circle_close = circle_style[:1] + "/" + circle_style[1:]
    bubble = f"{circle_style}{circle_close}{txt}{circle_style}{circle_close}"
    return bubble

def get_links():
    # pretend get links
    time.sleep(1)
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
            elif bubbles:
                txt = get_inverse("cyan", "[white on cyan]Fetched github\
 followers[/white on cyan]")
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
    elif bubbles:
        print("")
        txt_a = get_inverse("green4", "[white on green4]No \
unfollows![/white on green4]"
               )
        console.print(":thumbs_up:", txt_a)
        print("")
        txt_b = get_inverse("purple", "[white on purple]You have 80 followers.[/white on purple]")
        text_c = get_inverse("magenta", "[white on magenta]Keep up the good\
 work![/white on magenta]")
        console.print(":fire:", txt_b, text_c)
        print("")
        txt = get_inverse("blue", "[white on blue]Thanks for using this project[/white on blue]")
        console.print(":pray:", txt)
        print("")
    elif not panels:
        print("")
        txt_a = "[green]:raised_hands: [underline]No unfollows!"
        console.print(txt_a)
        print("")
        txt_b = Panel.fit(":fire: You have 80 followers. Keep up the good work\
\n", subtitle=":pray: Thanks for using this project", subtitle_align="left")
        console.print(txt_b)
        print("\n")



def start():
    if panels:
        txt = Panel.fit(
            ":dancer: [purple]Welcome to[/purple] [red]who-unfollowed-me[/red][blue] python implementation[/blue] by [#FFD700]Zac the Wise[#FFD700]"
        )
    elif bubbles:
        print("")
        part_a = get_inverse("purple", "[white on purple]Welcome to[/white on purple]")
        part_b = get_inverse("red", "[white on red]who-unfollowed-me[/white on red]")
        part_c = get_inverse("blue", "[white on blue]the Python implementation[/white on blue]")
        part_d = get_inverse("dark_goldenrod", "[white on dark_goldenrod]by Zac\
 the Wise[/white on dark_goldenrod]")
        txt = f":dancer: {part_a} {part_b} {part_c} {part_d}"
        #txt = get_inverse("purple", "[on purple]:dancer: [purple]Welcome to[/purple] [red]who-unfollowed-me[/red][blue] python implementation[/blue] by [#FFD700]Zac the Wise[#FFD700]"
#)
    elif not panels:
        print("")
        txt = ":dancer: [purple]Welcome to[/purple] [red]who-unfollowed-me[/red][blue] python implementation[/blue] by [#FFD700]Zac the Wise[#FFD700]"
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
