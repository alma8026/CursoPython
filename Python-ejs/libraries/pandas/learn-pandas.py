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
