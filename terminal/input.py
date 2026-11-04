import json
import time as tm
from pathlib import Path

from terminal.conta.conta_verificada import dentro_conta

CAMINHO_LOG = Path(__file__).parent / "conta" / "log_criado.json"


def input_entrar(username=None, password=None):
    with open(CAMINHO_LOG, "r", encoding="utf-8") as file:
        dados = json.load(file)

    if username is None:
        username = input("Digite seu nome de usuário: ").strip()

    if password is None:
        password = input("Digite sua senha: ")

    print("Verificando...")
    tm.sleep(3)

    for usuario in dados["usuarios"]:
        if usuario["username"] == username and usuario["senha_hash"] == password:
            print("Login bem-sucedido!")
            return dentro_conta()

    print("Login falhou. Usuário ou senha incorretos.")
    return None


if __name__ == "__main__":
    input_entrar()