from rich.align import Align
from rich.console import Console
from rich.text import Text

ART = r"""
  ____ _     ___
 / ___| |   |_ _|
| |   | |    | |
| |___| |___ | |
 \____|_____|___|
"""

console = Console()

art = Text(ART.strip("\n"), style="bold cyan", justify="left", no_wrap=True)

console.print(
    Align(
        art,
        align="center",
        vertical="middle",
        height=console.height - 1,
    )
)