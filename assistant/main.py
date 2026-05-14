import os
import sys
from assistant.config import MODELO, RED, SYSTEM_PROMPT
from assistant.chat import crear_cliente, chat
from assistant.history import cargar_historial, resumir_historial
from assistant.commands import manejar_comando
from assistant.ui import mostrar_banner, mostrar_prompt, RESET


def run_chat(bachCommand: list):
    os.system("cls" if os.name == "nt" else "clear")

    mostrar_banner(MODELO)

    client = crear_cliente()
    if client is None:
        sys.exit(1)

    tokens_totales = {"entrada": 0, "salida": 0}
    historial = cargar_historial()
    if not historial and bachCommand:
        historial = bachCommand
        chat(client, historial, "", tokens_totales)
    elif historial and bachCommand:
        historial.insert(bachCommand)
        chat(client, historial, "", tokens_totales)
    elif not historial:
        historial = [{'role': 'system', 'content':SYSTEM_PROMPT}]


    while True:
        try:
            entrada = mostrar_prompt()
        except (EOFError, KeyboardInterrupt):
            print()
            manejar_comando("/salir", historial, tokens_totales, client)
            break

        if not entrada:
            continue

        if entrada.startswith("/"):
            continuar = manejar_comando(entrada, historial, tokens_totales, client)
            if not continuar:
                break
            continue

        if len(entrada) > 20000:
            print(f"{RED}Mensaje muy largo (max 20000).{RESET}")
            continue

        if len(historial) >= 20:
            print(f"{RED}Limite alcanzado. Resumiendo...{RESET}")
            resumir_historial(historial, client)

        chat(client, historial, entrada, tokens_totales)


if __name__ == "__main__":
    run_chat()