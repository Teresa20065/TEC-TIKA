from rag import graph

def responder_rag(pregunta):
    response = graph.invoke({"question": pregunta}) # default "¿Qué información debe contener el Certificado de Origen de la Asociación Latinoamericana de Integración?"
    return response["answer"]