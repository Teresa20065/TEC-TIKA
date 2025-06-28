import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Cargar variables de entorno desde .env
load_dotenv()

# Ahora la API key se toma automáticamente de la variable de entorno
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")