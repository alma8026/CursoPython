# numero maximo
def example_max():
    maximum = max(1, 2, 3, 4, 7)
    mis_numeros = [1, 2, 3]
    num_maximo = max(mis_numeros)
    assert maximum == 7
    assert num_maximo == 3

# vvv---------- Dia 06/06/24 ----------vvv

def calcular_maximo(a: int, b: int) -> int:
    """
Funcion para calcular el máximo número
{param} a: int
{param} b: int
return --> int/ints
"""
    # "pass" para ignorar y seguir
    if a>b:
        return a
    elif a==b:
        return a, b
    else:
        return b
    
calcular_maximo(121, 121)

# %%
r_1 = calcular_maximo(1, 2)
r_2 = calcular_maximo('1', '2')

# assert para comprobar funciones que no fallen
assert r_1 == 2
assert r_2 == '2'
# %%
