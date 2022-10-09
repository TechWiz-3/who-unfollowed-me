from rich.console import Console
from rich.table import Table
from rich import box
from rich.style import Style

console = Console()
blue = Style(color="blue")
red = Style(color="red", bold=True)
bright_red = Style(color="bright_red")


def get_inverse(bg_col, txt):
    circle_style = f"[{bg_col}]"
    circle_close = f"{circle_style[:1]}/{circle_style[1:]}"
    return f"{circle_style}{circle_close}{txt}{circle_style}{circle_close}"


def beautify_unfollows(info, special=False):
    if special == "bubbles":
        table = Table(box=box.SQUARE, show_lines=False, show_edge=False,)
#                      padding=(0,2,0,2))
        txt_a = get_inverse("red", "[white on red]Name[/white on red]")
        txt_b = get_inverse("red", "[white on red]Link[/white on red]")
        print("")  # get some spacing before the table
    else:
        if special != "panels":  # for the vanilla type
            print("")  # add an extra line
        table = Table(box=box.SQUARE, show_lines=True)
        txt_a = "Name"
        txt_b = "Link"

    table.add_column(txt_a, header_style=red, justify="left", style=bright_red, no_wrap=True)
    table.add_column(txt_b, header_style=red, style=bright_red)

    for name, link in info:
        if special == "bubbles":
            name = get_inverse("bright_red", f"[white on bright_red]{name}[/white on bright_red]")
            link = get_inverse("bright_red", f"[white on bright_red]{link}[/white on bright_red]")
        table.add_row(name, link)

    console.print(table)
    if special == "bubbles":
        print("")
