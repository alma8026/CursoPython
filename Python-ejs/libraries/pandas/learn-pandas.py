# %%
import pandas as pd

# Leer un archivo CSV
df = pd.read_csv('../../../../../vehicles.csv')

print(df.head())  # Mostrar las primeras 5 filas del DataFrame
print("")

# columnas:
print("Columnas:")
print(df.columns)
# %%
import pandas as pd

df = pd.read_csv('../../../../../vehicles.csv') # todas las filas y cols del CSV original -> 1.45Gb

# Crear una copia del DataFrame con las 10 primeras filas
df_copia = df.head(10).copy()

# Guardar en otro CSV:
# mechatroner.rainbow-csv CSV Rainbow para visualizar columna por colores
df_copia.to_csv("vehicles_acortado.csv", index=False) 

# %%
import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria', 'Juan'],
    'Edad': [20, 24, 22, 32, 30],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Madrid']
}
df = pd.DataFrame(data)

# Agrupar por la columna 'Ciudad' y calcular la edad promedio:
df_agrupado = df.groupby('Ciudad')['Edad'].mean()

print(df_agrupado)
# %%
