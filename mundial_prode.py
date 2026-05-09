import streamlit as st
import pandas as pd
from st_supabase_connection import SupabaseConnection

st.set_page_config(page_title="Prode Mundial 2026", page_icon="⚽", layout="wide")

# --- CONEXIÓN A BASE DE DATOS (SUPABASE) ---
conn = st.connection(
    "supabase",
    type=SupabaseConnection,
    url="https://nbkurjpyrddrlohwissv.supabase.co",
    key="sb_publishable_jrhXeor3kuLa6m5VqtEEtw_JbtTHD5G"
)

# --- LÓGICA DE SESIÓN ---
if 'usuario' not in st.session_state:
    st.session_state.usuario = None

def login_registro():
    st.title("🏆 Prode Mundial 2026")
    st.markdown("### Registrate para empezar a jugar con tus amigos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔑 Ingresar")
        u_login = st.text_input("Usuario", key="u_login").lower().strip()
        p_login = st.text_input("Contraseña", type="password", key="p_login")
        if st.button("Entrar"):
            # Buscamos al usuario en la tabla
            res = conn.query("*", table="usuarios", ttl=0).eq("nombre", u_login).eq("password", p_login).execute()
            if res.data:
                st.session_state.usuario = u_login
                st.rerun()
            else:
                st.error("Usuario o clave incorrectos")

    with col2:
        st.subheader("📝 Registrarse")
        u_reg = st.text_input("Nuevo Usuario", key="u_reg").lower().strip()
        p_reg = st.text_input("Nueva Contraseña", type="password", key="p_reg")
        if st.button("Crear Cuenta"):
            if u_reg and p_reg:
                try:
                    conn.table("usuarios").insert({"nombre": u_reg, "password": p_reg, "puntos": 0}).execute()
                    st.success("¡Cuenta creada con éxito! Ahora ya podés ingresar.")
                except:
                    st.error("El usuario ya existe o hubo un error.")
            else:
                st.warning("Completá todos los campos.")

# --- PROGRAMA PRINCIPAL ---
if st.session_state.usuario is None:
    login_registro()
else:
    st.sidebar.title(f"⚽ Hola, {st.session_state.usuario.capitalize()}")
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.usuario = None
        st.rerun()

    tab1, tab2, tab3 = st.tabs(["📅 Cargar Pronósticos", "📊 Posiciones Grupos", "🏆 Ranking General"])

    # --- FIXTURE COMPLETO (72 PARTIDOS) ---
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
        st.markdown(f"### 📝 Tus Pronósticos")
        st.info("Cargá tus resultados y dale al botón de abajo para guardar en la nube.")
        
        mis_pronosticos = []
        for grupo, partidos in fixture_completo.items():
            with st.expander(f"📂 {grupo}", expanded=(grupo == "Grupo J")):
                col_izq, col_der = st.columns(2)
                for i, p in enumerate(partidos):
                    target_col = col_izq if i % 2 == 0 else col_der
                    with target_col:
                        st.caption(f"🏟️ {p['sede']} | {p['fecha']} - {p['hora']} hs")
                        c1, c2, c3, c4, c5 = st.columns([2, 1, 0.4, 1, 2])
                        with c1: st.write(f"**{p['l']}**")
                        with c2: gl = st.number_input("L", 0, 15, key=f"L_{p['l']}_{p['v']}_{p['fecha']}", label_visibility="collapsed")
                        with c3: st.write("x")
                        with c4: gv = st.number_input("V", 0, 15, key=f"V_{p['l']}_{p['v']}_{p['fecha']}", label_visibility="collapsed")
                        with c5: st.write(f"**{p['v']}**")
                        st.divider()
                        mis_pronosticos.append({"Grupo": grupo, "Partido": f"{p['l']} vs {p['v']}", "L": gl, "V": gv, "Local": p['l'], "Visitante": p['v']})

        if st.button("💾 Guardar mis Predicciones"):
            with st.spinner("Subiendo a la base de datos..."):
                for pr in mis_pronosticos:
                    conn.table("predicciones").upsert({
                        "usuario_nombre": st.session_state.usuario,
                        "partido": pr["Partido"],
                        "goles_l": pr["L"],
                        "goles_v": pr["V"],
                        "grupo": pr["Grupo"]
                    }).execute()
                st.success("¡Datos guardados con éxito!")
                st.balloons()

    with tab2:
        st.markdown("### 📊 Posiciones Proyectadas")
        filas_pos = st.columns(3)
        for i, (grupo, partidos) in enumerate(fixture_completo.items()):
            with filas_pos[i % 3]:
                puntos = {p['l']: 0 for p in partidos}
                puntos.update({p['v']: 0 for p in partidos})
                # Calculamos con los datos actuales de la pantalla
                for pr in mis_pronosticos:
                    if pr['Grupo'] == grupo:
                        if pr['L'] > pr['V']: puntos[pr['Local']] += 3
                        elif pr['V'] > pr['L']: puntos[pr['Visitante']] += 3
                        else:
                            puntos[pr['Local']] += 1
                            puntos[pr['Visitante']] += 1
                df_t = pd.DataFrame(list(puntos.items()), columns=['Equipo', 'Pts']).sort_values(by='Pts', ascending=False)
                st.subheader(f"📍 {grupo}")
                st.table(df_t)

    with tab3:
        st.header("🏆 Ranking de Amigos")
        st.info("Aquí verás quién va ganando a medida que carguemos los resultados reales.")
        try:
            res_ranking = conn.query("nombre, puntos", table="usuarios", ttl=0).order("puntos", desc=True).execute()
            if res_ranking.data:
                df_ranking = pd.DataFrame(res_ranking.data)
                df_ranking.columns = ["Usuario", "Puntos Totales"]
                st.dataframe(df_ranking, use_container_width=True, hide_index=True)
            else:
                st.write("Todavía no hay jugadores registrados.")
        except:
            st.error("Error al cargar el ranking.")