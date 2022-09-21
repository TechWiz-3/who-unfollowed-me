from rich.console import Console
from rich.table import Table
from rich import box

console = Console()


def beautify_unfollows(info):
    table = Table(box=box.SQUARE, show_lines=True)

    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Link", style="magenta")

    for name, link in info:
        table.add_row(name, link)

    console.print(table)
