import sys
from time import sleep

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

from terminal.comandos.comandos import prompts

console = Console()


def mostrar_mensagem(texto, estilo="cyan"):
    console.print(Text(texto, style=estilo))


while True:
    entrada = Prompt.ask("[bold #a855f7]>[/]").strip().casefold()

    if entrada == "help" or entrada == "h":
        prompts()

    elif entrada == "exit":
        sleep(2)
        console.print("[bold #c084fc]Até logo![/]")
        sys.exit(0)

    elif entrada == "clear" or entrada == "cls":
        console.clear()

    elif entrada == "version" or entrada == "v":
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