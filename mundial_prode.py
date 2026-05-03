import streamlit as st
import pandas as pd


st.set_page_config(page_title="Prode Mundial 2026", page_icon="⚽", layout="wide")
st.markdown("<h1 style='text-align: center; color: #004d99;'>⚽ PRODE MUNDIAL 2026</h1>", unsafe_allow_html=True)
st.divider()
st.markdown("""
    <style>
    .stTable { font-size: 20px !important; }
    .css-1offfwp { font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆Roply Prode - Mundial 2026")
st.markdown("### Fixture Oficial de la Fase de Grupos")
st.info("🕒 Horarios en hora de **Argentina** (GMT-3).")

tab1, tab2 = st.tabs(["📅 Cargar Resultados", "📊 Tablas de Posiciones"])



fixture_completo = {
    "Grupo A": [
        {"l": "México", "v": "Sudáfrica", "fecha": "11/06", "hora": "16:00", "sede": "CDMX"},
        {"l": "Corea del Sur", "v": "Rep. Checa", "fecha": "11/06", "hora": "23:00", "sede": "Guadalajara"},
        {"l": "Rep. Checa", "v": "Sudáfrica", "fecha": "18/06", "hora": "13:00", "sede": "Atlanta"},
        {"l": "México", "v": "Corea del Sur", "fecha": "18/06", "hora": "22:00", "sede": "Guadalajara"},
        {"l": "Rep. Checa", "v": "México", "fecha": "24/06", "hora": "22:00", "sede": "CDMX"},
        {"l": "Sudáfrica", "v": "Corea del Sur", "fecha": "24/06", "hora": "22:00", "sede": "Monterrey"},
    ],
    "Grupo B": [
        {"l": "Canadá", "v": "Bosnia y Herzegovina", "fecha": "12/06", "hora": "16:00", "sede": "Toronto"},
        {"l": "Qatar", "v": "Suiza", "fecha": "13/06", "hora": "16:00", "sede": "San Francisco"},
        {"l": "Suiza", "v": "Bosnia y Herzegovina", "fecha": "18/06", "hora": "16:00", "sede": "Los Ángeles"},
        {"l": "Canadá", "v": "Qatar", "fecha": "18/06", "hora": "19:00", "sede": "Vancouver"},
        {"l": "Suiza", "v": "Canadá", "fecha": "24/06", "hora": "16:00", "sede": "Vancouver"},
        {"l": "Bosnia y Herzegovina", "v": "Qatar", "fecha": "24/06", "hora": "16:00", "sede": "Seattle"},
    ],
    "Grupo C": [
        {"l": "Brasil", "v": "Marruecos", "fecha": "13/06", "hora": "19:00", "sede": "Nueva Jersey"},
        {"l": "Haití", "v": "Escocia", "fecha": "13/06", "hora": "22:00", "sede": "Boston"},
        {"l": "Brasil", "v": "Haití", "fecha": "19/06", "hora": "21:30", "sede": "Philadelphia"},
        {"l": "Escocia", "v": "Marruecos", "fecha": "19/06", "hora": "19:00", "sede": "Boston"},
        {"l": "Brasil", "v": "Escocia", "fecha": "24/06", "hora": "19:00", "sede": "Miami"},
        {"l": "Marruecos", "v": "Haití", "fecha": "24/06", "hora": "19:00", "sede": "Atlanta"},
    ],
    "Grupo D": [
        {"l": "EE. UU.", "v": "Paraguay", "fecha": "12/06", "hora": "22:00", "sede": "Los Ángeles"},
        {"l": "Australia", "v": "Turquía", "fecha": "13/06", "hora": "01:00", "sede": "Vancouver"},
        {"l": "EE. UU.", "v": "Australia", "fecha": "19/06", "hora": "16:00", "sede": "Seattle"},
        {"l": "Turquía", "v": "Paraguay", "fecha": "19/06", "hora": "00:00", "sede": "San Francisco"},
        {"l": "Turquía", "v": "EE. UU.", "fecha": "25/06", "hora": "23:00", "sede": "Los Ángeles"},
        {"l": "Paraguay", "v": "Australia", "fecha": "25/06", "hora": "23:00", "sede": "San Francisco"},
    ],
    "Grupo E": [
        {"l": "Alemania", "v": "Curazao", "fecha": "14/06", "hora": "14:00", "sede": "Houston"},
        {"l": "Costa de Marfil", "v": "Ecuador", "fecha": "14/06", "hora": "20:00", "sede": "Philadelphia"},
        {"l": "Alemania", "v": "Costa de Marfil", "fecha": "20/06", "hora": "17:00", "sede": "Toronto"},
        {"l": "Ecuador", "v": "Curazao", "fecha": "20/06", "hora": "23:00", "sede": "Kansas City"},
        {"l": "Ecuador", "v": "Alemania", "fecha": "25/06", "hora": "17:00", "sede": "Nueva Jersey"},
        {"l": "Curazao", "v": "Costa de Marfil", "fecha": "25/06", "hora": "17:00", "sede": "Philadelphia"},
    ],
    "Grupo F": [
        {"l": "P. Bajos", "v": "Japón", "fecha": "14/06", "hora": "17:00", "sede": "Dallas"},
        {"l": "Suecia", "v": "Túnez", "fecha": "14/06", "hora": "23:00", "sede": "Monterrey"},
        {"l": "Túnez", "v": "Japón", "fecha": "20/06", "hora": "01:00", "sede": "Monterrey"},
        {"l": "P. Bajos", "v": "Suecia", "fecha": "20/06", "hora": "14:00", "sede": "Houston"},
        {"l": "Túnez", "v": "P. Bajos", "fecha": "25/06", "hora": "20:00", "sede": "Kansas City"},
        {"l": "Japón", "v": "Suecia", "fecha": "25/06", "hora": "20:00", "sede": "Dallas"},
    ],
    "Grupo G": [
        {"l": "Bélgica", "v": "Egipto", "fecha": "15/06", "hora": "16:00", "sede": "Seattle"},
        {"l": "Irán", "v": "N. Zelanda", "fecha": "15/06", "hora": "22:00", "sede": "Los Angeles"},
        {"l": "Bélgica", "v": "Irán", "fecha": "21/06", "hora": "16:00", "sede": "Los Ángeles"},
        {"l": "N. Zelanda", "v": "Egipto", "fecha": "21/06", "hora": "22:00", "sede": "Vancouver"},
        {"l": "Egipto", "v": "Irán", "fecha": "26/06", "hora": "00:00", "sede": "Seattle"},
        {"l": "N. Zelanda", "v": "Bélgica", "fecha": "26/06", "hora": "00:00", "sede": "Vancouver"},
    ],
    "Grupo H": [
        {"l": "España", "v": "Cabo Verde", "fecha": "15/06", "hora": "13:00", "sede": "Atlanta"},
        {"l": "Arabia Saudita", "v": "Uruguay", "fecha": "15/06", "hora": "19:00", "sede": "Miami"},
        {"l": "España", "v": "Arabia Saudita", "fecha": "21/06", "hora": "13:00", "sede": "Atlanta"},
        {"l": "Uruguay", "v": "Cabo Verde", "fecha": "22/06", "hora": "19:00", "sede": "Miami"},
        {"l": "Uruguay", "v": "España", "fecha": "26/06", "hora": "21:00", "sede": "Guadalajara"},
        {"l": "Cabo Verde", "v": "Arabia Saudita", "fecha": "26/06", "hora": "21:00", "sede": "Houston"},
    ],
    "Grupo I": [
        {"l": "Francia", "v": "Senegal", "fecha": "16/06", "hora": "16:00", "sede": "NY/NJ"},
        {"l": "Irak", "v": "Noruega", "fecha": "16/06", "hora": "19:00", "sede": "Boston"},
        {"l": "Francia", "v": "Irak", "fecha": "22/06", "hora": "18:00", "sede": "Philadelphia"},
        {"l": "Noruega", "v": "Senegal", "fecha": "22/06", "hora": "21:00", "sede": "Nueva Jersey"},
        {"l": "Noruega", "v": "Francia", "fecha": "26/06", "hora": "16:00", "sede": "Boston"},
        {"l": "Senegal", "v": "Irak", "fecha": "26/06", "hora": "16:00", "sede": "Toronto"},
    ],
    "Grupo J": [
        {"l": "Austria", "v": "Jordania", "fecha": "16/06", "hora": "01:00", "sede": "San Francisco"},
        {"l": "Argentina", "v": "Argelia", "fecha": "16/06", "hora": "22:00", "sede": "Kansas City"},
        {"l": "Jordania", "v": "Argelia", "fecha": "22/06", "hora": "00:00", "sede": "San Francisco"},
        {"l": "Argentina", "v": "Austria", "fecha": "22/06", "hora": "14:00", "sede": "Dallas"},
        {"l": "Jordania", "v": "Argentina", "fecha": "27/06", "hora": "23:00", "sede": "Dallas"},
        {"l": "Argelia", "v": "Austria", "fecha": "27/06", "hora": "23:00", "sede": "Kansas City"},
    ],
    "Grupo K": [
        {"l": "Portugal", "v": "RD Congo", "fecha": "17/06", "hora": "14:00", "sede": "Houston"},
        {"l": "Uzbekistán", "v": "Colombia", "fecha": "17/06", "hora": "23:00", "sede": "CDMX"},
        {"l": "Portugal", "v": "Uzbekistán", "fecha": "23/06", "hora": "20:00", "sede": "CDMX"},
        {"l": "Colombia", "v": "RD Congo", "fecha": "23/06", "hora": "23:00", "sede": "Guadalajara"},
        {"l": "Colombia", "v": "Portugal", "fecha": "27/06", "hora": "20:30", "sede": "Miami"},
        {"l": "RD Congo", "v": "Uzbekistán", "fecha": "27/06", "hora": "20:30", "sede": "Atlanta"},
    ],
    "Grupo L": [
        {"l": "Inglaterra", "v": "Croacia", "fecha": "17/06", "hora": "17:00", "sede": "Dallas"},
        {"l": "Ghana", "v": "Panamá", "fecha": "17/06", "hora": "20:00", "sede": "Toronto"},
        {"l": "Inglaterra", "v": "Ghana", "fecha": "23/06", "hora": "17:00", "sede": "Boston"},
        {"l": "Panamá", "v": "Croacia", "fecha": "23/06", "hora": "20:00", "sede": "Toronto"},
        {"l": "Panamá", "v": "Inglaterra", "fecha": "27/06", "hora": "18:00", "sede": "NY/NJ"},
        {"l": "Croacia", "v": "Ghana", "fecha": "27/06", "hora": "18:00", "sede": "Philadelphia"},
    ]
}


with tab1:
    st.sidebar.header("Tu Perfil")
    nombre = st.sidebar.text_input("👤 Tu Nombre:")
    st.markdown("### 📝 Completá tus pronósticos")
    
    pronosticos = []

    for grupo, partidos in fixture_completo.items():
        # Cada grupo es un desplegable
        with st.expander(f"📂 {grupo} - ", expanded=(grupo == "Grupo J")):
            
            # Adentro del expander, creamos 2 columnas
            col_izq, col_der = st.columns(2)
            
            for index, p in enumerate(partidos):
                # Repartimos los partidos: los pares a la izquierda, los impares a la derecha
                target_col = col_izq if index % 2 == 0 else col_der
                
                with target_col:
                    # Contenedor visual para cada partido
                    st.caption(f"🏟️ {p['sede']} | {p['fecha']} - {p['hora']} hs")
                    c1, c2, c3, c4, c5 = st.columns([2, 1, 0.4, 1, 2])
                    with c1: st.write(f"**{p['l']}**")
                    with c2: 
                        gl = st.number_input("L", 0, 15, key=f"C_{p['l']}_{p['v']}_{p['fecha']}_L", label_visibility="collapsed")
                    with c3: st.write("x")
                    with c4: 
                        gv = st.number_input("V", 0, 15, key=f"C_{p['l']}_{p['v']}_{p['fecha']}_V", label_visibility="collapsed")
                    with c5: st.write(f"**{p['v']}**")
                    st.divider() # Una línea sutil para separar partidos dentro del cuadro
                
                pronosticos.append({"Grupo": grupo, "Local": p['l'], "Goles L": gl, "Goles V": gv, "Visitante": p['v']})

    if st.button("💾 Guarda tu Pronóstico"):
        if nombre:
            pd.DataFrame(pronosticos).to_csv(f"prode_{nombre.lower()}.csv", index=False)
            st.success(f"¡Prode de {nombre} guardado!")
            st.balloons()
        else:
            st.error("⚠️ Poné tu nombre para identificar el archivo.")



with tab2:
    st.markdown("### 📈 Tabla de Posiciones")
    

    # Lógica de cálculo
    filas_grupos = st.columns(3) # Para mostrar de a 3 grupos por fila
    
    for i, (grupo, partidos_grupo) in enumerate(fixture_completo.items()):
        col_idx = i % 3
        with filas_grupos[col_idx]:
            puntos = {}
            # Inicializar equipos con 0 puntos
            for p in partidos_grupo:
                puntos[p['l']] = 0
                puntos[p['v']] = 0
            
            # Sumar puntos según pronósticos actuales
            for pr in pronosticos:
                if pr['Grupo'] == grupo:
                    if pr['Goles L'] > pr['Goles V']: puntos[pr['Local']] += 3
                    elif pr['Goles V'] > pr['Goles L']: puntos[pr['Visitante']] += 3
                    else: 
                        puntos[pr['Local']] += 1
                        puntos[pr['Visitante']] += 1
            
            # Crear DataFrame estético
            df_tabla = pd.DataFrame(list(puntos.items()), columns=['Equipo', 'Pts']).sort_values(by='Pts', ascending=False)
            
            st.subheader(f"📍 {grupo}")
            st.dataframe(df_tabla, hide_index=True, use_container_width=True)