import streamlit as st
import streamlit as st
import pandas as pd
from itertools import combinations

st.set_page_config(page_title="Prode Mundial 2026", page_icon="⚽")

# 1. Base de datos de grupos completa
grupos_2026 = {
    "Grupo A": ["México", "Sudáfrica", "Corea del Sur", "Rep. Checa"],
    "Grupo B": ["Canadá", "Bosnia", "Qatar", "Suiza"],
    "Grupo C": ["Brasil", "Marruecos", "Haití", "Escocia"],
    "Grupo D": ["EEUU", "Paraguay", "Australia", "Turquía"],
    "Grupo E": ["Alemania", "Curazao", "Costa de Marfil", "Ecuador"],
    "Grupo F": ["Países Bajos", "Japón", "Suecia", "Túnez"],
    "Grupo G": ["Bélgica", "Egipto", "Irán", "Nueva Zelanda"],
    "Grupo H": ["España", "Cabo Verde", "Arabia Saudita", "Uruguay"],
    "Grupo I": ["Francia", "Senegal", "Irak", "Noruega"],
    "Grupo J": ["Argentina", "Argelia", "Austria", "Jordania"],
    "Grupo K": ["Portugal", "RD Congo", "Uzbekistán", "Colombia"],
    "Grupo L": ["Inglaterra", "Croacia", "Ghana", "Panamá"]
}

st.title("🏆 Mi Prode Mundial 2026")

# Creamos un diccionario para guardar los resultados
if 'prode_usuario' not in st.session_state:
    st.session_state.prode_usuario = {}

# --- INTERFAZ DINÁMICA ---
for nombre_grupo, equipos in grupos_2026.items():
    with st.expander(f"📅 {nombre_grupo}"):
        for local, visitante in combinations(equipos, 2):
            key_l = f"{local}_{visitante}_L"
            key_v = f"{local}_{visitante}_V"
            
            col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 3])
            
            with col1: st.write(local)
            with col2: goles_l = st.number_input("L", 0, 20, key=key_l, label_visibility="collapsed")
            with col3: st.write("vs")
            with col4: goles_v = st.number_input("V", 0, 20, key=key_v, label_visibility="collapsed")
            with col5: st.write(visitante)
            
            # Guardamos en el estado de la sesión
            st.session_state.prode_usuario[f"{local} vs {visitante}"] = [goles_l, goles_v]

if st.button("💾 Guardar mis predicciones"):
    # Convertimos el diccionario a un DataFrame y lo bajamos como CSV (base de datos simple)
    df_resultado = pd.DataFrame.from_dict(st.session_state.prode_usuario, orient='index', columns=['Goles Local', 'Goles Visitante'])
    df_resultado.to_csv("mis_pronosticos.csv")
    st.success("¡Predicciones guardadas en 'mis_pronosticos.csv'!")
    st.balloons() # ¡Festejo!