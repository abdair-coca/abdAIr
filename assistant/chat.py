import os
import time
from groq import Groq, RateLimitError, APIConnectionError, APIStatusError
from assistant.config import MODELO, MAX_TOKENS, MAX_REINTENTOS, CYAN, RED, YELLOW, GREEN, BOLD, RESET


def crear_cliente() -> Groq | None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print(f"{RED}Error: API_KEY no encontrada.{RESET}")
        return None
    return Groq(api_key=api_key)


def chat(client: Groq, historial: list, mensaje: str, tokens_totales: dict) -> bool:
    if mensaje:
        historial.append({"role": "user", "content": mensaje})
    texto_acumulado = ""

    print(f"\n{GREEN}{BOLD}Asistente:{RESET} ", end="", flush=True)

    for intento in range(1, MAX_REINTENTOS + 1):
        try:
            stream = client.chat.completions.create(
                model=MODELO,
                max_tokens=MAX_TOKENS,
                messages=historial,
                stream=True
            )
            for chunk in stream:
                contenido = chunk.choices[0].delta.content or ""
                print(contenido, end="", flush=True)
                texto_acumulado += contenido

                if chunk.usage:
                    tokens_totales["entrada"] += chunk.usage.prompt_tokens
                    tokens_totales["salida"] += chunk.usage.completion_tokens

            print()

            historial.append({"role": "assistant", "content": texto_acumulado})
            return True

        except RateLimitError:
            espera = 2 ** intento
            print(f"\n{YELLOW}Limite. Esperando {espera}s...{RESET}")
            time.sleep(espera)
            texto_acumulado = ""

        except APIConnectionError:
            if intento < MAX_REINTENTOS:
                print(f"\n{YELLOW}Sin conexion. Reintentando...{RESET}")
                time.sleep(2 ** intento)
                texto_acumulado = ""
            else:
                print(f"\n{RED}No se pudo conectar a la API.{RESET}")
                historial.pop()
                return False

        except APIStatusError as e:
            print(f"\n{RED}Error de API ({e.status_code}).{RESET}")
            historial.pop()
            return False

        except KeyboardInterrupt:
            print(f"\n{YELLOW}(Generacion interrumpida){RESET}")
            if texto_acumulado:
                historial.append({"role": "assistant", "content": texto_acumulado})
            return True

    print(f"\n{RED}Se agotaron los reintentos.{RESET}")
    historial.pop()
    return False