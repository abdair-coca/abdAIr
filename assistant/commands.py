import os
from assistant.config import CYAN, GREEN, RED, YELLOW, GREY, BOLD, RESET
from assistant.history import guardar_historial, resumir_historial


def manejar_comando(comando: str, historial: list, tokens_totales: dict, client) -> bool:
    cmd = comando.lower().strip()

    if cmd in ("/salir", "/exit", "/q"):
        total = tokens_totales["entrada"] + tokens_totales["salida"]
        print(f"\n{CYAN}Sesion terminada.{RESET}")
        print(f"{GREY}Tokens: entrada={tokens_totales['entrada']}, salida={tokens_totales['salida']}, total={total}{RESET}")
        return False

    elif cmd == "/limpiar":
        historial.clear()
        os.system("cls" if os.name == "nt" else "clear")
        historial.append({"role": "system", "content": "Eres un asistente inteligente y amigable."})
        print(f"{CYAN}Historial limpiado.{RESET}\n")

    elif cmd == "/historial":
        if not historial:
            print(f"{GREY}El historial esta vacio.{RESET}")
        else:
            print(f"\n{CYAN}-- Historial ({len(historial)} mensajes) --{RESET}")
            for i, msg in enumerate(historial):
                rol = "user" if msg["role"] == "user" else "AI"
                preview = msg["content"][:80].replace("\n", " ")
                if len(msg["content"]) > 80:
                    preview += "..."
                print(f"  [{i+1}] {rol}: {preview}")
            print()

    elif cmd == "/tokens":
        total = tokens_totales["entrada"] + tokens_totales["salida"]
        print(f"{GREY}Tokens: entrada={tokens_totales['entrada']}, salida={tokens_totales['salida']}, total={total}{RESET}")

    elif cmd == "/guardar":
        if guardar_historial(historial):
            print(f"{GREEN}Historial guardado.{RESET}")
        else:
            print(f"{RED}Error al guardar.{RESET}")

    elif cmd == "/resumir":
        resumir_historial(historial, client)
        print(f"{CYAN}Historial resumido.{RESET}")

    elif cmd == "/ayuda":
        print(f"""
{CYAN}Comandos disponibles:{RESET}
  /salir     → Salir del programa
  /limpiar   → Borrar historial
  /historial → Ver mensajes
  /tokens    → Ver tokens usados
  /guardar   → Guardar historial
  /resumir   → Resumir historial
  /ayuda     → Mostrar ayuda
""")

    else:
        print(f"{YELLOW}Comando desconocido: '{comando}'. Escribe /ayuda.{RESET}")

    return True