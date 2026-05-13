import os
import json
from groq import Groq
from assistant.config import SYSTEM_PROMPT, MODELO


def cargar_historial():
    if os.path.exists("historial.json"):
        try:
            with open("historial.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
        except (json.JSONDecodeError, OSError):
            pass
    return []


def guardar_historial(historial: list):
    try:
        with open("historial.json", "w", encoding="utf-8") as f:
            json.dump(historial, f, ensure_ascii=False, indent=4)
        return True
    except (OSError, IOError):
        return False


def resumir_historial(historial: list, client: Groq) -> bool:
    try:
        response = client.chat.completions.create(
            model=MODELO,
            max_tokens=200,
            messages=[
                {"role": "system", "content": "Resume la conversación en 3 puntos clave. Sé breve."}
            ] + historial
        )

        resumen = response.choices[0].message.content

        historial.clear()
        historial.append({"role": "system", "content": SYSTEM_PROMPT})
        historial.append({"role": "assistant", "content": resumen})

        return True
    except Exception:
        return False