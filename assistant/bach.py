from assistant.config import RED,RESET
from assistant.main import run_chat

def ReadFile(routeFile: str) -> tuple[bool, str]:
    try:
        with open(routeFile, "r", encoding="utf-8") as file:
            return True, file.read()   
    except FileNotFoundError:

        return False, "❌ Archivo no encontrado"

    except PermissionError:

        return False, "❌ Sin permisos para abrir el archivo"

    except Exception as e:

        return False, f"❌ Error: {e}"
    
def verify_mode(mode:str) -> bool:
    allowCommands = [
        "--explicar",
        "--mejorar",
        "--bugs"
    ]
    return mode in allowCommands
def command_control(mode:str, routeFile:str):
    status, fileRead = ReadFile(routeFile)
    if mode == "--explicar" and status:
        systemPrompt = """
        Eres un experto programador. 
        Analiza el código y responde en español.
        """
    elif mode == "--mejorar" and status:
        systemPrompt = """
            Eres un experto programador.
            Genera únicamente código válido.
            Genera y mejora el codigo completos.
            NO expliques Mucho, solo lo necesario.
            NO uses markdown.
            NO escribas ```'lenguaje', ni al final ```.
            SOLO devuelve código 
        """
    elif mode == "--bugs" and status:
        systemPrompt = """
        Eres un experto programador. 
        Encuentra bugs y problemas potenciales en el código.
        """
    else:
        print(f"{RED}{fileRead}{RESET}")
        return
    message =[{
            'role':'system',
            'content':systemPrompt
        },
        {
            'role':'user',
            'content': fileRead
        }]
    run_chat(message)
    