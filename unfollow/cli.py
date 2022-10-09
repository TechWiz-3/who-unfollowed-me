#!/usr/bin/env python3

import sys
import argparse
import requests

from rich.panel import Panel
from rich.console import Console

# local file imports
from unfollow.beautify import beautify_unfollows
from unfollow.unfollow import main as unfollow_main
from unfollow.config import get_config

console = Console()

config = get_config()

theme = config['apperance']['styling']['theme']
emojis = config['apperance']['emojis']

locale_lang = config['locale']['locale']

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
help_txt = "[optional]\n'regular':  regular theme (triggers if no other theme\
 arguement is provided)\n'panels':   displays\
 everything in panels\n'bubbles':  displays everything in\
 bubbles (requires a nerd font to be used)\n'regular':  \
default, some panels used\n'simple':   no color"
parser.add_argument('style', nargs='?', help=help_txt)

parser.add_argument('--token', action="store_true",
                    help="Uses an env variable stored as\
 UNFOLLOW_TOKEN which is a github token for requests to the API.")
parser.add_argument('--test', action="store_true", help="for testing purposes")

args = parser.parse_args(sys.argv[1:])

panels = False  # all text in panels
bubbles = False  # nerd fonts only
simple = False  # no colour
regular = True

info = None  # stores the unfollowers

if theme == "panels":
    panels = True
elif theme == "bubbles":
    bubbles = True
elif theme == "simple":
    simple = True  # no colour
elif theme == "regular":
    regular = True  # regular theme

if args.style == "panels":
    theme = "panels"
    panels = True
elif args.style == "bubbles":
    theme = "bubbles"
    bubbles = True
elif args.style == "simple":
    simple = True
elif args.style == "regular":
    theme = "regular"
    regular = True

locale = config['locale'][locale_lang][theme]


def get_inverse(bg_col, txt, txt_before=None):
    circle_style = f"[{bg_col}]"
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
        txt = Panel.fit(locale['fetched_followers_message'])
        sys.stdout.write("\033[F")  # lift the line up
    elif bubbles:
        txt = get_inverse("cyan", locale['fetched_followers_message'], txt_before=":mag:")
        # end = "\r\n"
    elif regular:
        txt = locale['fetched_followers_message']
    console.print(txt)
    return


def no_unfollows():
    from rich.style import Style
    a = Style(color="green")
    if panels:
        txt = Panel.fit(locale['no_unfollows_message'], border_style=a)
        console.print(txt)
    elif bubbles:
        print("")
        txt = get_inverse("green4", locale['no_unfollows_message'])
        console.print(emojis['no_unfollows_emoji'], txt)
        print("")
    elif regular:
        print("")
        txt_a = locale['no_unfollows_message']
        console.print(txt_a)


def end(follower_num=0): # remember TO CHANge THIS
    # for super pretty version
    # console.print("[#026440 on black][/#026440 on black]Yay we all g bruh[#026440 on black]", style="white on #026440")
    if panels:
        txt_b = Panel.fit(locale['end_message'].format(follower_num=follower_num), subtitle=locale['thankyou_message'], subtitle_align="left")
        console.print(txt_b)
        print("\n")
    elif bubbles:
        txt_b = get_inverse("purple", locale['end_message_a'].format(follower_num=follower_num))
        text_c = get_inverse("magenta", locale['end_message_b'])
        console.print(emojis['follow_count_emoji'], txt_b, text_c)
        print("")
        txt = get_inverse("blue", locale['thankyou_message'])
        console.print(emojis['thankyou_emoji'], txt)
        print("")
    elif regular:
        print("")
        txt_b = Panel.fit(locale['end_message'].format(follower_num=follower_num), subtitle=":pray: Thanks for using this project", subtitle_align="left")
        console.print(txt_b)
        print("\n")


def start():
    if panels:
        txt = Panel.fit(locale['welcome_message'])
    elif bubbles:
        print("")
        part_a = get_inverse("purple", str(locale['welcome_message_a']))
        part_b = get_inverse("red", locale['welcome_message_b'])
        part_c = get_inverse("blue", locale['welcome_message_c'])
        part_d = get_inverse("dark_goldenrod", locale['welcome_message_d'])
        txt = f"{emojis['init_emoji']} {part_a} {part_b} {part_c} {part_d}"
    elif regular:
        print("")
        txt = locale['welcome_message']
    console.print(txt)


def check_connectivity():
    url = "http://google.com"
    timeout = 10
    try:
        request = requests.get(url, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("Internet connection invalid, please try again later!")
        Console().print("If you think this is a bug, please make an issue.", style="dim")
        exit(1222)  # microsoft ERROR_NO_NETWORK code coz why not


def main():
    start()
    check_connectivity()
    get_links()

    if info[0] == "first":
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


if __name__ == "__main__":
    main()
