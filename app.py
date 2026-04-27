import streamlit as st
import random

st.set_page_config(page_title="Juegos Interactivos", page_icon="🎮")

st.title("🎮 Juegos Interactivos")

# -------------------------
# SELECTOR DE JUEGO
# -------------------------
modo = st.selectbox(
    "Elige un juego:",
    ["Villanas Disney", "Ley de IA en Perú"]
)

# -------------------------
# PREGUNTAS
# -------------------------

villanas = [
    {
        "pregunta": "¿Cómo se llama la villana de La Sirenita?",
        "opciones": ["Úrsula", "Maléfica", "Cruella", "Yzma"],
        "respuesta": "Úrsula"
    },
    {
        "pregunta": "¿Qué villana puede convertirse en dragón?",
        "opciones": ["Maléfica", "Reina Grimhilde", "Lady Tremaine", "Madre Gothel"],
        "respuesta": "Maléfica"
    },
    {
        "pregunta": "¿Quién odia a los dálmatas?",
        "opciones": ["Cruella de Vil", "Úrsula", "Yzma", "Maléfica"],
        "respuesta": "Cruella de Vil"
    },
    {
        "pregunta": "¿Qué villana aparece en Enredados?",
        "opciones": ["Madre Gothel", "Yzma", "Reina Roja", "Cruella"],
        "respuesta": "Madre Gothel"
    },
    {
        "pregunta": "¿Quién es la villana de Las locuras del emperador?",
        "opciones": ["Yzma", "Maléfica", "Úrsula", "Cruella"],
        "respuesta": "Yzma"
    }
]

ley_ia = [
    {
        "pregunta": "¿Qué promueve la Ley N.º 31814?",
        "opciones": [
            "El uso de inteligencia artificial para desarrollo",
            "La prohibición de la inteligencia artificial",
            "Solo el uso militar de IA",
            "El uso exclusivo en universidades"
        ],
        "respuesta": "El uso de inteligencia artificial para desarrollo"
    },
    {
        "pregunta": "¿Cuál es el objetivo principal del reglamento?",
        "opciones": [
            "Regular el uso responsable de IA",
            "Eliminar tecnologías digitales",
            "Privatizar la IA",
            "Restringir el acceso a internet"
        ],
        "respuesta": "Regular el uso responsable de IA"
    },
    {
        "pregunta": "¿La ley busca beneficiar principalmente a qué ámbito?",
        "opciones": [
            "Desarrollo económico y social",
            "Solo entretenimiento",
            "Sector militar",
            "Publicidad"
        ],
        "respuesta": "Desarrollo económico y social"
    },
    {
        "pregunta": "¿Qué enfoque tiene el uso de IA según la ley?",
        "opciones": [
            "Ético y responsable",
            "Sin regulación",
            "Solo comercial",
            "Exclusivo para expertos"
        ],
        "respuesta": "Ético y responsable"
    },
    {
        "pregunta": "¿Quién emitió el decreto supremo?",
        "opciones": [
            "Presidencia del Consejo de Ministros",
            "Ministerio de Deportes",
            "Congreso de EE.UU.",
            "ONU"
        ],
        "respuesta": "Presidencia del Consejo de Ministros"
    }
]

# Selección dinámica
preguntas = villanas if modo == "Villanas Disney" else ley_ia

# -------------------------
# ESTADO
# -------------------------
if "indice" not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntaje = 0
    st.session_state.preguntas_mezcladas = random.sample(preguntas, len(preguntas))
    st.session_state.opciones_mezcladas = []

# Reset si cambia juego
if "modo_actual" not in st.session_state:
    st.session_state.modo_actual = modo

if st.session_state.modo_actual != modo:
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# -------------------------
# JUEGO
# -------------------------
if st.session_state.indice < len(preguntas):

    pregunta_actual = st.session_state.preguntas_mezcladas[st.session_state.indice]

    if len(st.session_state.opciones_mezcladas) <= st.session_state.indice:
        opciones = pregunta_actual["opciones"].copy()
        random.shuffle(opciones)
        st.session_state.opciones_mezcladas.append(opciones)

    opciones = st.session_state.opciones_mezcladas[st.session_state.indice]

    st.subheader(f"Pregunta {st.session_state.indice + 1}")
    respuesta = st.radio(pregunta_actual["pregunta"], opciones)

    if st.button("Responder"):
        if respuesta == pregunta_actual["respuesta"]:
            st.success("¡Correcto!")
            st.session_state.puntaje += 1
        else:
            st.error(f"Incorrecto. Respuesta: {pregunta_actual['respuesta']}")

        st.session_state.indice += 1
        st.rerun()

else:
    st.subheader("🎯 Resultado final")
    st.write(f"Puntaje: {st.session_state.puntaje}/5")

    if st.session_state.puntaje == 5:
        st.balloons()
        st.success("🎉 ¡Perfecto!")
        st.snow()
    else:
        st.info("Sigue intentando")

    if st.button("Reiniciar"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
