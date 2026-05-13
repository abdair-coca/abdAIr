# assistant/config.py

import os
from dotenv import load_dotenv

load_dotenv()

MODELO = os.getenv("MODEL")

MAX_TOKENS = 300
MAX_REINTENTOS = 3

SYSTEM_PROMPT = """Eres un asistente inteligente y amigable.
Responde siempre en español, de forma clara y concisa.
Si el usuario pregunta sobre código, muéstralo con bloques de código.
Si no conoces algo con certeza, indícalo claramente."""

# ANSI Colors
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
GREY   = "\033[90m"
RESET  = "\033[0m"
BOLD   = "\033[1m"