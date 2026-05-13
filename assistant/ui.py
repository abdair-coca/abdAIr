from assistant.config import CYAN, BOLD, RESET


def mostrar_banner(modelo: str):
    print(f"""{CYAN}{BOLD}
+------------------------------------------+
|        Asistente IA - CLI               |
|              Powered by Groq            |
+------------------------------------------+{RESET}
Modelo: {modelo}
Escribe {BOLD}/ayuda{RESET} para ver comandos.
Usa {BOLD}Ctrl+C{RESET} para interrumpir.
Usa {BOLD}/salir{RESET} para terminar.
""")


def mostrar_prompt():
    return input(f"\n{BOLD}Tu:{RESET} ").strip()