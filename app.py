import gradio as gr 
 
def obtener_respuesta_mock(consulta): 
    """ 
    Esta es una función de prueba. Finge ser la IA. 
    Toma la consulta del usuario y devuelve una respuesta de ejemplo. 
    """ 
    print(f"La consulta del usuario fue: {consulta}") 
    return f"Respuesta de prueba para la consulta: '{consulta}'. La IA real se conectará pronto. ¡Buen trabajo!" 
 
# --- Aquí se define la interfaz visual --- 
with gr.Blocks(theme=gr.themes.Soft()) as app: 
    gr.Markdown( 
        """ 
        # Asistente Aduanero AI 
 
        ### Empoderando a PyMEs y artesanos a llevar sus productos al mundo. 
        """ 
    ) 
 
    with gr.Row(): 
        # Columna de la izquierda para la entrada del usuario 
        with gr.Column(scale=1): 
            pregunta_usuario = gr.Textbox( 
                label="Escribe tu consulta aquí", 
                placeholder="Ej: ¿Qué necesito para exportar textiles de alpaca?", 
                lines=5 
            ) 
            boton_consultar = gr.Button("Consultar al Experto", variant="primary") 
            gr.Examples( 
                [ 
                    "¿Qué arancel tienen los paneles solares?", 
                    "Soy una artesana, ¿cómo exporto mis productos por primera vez?", 
                    "¿Qué es el ODS 10 y cómo ayuda el comercio?", 
                ], 
                inputs=pregunta_usuario 
            ) 
 
        # Columna de la derecha para la respuesta de la IA 
        with gr.Column(scale=2): 
            respuesta_ia = gr.Markdown("### Respuesta del Experto:\n---") 
 
    # --- Aquí se conecta el botón con la función --- 
    boton_consultar.click( 
        fn=obtener_respuesta_mock, 
        inputs=pregunta_usuario, 
        outputs=respuesta_ia 
    ) 
 
# Lanza la aplicación 
if __name__ == "__main__": 
    app.launch()