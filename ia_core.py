import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('models/gemini-2.5-flash')

def preguntar_a_gemini(pregunta):
    try:
        response = model.generate_content(pregunta)
        return response.text
    except Exception as e:
        return f"Ocurrió un error: {e}"
    
def leer_fragmentos_ley(ruta_archivo="ley_fragmentos.txt"):
    """
    Lee el archivo de fragmentos de ley y devuelve su contenido como un string.
    """
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no fue encontrado.")
        return ""
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return ""