import sys
from assistant.main import run_chat
from assistant.config import MODELO


def mostrar_ayuda():
    print(f"""Uso: python -m assistant [OPCIONES]

Opciones:
  chat          Iniciar el chat interactivo (por defecto)
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

    if not args or args[0] == "chat":
        run_chat()
    elif args[0] in ("-h", "--help"):
        mostrar_ayuda()
    elif args[0] == "--version":
        mostrar_version()
    else:
        print(f"Error: argumento desconocido '{args[0]}'")
        print("Usa --help para ver las opciones disponibles.")
        sys.exit(1)


if __name__ == "__main__":
    main()