# %%
import sys
import numpy as np

# Crear un arreglo unidimensional
numeros = [1, 2, 3, 4, 5]
arr = np.array(numeros) # array <> lista 

print("lista:", numeros)
print("lista:", sys.getsizeof(numeros), "bytes")
print("lista:", type(numeros))
print("")
print("array:", arr)
print("array:", sys.getsizeof(arr), "bytes")
print("array:", type(arr))

print("")

# Crear un arreglo bidimensional
numeros_2d = [[1, 2, 3], [4, 5, 6]]
print("Num --> ", numeros_2d[1][2])
arr2d = np.array(numeros_2d)
print("lista 2D:", numeros_2d)
print("lista 2D:", sys.getsizeof(numeros_2d), "bytes")
print("lista 2D:", type(numeros_2d))
print("")
print("array 2D:", arr2d)
print("array 2D:", sys.getsizeof(arr2d), "bytes")
print("array 2D:", type(arr2d))

# %% Ejemplo de funciones de np
import numpy as np

# Crear un arreglo de ceros
zeros = np.zeros((3, 3))
print(zeros)
print("")

# Crear un arreglo de unos
ones = np.ones((2, 2))
print(ones)
print("")
# Crear un arreglo con valores aleatorios
random = np.random.randint((10, 200))
print("Random int --> ", random)
print("")

# Crear un arreglo con valores espaciados uniformemente
# Del 0 al 10 y nos da 5 valores
linspace = np.linspace(0, 10, 5)
print("5 valores del 0-10 --> ", linspace)
# %% Operaciones matemáticas
import numpy as np

# Crear arreglos de ejemplo
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

lista_A = [1, 2, 3, 4]
lista_B = [5, 6, 7, 8]

# Suma de arreglos
suma = a + b
print("suma: ", suma)
# print(lista_A + lista_B) # el operador + concatena las listas
print("")
# Resta de arreglos
resta = a - b
print("resta:", resta)
print("")
# Producto elemento a elemento
producto = a * b
print("prod: ", producto)
print("")
# División elemento a elemento
division = a / b
print("divi: ", division)
print("")
# Producto punto
producto_punto = np.dot(a, b) # 1*5 + 2*6 + 3*7 + 4*8
print(producto_punto)
# %% Estadística
import numpy as np

# Crear un arreglo de ejemplo
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10])

# Calcular la media
mean = np.mean(arr) 
print("Media:     ", mean)

# Calcular la mediana
median = np.median(arr)
print("Mediana:   ", median)

# Calcular la desviación estándar
std_dev = np.std(arr)
print("Desviación:", std_dev)
# %%
