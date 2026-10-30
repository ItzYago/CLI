import sys

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

from terminal.comandos.comandos import comandos

console = Console()


def mostrar_mensagem(texto, estilo="cyan"):
    console.print(Text(texto, style=estilo))


while True:
    entrada = Prompt.ask("[bold #a855f7]>[/]").strip().casefold()

    if entrada == "help":
        comandos()

    elif entrada == "exit":
        console.print("[bold #c084fc]Até logo![/]")
        sys.exit(0)

    elif entrada == "clear":
        console.clear()

    elif entrada == "version":
        console.print(
            Panel("Versão atual: 0.0.1", border_style="#a855f7", expand=False)
        )

    elif entrada == "about":
        console.print(
            Panel(
                "Este é um programa de terminal simples desenvolvido em Python.",
                title="[bold #c084fc]about[/]",
                border_style="#a855f7",
            )
        )

    elif entrada == "":
        continue

    else:
        console.print(
            f"[red]Comando não reconhecido:[/] [bold]{entrada}[/]. "
            "Digite [bold #c084fc]help[/] para ver os comandos disponíveis."
        )