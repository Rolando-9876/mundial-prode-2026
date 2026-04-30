import pandas as pd

archivo = "fixture Mundial.xlsx" # Asegurate de que el nombre sea el correcto
df = pd.read_excel(archivo)

# Seleccionamos solo las columnas que tienen los partidos del fixture
# .iloc permite elegir columnas por su número de posición (empezando de 0)
fixture = df.iloc[:, [1, 2, 3, 4, 5]] 

# Le ponemos nombres humanos a esas columnas
fixture.columns = ['Grupo', 'Local', 'Goles_L', 'Goles_V', 'Visitante']

# Borramos las filas que están totalmente vacías (NaN)
fixture = fixture.dropna(subset=['Local', 'Visitante'])

print("--- FIXTURE LIMPIO ---")
print(fixture.head(10))