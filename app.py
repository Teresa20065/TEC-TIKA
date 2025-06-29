import gradio as gr
import time
# from ia_core import preguntar_a_gemini # solo usa gemini
from rag_core import responder_rag # usa gemini con rag

def obtener_respuesta_mock(consulta): 
    """
    Toma la consulta del usuario y devuelve una respuesta de ejemplo.
    """
    return responder_rag(consulta)

def chatbot_response(message, history):
    # Verificar que hay un mensaje
    if not message:
        return history, ""
    
    try:
        response = obtener_respuesta_mock(message)
        if not response:
            response = "Lo siento, no pude procesar tu consulta en este momento. ¿Podrías reformular tu pregunta sobre auriculares?"
    except Exception as e:
        print(f"Error al obtener respuesta de IA: {e}")
        response = "Disculpa, hubo un problema técnico. ¿Podrías intentar de nuevo?"

    time.sleep(1)

    # Inicializa history si es None
    if history is None:
        history = []

    # Agrega los mensajes como diccionarios
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": response})

    return history, ""

# Función para manejar los botones de sugerencias
def handle_suggestion(suggestion, history):
    return chatbot_response(suggestion, history)

# CSS personalizado para recrear el diseño
custom_css = """
/* Fondo principal con gradiente */
.gradio-container {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%) !important;
    font-family: 'Inter', sans-serif !important;
}

/* Estilo del contenedor principal */
.main-container {
    max-width: 900px !important;
    margin: 0 auto !important;
    padding: 2rem !important;
}

/* Título principal */
.main-title {
    text-align: center !important;
    font-size: 2.5rem !important;
    font-weight: bold !important;
    margin-bottom: 1rem !important;
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
}

/* Subtítulo */
.subtitle {
    text-align: center !important;
    color: #a0a0a0 !important;
    font-size: 1.1rem !important;
    margin-bottom: 2rem !important;
}

/* Contenedor del chat */
.chat-container {
    background: rgba(255, 255, 255, 0.05) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(10px) !important;
    padding: 1rem !important;
    margin-bottom: 1rem !important;
}

/* Botones de sugerencias */
.suggestion-btn {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 15px !important;
    color: white !important;
    padding: 1.5rem !important;
    margin: 0.5rem !important;
    transition: all 0.3s ease !important;
    backdrop-filter: blur(10px) !important;
    height: 120px !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    font-size: 0.9rem !important;
    line-height: 1.4 !important;
    white-space: pre-line !important;
}

.suggestion-btn:hover {
    background: rgba(255, 255, 255, 0.2) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2) !important;
}

/* Input del chat */
.input-container input {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 25px !important;
    color: white !important;
    padding: 1rem 1.5rem !important;
}

.input-container input::placeholder {
    color: rgba(255, 255, 255, 0.6) !important;
}

/* Mensajes del chat */
.message {
    margin: 1rem 0 !important;
    padding: 1rem !important;
    border-radius: 15px !important;
}

.user-message {
    background: linear-gradient(45deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    margin-left: 20% !important;
}

.bot-message {
    background: rgba(255, 255, 255, 0.1) !important;
    color: white !important;
    margin-right: 20% !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
}
"""

# Crear la interfaz principal
with gr.Blocks(css=custom_css, title="Headphones AI Assistant") as demo:
    # Estado del historial del chat
    chatbot_history = gr.State([])
    
    with gr.Column(elem_classes="main-container"):
        # Título y subtítulo
        gr.HTML("""
            <div class="main-title">
                Find headphones 🎧 that beat your heart
            </div>
            <div class="subtitle">
                Talk freely and our AI will fit the best headphones for you
            </div>
        """)
        
 # Sección "You may ask"
        gr.HTML("<div style='text-align: center; color: #a0a0a0; margin: 2rem 0;'>You may ask</div>")
        
        # Botones de sugerencias
        with gr.Row():
            btn1 = gr.Button(
                "🏋️hola",
                elem_classes="suggestion-btn"
            )
            btn2 = gr.Button(
                "📱como te llamas?",
                elem_classes="suggestion-btn"
            )
            btn3 = gr.Button(
                "🎵eres hombre o mujer?",
                elem_classes="suggestion-btn"
            )
            btn4 = gr.Button(
                "💰cuantos años tienes?",
                elem_classes="suggestion-btn"
            )

        # Contenedor del chat
        with gr.Column(elem_classes="chat-container"):
            chatbot = gr.Chatbot(
                value=[],
                height=300,
                show_label=False,
                container=False,
                type="messages"
            )
            # Botón de enviar
            with gr.Row():
                msg_input = gr.Textbox(
                    placeholder="I'm looking for...",
                    show_label=False,
                    container=False,
                    scale=4,
                    elem_classes="input-container"
                )
                send_btn = gr.Button("🔍", scale=1, variant="primary")
        
       
    
    # Funciones de eventos - los botones envían preguntas fijas al chatbot
    def send_message(message, history):
        return chatbot_response(message, history)
    
    def use_suggestion_1(history):
        return handle_suggestion("hola", history)
    
    def use_suggestion_2(history):
        return handle_suggestion("como te llamas?", history)
    
    def use_suggestion_3(history):
        return handle_suggestion("eres hombre o mujer?", history)
    
    def use_suggestion_4(history):
        return handle_suggestion("cuantos años tienes?", history)
    
    # Eventos
    send_btn.click(
        send_message,
        inputs=[msg_input, chatbot_history],
        outputs=[chatbot, msg_input],
        show_progress=True
    )
    
    msg_input.submit(
        send_message,
        inputs=[msg_input, chatbot_history],
        outputs=[chatbot, msg_input],
        show_progress=True
    )
    
    btn1.click(
        use_suggestion_1,
        inputs=[chatbot_history],
        outputs=[chatbot, msg_input]
    )
    
    btn2.click(
        use_suggestion_2,
        inputs=[chatbot_history],
        outputs=[chatbot, msg_input]
    )
    
    btn3.click(
        use_suggestion_3,
        inputs=[chatbot_history],
        outputs=[chatbot, msg_input]
    )
    
    btn4.click(
        use_suggestion_4,
        inputs=[chatbot_history],
        outputs=[chatbot, msg_input]
    )
    
    # Actualizar el estado del historial
    chatbot.change(
        lambda x: x,
        inputs=[chatbot],
        outputs=[chatbot_history]
    )

# Lanzar la aplicación
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,
        show_error=True
    )