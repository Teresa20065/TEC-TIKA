import gradio as gr
import random
import time
from rag_core import responder_rag # usa gemini con rag

def obtener_respuesta_mock(consulta): 
    """
    Toma la consulta del usuario y devuelve una respuesta de ejemplo.
    """
    return responder_rag(consulta)



# CSS personalizado para hacer la interfaz más colorida y atractiva
custom_css = """
/* Estilo general */
.gradio-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    font-family: 'Arial', sans-serif;
}

/* Header principal */
.main-header {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7, #DDA0DD);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Tarjetas coloridas */
.info-card {
    background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
    border-left: 5px solid #ff6b6b;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.feature-card {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    padding: 15px;
    border-radius: 12px;
    margin: 8px 0;
    text-align: center;
    transition: transform 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

/* Botones coloridos */
.btn-gradient {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4) !important;
    border: none !important;
    color: white !important;
    font-weight: bold !important;
    padding: 12px 24px !important;
    border-radius: 25px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
}

.btn-gradient:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.3) !important;
}

/* Área de respuesta */
.response-area {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
    border-radius: 15px;
    color: white;
    box-shadow: 0 5px 20px rgba(0,0,0,0.2);
}

/* Ejemplos coloridos */
.example-container {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
}
"""

# Crear la interfaz con diseño mejorado
with gr.Blocks(
    theme=gr.themes.Base(),
    css=custom_css,
    title="🌟 Asistente Aduanero AI"
) as app:
    
    # Header principal con animación
    gr.HTML("""
    <div class="main-header">
        <h1 style="color: white; font-size: 3em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            🌟 Asistente Aduanero AI
        </h1>
        <h2 style="color: white; font-size: 1.5em; margin: 10px 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            🚀 Empoderando a PyMEs y artesanos a llevar sus productos al mundo 🌍
        </h2>
        <p style="color: white; font-size: 1.1em; opacity: 0.9;">
            ✨ Tu experto en comercio internacional disponible 24/7 ✨
        </p>
    </div>
    """)
    
    # Tarjetas informativas coloridas
    with gr.Row():
        with gr.Column():
            gr.HTML("""
            <div class="info-card">
                <h3 style="color: #333; margin-top: 0;">🎯 ¿Qué puedo hacer por ti?</h3>
                <ul style="color: #555;">
                    <li>📊 Consultar aranceles y partidas</li>
                    <li>📋 Guía paso a paso para exportar</li>
                    <li>🌐 Información sobre mercados internacionales</li>
                    <li>📜 Documentos y certificaciones necesarias</li>
                </ul>
            </div>
            """)
        
        with gr.Column():
            gr.HTML("""
            <div class="info-card" style="background: linear-gradient(135deg, #a8e6cf 0%, #ffd3a5 100%);">
                <h3 style="color: #333; margin-top: 0;">💡 Especializado en:</h3>
                <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px;">
                    <span style="background: #ff6b6b; color: white; padding: 5px 12px; border-radius: 15px; font-size: 0.9em;">🧶 Textiles</span>
                    <span style="background: #4ecdc4; color: white; padding: 5px 12px; border-radius: 15px; font-size: 0.9em;">🎨 Artesanías</span>
                    <span style="background: #45b7d1; color: white; padding: 5px 12px; border-radius: 15px; font-size: 0.9em;">🍫 Alimentos</span>
                    <span style="background: #96ceb4; color: white; padding: 5px 12px; border-radius: 15px; font-size: 0.9em;">⚡ Tecnología</span>
                </div>
            </div>
            """)
    
    # Área principal de interacción
    with gr.Row():
        # Columna izquierda - Input del usuario
        with gr.Column(scale=1):
            gr.HTML("""
            <div style="background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%); 
                        padding: 20px; border-radius: 15px; margin-bottom: 15px; text-align: center;">
                <h3 style="color: #2d3436; margin: 0;">💬 Hazme tu pregunta</h3>
            </div>
            """)
            
            pregunta_usuario = gr.Textbox(
                label="🤔 ¿Qué necesitas saber?",
                placeholder="Ej: ¿Qué necesito para exportar textiles de alpaca a Estados Unidos?",
                lines=4,
                elem_classes="input-colorful"
            )
            
            boton_consultar = gr.Button(
                "🚀 Consultar al Experto", 
                variant="primary",
                size="lg",
                elem_classes="btn-gradient"
            )
            
            # Ejemplos con diseño mejorado
            gr.HTML("""
            <div class="example-container">
                <h4 style="color: #2d3436; margin-top: 0;">💡 Preguntas de ejemplo:</h4>
            </div>
            """)
            
            gr.Examples(
                [
                    " ¿Qué información debe contener el Certificado de Origen de la Asociación Latinoamericana de Integración?",
                    " ¿Cuáles son los pasos para obtener un certificado de origen para exportar productos?",
                    " ¿Qué observaciones importantes debo considerar al llenar un certificado de origen?",
                    " ¿Quién debe firmar y certificar el Certificado de Origen según la normativa?",
                ],
                inputs=pregunta_usuario
            )
        
        # Columna derecha - Respuesta de la IA
        with gr.Column(scale=2):
            gr.HTML("""
            <div style="background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%); 
                        padding: 20px; border-radius: 15px; margin-bottom: 15px; text-align: center;">
                <h3 style="color: white; margin: 0;">🤖 Respuesta del Experto</h3>
            </div>
            """)
            
            respuesta_ia = gr.Markdown(
                """
### 👋 ¡Bienvenido al Asistente Aduanero AI!

Estoy aquí para ayudarte con todas tus consultas sobre:
- 📊 **Aranceles y clasificación arancelaria**
- 🚢 **Procesos de exportación e importación**  
- 📋 **Documentación y certificaciones**
- 🌍 **Oportunidades de mercado internacional**
- 💡 **Consejos para PyMEs y emprendedores**

**¡Haz tu primera pregunta y comencemos! 🚀**
                """,
                elem_classes="response-area"
            )
    
    # Footer con información adicional
    gr.HTML("""
    <div style="background: linear-gradient(45deg, #2d3436, #636e72); 
                padding: 20px; border-radius: 15px; margin-top: 20px; text-align: center;">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px;">
            <div class="feature-card">
                <h4 style="color: #2d3436; margin: 0;">⚡ Respuestas Rápidas</h4>
                <p style="color: #636e72; margin: 5px 0;">Información al instante</p>
            </div>
            <div class="feature-card">
                <h4 style="color: #2d3436; margin: 0;">🎯 Especializado</h4>
                <p style="color: #636e72; margin: 5px 0;">Enfoque en PyMEs</p>
            </div>
            <div class="feature-card">
                <h4 style="color: #2d3436; margin: 0;">🌟 Actualizado</h4>
                <p style="color: #636e72; margin: 5px 0;">Normativas vigentes</p>
            </div>
            <div class="feature-card">
                <h4 style="color: #2d3436; margin: 0;">🤝 Accesible</h4>
                <p style="color: #636e72; margin: 5px 0;">Disponible 24/7</p>
            </div>
        </div>
        <p style="color: white; margin-top: 15px; opacity: 0.8;">
            💼 Desarrollado para impulsar el comercio internacional de pequeñas y medianas empresas 🌟
        </p>
    </div>
    """)
    
    # Conectar funcionalidad
    boton_consultar.click(
        fn=obtener_respuesta_mock,
        inputs=pregunta_usuario,
        outputs=respuesta_ia
    )
    
    # También responder al presionar Enter
    pregunta_usuario.submit(
        fn=obtener_respuesta_mock,
        inputs=pregunta_usuario,
        outputs=respuesta_ia
    )

# Lanzar la aplicación con configuración optimizada
if __name__ == "__main__":
    print("🌟 Iniciando Asistente Aduanero AI...")
    print("🎨 Interfaz colorida y mejorada cargando...")
    print("🚀 ¡Abre tu navegador para ver el resultado!")
    
    app.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        debug=True,
        show_api=False,
        favicon_path=None,
        inbrowser=True  # Abre automáticamente el navegador
    )