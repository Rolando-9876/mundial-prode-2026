import streamlit as st
import pandas as pd
from itertools import combinations

st.set_page_config(page_title="Prode Mundial 2026", page_icon="⚽")


fixture_fase_grupos = {
    "Grupo A (Sede México)": [
        {"local": "México", "visitante": "Sudáfrica", "fecha": "11/06", "hora": "15:00", "sede": "Estadio Azteca, CDMX"},
        {"local": "Nueva Zelanda", "visitante": "Noruega", "fecha": "12/06", "hora": "18:00", "sede": "Estadio Akron, Guadalajara"},
    ],
    "Grupo D (Sede USA)": [
        {"local": "Estados Unidos", "visitante": "Australia", "fecha": "12/06", "hora": "21:00", "sede": "SoFi Stadium, LA"},
        {"local": "Panamá", "visitante": "Polonia", "fecha": "13/06", "hora": "16:00", "sede": "Levi's Stadium, SF"},
    ],
    "Grupo J (Argentina)": [
        {"local": "Argentina", "visitante": "Argelia", "fecha": "15/06", "hora": "18:00", "sede": "Estadio BBVA, Monterrey"},
        {"local": "Austria", "visitante": "Jordania", "fecha": "15/06", "hora": "21:00", "sede": "MetLife Stadium, NJ"},
        {"local": "Argentina", "visitante": "Austria", "fecha": "20/06", "hora": "15:00", "sede": "Estadio Akron, Guadalajara"},
        {"local": "Argelia", "visitante": "Jordania", "fecha": "20/06", "hora": "18:00", "sede": "NRG Stadium, Houston"},
    ],
    "Grupo L": [
        {"local": "Inglaterra", "visitante": "Ghana", "fecha": "16/06", "hora": "14:00", "sede": "BMO Field, Toronto"},
        {"local": "España", "visitante": "Irak", "fecha": "16/06", "hora": "17:00", "sede": "Prudential Park, Boston"},
    ]
}

st.title("🏆 Mi Prode Mundial 2026")

# Creamos un diccionario para guardar los resultados
if 'prode_usuario' not in st.session_state:
    st.session_state.prode_usuario = {}

# --- INTERFAZ DINÁMICA ---
pronosticos = []

for nombre_grupo, partidos in fixture_fase_grupos.items():
    with st.expander(f"📅 {nombre_grupo}", expanded=True):
        for partido in partidos:
            st.caption(f"🏟️ {partido['sede']} | 🕒 {partido['fecha']} - {partido['hora']} hs")
            
            col_l, col_gl, col_vs, col_gv, col_v = st.columns([3, 1, 0.5, 1, 3])
            
            with col_l:
                st.write(f"**{partido['local']}**")
            with col_gl:
                gl = st.number_input("L", 0, 15, key=f"{partido['local']}_{partido['visitante']}_L", label_visibility="collapsed")
            with col_vs:
                st.write("vs")
            with col_gv:
                gv = st.number_input("V", 0, 15, key=f"{partido['local']}_{partido['visitante']}_V", label_visibility="collapsed")
            with col_v:
                st.write(f"**{partido['visitante']}**")
            
            # Guardamos en el estado de la sesión
            pronosticos.append({
                "Grupo": nombre_grupo,
                "Local": partido['local'],
                "Goles L": gl,
                "Goles V": gv,
                "Visitante": partido['visitante']
            })
            st.markdown("---")

if st.button("💾 Guardar mis predicciones"):
   
    df_resultado = pd.DataFrame.from_dict(st.session_state.prode_usuario, orient='index', columns=['Goles Local', 'Goles Visitante'])
    df_resultado.to_csv("mis_pronosticos.csv")
    st.success("¡Predicciones guardadas en 'mis_pronosticos.csv'!")
    st.balloons() 