import pandas as pd

from itertools import combinations

# 1. Definimos los 12 grupos del Mundial 2026
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

# 2. Nuestra función estrella (ya corregida)
def generar_partidos(lista_equipos, nombre_grupo):
    partidos = []
    for local, visitante in combinations(lista_equipos, 2):
        partidos.append({
            "Grupo": nombre_grupo,
            "Local": local,
            "Visitante": visitante,
            "Goles_L": 0,
            "Goles_V": 0
        })
    return partidos

# 3. Generamos TODO el fixture
todo_el_fixture = []

for nombre_grupo, equipos in grupos_2026.items():
    partidos_del_grupo = generar_partidos(equipos, nombre_grupo)
    todo_el_fixture.extend(partidos_del_grupo)

print(f"✅ ¡Éxito! Se generaron {len(todo_el_fixture)} partidos para la Fase de Grupos.")

# Mostramos los últimos 3 para chequear el Grupo L
print("\nÚltimos partidos generados:")
for p in todo_el_fixture[-3:]:
    print(f"{p['Grupo']}: {p['Local']} vs {p['Visitante']}")