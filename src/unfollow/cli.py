#!/usr/bin/evn python3

import sys
import time
import argparse
import requests
import concurrent.futures

from rich.rule import Rule
from rich.panel import Panel
from rich.status import Status
from rich.console import Console

# local file imports
from unfollow.beautify import beautify_unfollows
from unfollow.unfollow import main as unfollow_main

console = Console()

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
help_txt = "[optional]\n'panels':   displays\
 everything in panels\n'bubbles':  displays everything in\
 bubbles (requires a nerd font to be used)\n'regular':  \
default, some panels used\n'simple':   no color, coming\
 soon"
parser.add_argument('style', nargs='?', help=help_txt)

parser.add_argument('--token', action="store_true",
                    help="Uses an env variable stored as\
 UNFOLLOW_TOKEN which is a github token for requests to the API."
               )
parser.add_argument('--test', action="store_true", help="for testing purposes")

args = parser.parse_args(sys.argv[1:])

panels = False
bubbles = False  # nerd fonts only
simple = False  # no colour

info = None  # stores the unfollowers

if args.style == "panels":
    panels = True
elif args.style == "bubbles":
    bubbles = True
elif args.style == "simple":
    simple = True  # no colour


def get_inverse(bg_col, txt, txt_before=None):
    circle_style=f"[{bg_col}]"
    circle_close = circle_style[:1] + "/" + circle_style[1:]
    if txt_before:
        bubble = f"{txt_before} {circle_style}{circle_close}{txt}{circle_style}{circle_close}"
    else:
        bubble = f"{circle_style}{circle_close}{txt}{circle_style}{circle_close}"
    return bubble


def get_links():
    """get unfollows"""
    global info
    info = unfollow_main()
    print_get()


def print_get():
    global panels
    global bubbles
    global simple
    if panels:
        txt = Panel.fit("[green]✔ [underline]Fetched github followers")
        sys.stdout.write("\033[F")  # lift the line up
    elif bubbles:
        txt = get_inverse("cyan", "[white on cyan]Fetched github \
followers[/white on cyan]", txt_before=":mag:")
        #end = "\r\n"
    elif not panels:
        txt = "[green]✔ [underline]Fetched github followers"
    console.print(txt)
    return


def no_unfollows():
    from rich.style import Style
    a = Style(color="green")
    if panels:
        txt = Panel.fit("[white on #308012] No unfollows! [/white on #308012]                                ",
                          border_style=a
                        )
        console.print(txt)
    elif bubbles:
        print("")
        txt = get_inverse("green4", "[white on green4]No \
unfollows![/white on green4]"
               )
        console.print(":thumbs_up:", txt)
        print("")
    elif not panels:
        print("")
        txt_a = "[green]:raised_hands: [underline]No unfollows!"
        console.print(txt_a)


def end(follower_num=0): ## remember TO CHANge THIS
    # for super pretty version
    # console.print("[#026440 on black][/#026440 on black]Yay we all g bruh[#026440 on black]", style="white on #026440")
    if panels:
        txt_b = Panel.fit(f":fire: You have {follower_num} followers. Keep up the good work\
\n", subtitle=":pray: Thanks for using this project", subtitle_align="left")
        console.print(txt_b)
        print("\n")
    elif bubbles:
        txt_b = get_inverse("purple", f"[white on purple]You have {follower_num} followers.[/white on purple]")
        text_c = get_inverse("magenta", "[white on magenta]Keep up the good\
 work![/white on magenta]")
        console.print(":fire:", txt_b, text_c)
        print("")
        txt = get_inverse("blue", "[white on blue]Thanks for using this project[/white on blue]")
        console.print(":pray:", txt)
        print("")
    elif not panels:
        print("")
        txt_b = Panel.fit(f":fire: You have {follower_num} followers. Keep up the good work\
\n", subtitle=":pray: Thanks for using this project", subtitle_align="left")
        console.print(txt_b)
        print("\n")


def start():
    if panels:
        txt = Panel.fit(
            ":dancer: [purple]Welcome to[/purple] [red]who-unfollowed-me[/red][blue] Python implementation[/blue] by [#FFD700]Zac the Wise[#FFD700]"
        )
    elif bubbles:
        print("")
        part_a = get_inverse("purple", "[white on purple]Welcome to[/white on purple]")
        part_b = get_inverse("red", "[white on red]who-unfollowed-me[/white on red]")
        part_c = get_inverse("blue", "[white on blue]the Python implementation[/white on blue]")
        part_d = get_inverse("dark_goldenrod", "[white on dark_goldenrod]by Zac\
 the Wise[/white on dark_goldenrod]")
        txt = f":dancer: {part_a} {part_b} {part_c} {part_d}"
    elif not panels:
        print("")
        txt = ":dancer: [purple]Welcome to[/purple] [red]who-unfollowed-me[/red][blue] Python implementation[/blue] by [#FFD700]Zac the Wise[#FFD700]"
    console.print(txt)


def check_connectivity():
    url = "http://google.com"
    timeout = 10
    try:
        request = requests.get(url, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("Internet connection invalid, please try again later!")
        Console().print("If you think this is a bug, please make an issue.",
                      style="dim")
        exit(1222)  # microsoft ERROR_NO_NETWORK code coz why not


def main():
    start()
    check_connectivity()
    get_links()

    if info[0]  == "first":
        # follows saved for later
        end(follower_num=info[1])
    elif info[0] == "regular":
        if len(info) == 3:  # unfollowers have been detected
            if bubbles:
                beautify_unfollows(info[2], special="bubbles")
            elif panels:
                beautify_unfollows(info[2], special="panels")
            else:
                beautify_unfollows(info[2])
        else:
            no_unfollows()
        end(follower_num=info[1])

