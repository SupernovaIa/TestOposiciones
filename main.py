import os
from dotenv import load_dotenv

from src.assistant import OpenAIAssistantManager

# Cargar variables de entorno
if not load_dotenv():
    print("Advertencia: No se encontró el archivo .env.")

# ID del asistente en OpenAI
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

if not ASSISTANT_ID:
    raise ValueError("No se ha encontrado el ASSISTANT_ID en las variables de entorno.")

if __name__ == '__main__':
    try:
        assistant = OpenAIAssistantManager()
        assistant.get_assistant(ASSISTANT_ID)
    except Exception as e:
        print(f"Error al obtener el asistente: {e}")
        exit(1)

    while True:
        try:
            prompt = input("Tú: ")
            if prompt.lower() in ["salir", "exit", "quit"]:
                print("Asistente: ¡Hasta luego!")
                break

            respuesta = assistant.chat(prompt)
            print(f"Asistente: {respuesta}")
        except Exception as e:
            print(f"Se ha producido un error: {e}")
