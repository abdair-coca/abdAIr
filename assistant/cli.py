import sys
from assistant.main import run_chat
from assistant.config import MODELO
from assistant.bach import verify_mode, command_control

def mostrar_ayuda():
    print(f"""Uso: python -m assistant [OPCIONES]

Opciones:
  chat          Iniciar el chat interactivo (por defecto)
  --mejorar nombre_archivo
  --explicar nombre_archivo
  --bugs nombre_archivo
  -h, --help    Mostrar esta ayuda
  --version     Mostrar version

Ejemplos:
  python -m assistant
  python -m assistant chat
  python -m assistant -h
""")


def mostrar_version():
    print(f"assistant CLI v1.0 - Modelo: {MODELO}")


def main():
    args = sys.argv[1:]

    if not args or args[0] == "chat" :
        run_chat([])
    elif args[0] in ("-h", "--help"):
        mostrar_ayuda()
    elif args[0] == "--version":
        mostrar_version()
    elif verify_mode(args[0]) and args[1]:
        command_control(args[0], args[1])
    else:
        print(f"Error: argumento desconocido '{args[0]}'")
        print("Usa --help para ver las opciones disponibles.")
        sys.exit(1)


if __name__ == "__main__":
    main()