from rich import print
#print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())


from rich.console import Console
console = Console()
console.print("Hello", "World!", style="bold red")
console.print("Hello", style="5")
console.print("Hello", style="#af00ff")
console.print("Hello", style="rgb(175,0,255)")
console.print("DANGER!", style="red on white")
console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")
console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
console.print(locals())
console.print("FOO", style="white on blue")
console.print("Google", style="link https://google.com")
console.log("Hello, World!")
console.input("What is [i]your[/i] [bold red]name[/]? :smiley: ")
from rich.panel import Panel
print(Panel("Hello, [red]World!"))

from rich.theme import Theme
custom_theme = Theme({
    "info" : "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})
console = Console(theme=custom_theme)
console.print("This is information", style="info")
console.print("Something terrible happened!", style="danger")

from rich.text import Text
text = Text("Hello, World!")
text.stylize(0, 8, "bold magenta")
console.print(text)


from rich.highlighter import RegexHighlighter

class EmailHighlighter(RegexHighlighter):
    """Apply style to anything that looks like an email."""

    base_style = "example."
    highlights = [r"(?P<email>[\w-]+@([\w-]+\.)+[\w-]+)"]


theme = Theme({"example.email": "bold magenta"})
console = Console(highlighter=EmailHighlighter(), theme=theme)
console.print("Send funds to money@example.org")


from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rouge One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)


MARKDOWN = """
# This is a h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""
from rich.markdown import Markdown

console = Console()
md = Markdown(MARKDOWN)
console.print(md)

