import os
import sys
from assistant.config import MODELO, RED
from assistant.chat import crear_cliente, chat
from assistant.history import cargar_historial, resumir_historial
from assistant.commands import manejar_comando
from assistant.ui import mostrar_banner, mostrar_prompt


def run_chat():
    os.system("cls" if os.name == "nt" else "clear")

    mostrar_banner(MODELO)

    client = crear_cliente()
    if client is None:
        sys.exit(1)

    historial = cargar_historial()
    if not historial:
        from assistant.config import SYSTEM_PROMPT
        historial = [{"role": "system", "content": SYSTEM_PROMPT}]

    tokens_totales = {"entrada": 0, "salida": 0}

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