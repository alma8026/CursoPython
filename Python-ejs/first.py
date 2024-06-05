hola='texto asdasdasd'

print('text: ' + hola)

if 5>2 and 4>5: 
    print('e verda') 
else: 
    print('no')

if 5>2 or 4>5: 
    print('e verda') 
else: 
    print('no')
# holaasd asdas d asd asd asd sad asd asd asd ds s
"""asdasd"""
fols = False
tru = True
def a():
    if fols==False: return 'hola'
myvar__var = a()
print(myvar__var)

a = "Hello, Worlda!"
print(len(a))

txt = "The best things in life are free!"
if "caca" in txt or "culo" in txt:
    print('no diga eso')
else:
    print('todo perfe')
    print('.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-')

b = "Hello, World!"
print(b[-5:-2])

a = " Hello, World!  "
print(a.strip())
print(a.replace("H", "J"))

lista = [1, 2, 3, 4]

for num in lista:
    print(num)
print('bucle con indice')
for i, num in enumerate(lista):
    print(i, '-->' ,num)

print('del 1 al 10 with range:')

for i in range(1, 11):
    print(i)

# lista vs tupla
lista = [1, 2, 3, (1, 2, 3)]
tupla = (1, 2, 3, 'waos')
print('LISTA --> son del mismo tipo y se puede añadir')
print(lista)
# añado el 4
lista.append(4)
print(lista)
lista[3] = (1,2)
print(lista)
print('TUPLA --> suelen ser de diferente tipo y no se puede añadir')
print(tupla)

# ---------------------------
usuario = {
    "nombre": "Alejandro",
    "apellidos": "Martínez Aláez",
    "id": 20
}
print("iterar el dict:")
for k, v in usuario.items():
    print(type(k), "-->", v)
# ---------------------------

print(usuario["id"])
# No repite datos del mismo tipo
mi_set = {1, 2, 3, 4, 1, 1, '1'}
print(mi_set)
mi_set.add(6)
print(mi_set)

# Ejemplo con países para no repetir datos
paises = ["España", "UK", "Venezuela", "Antártida", "España", "Demacia"]
paises_set = set(paises)
print(paises_set)

# Frozenset
mi_set_inmutable = frozenset({1, 'inmutable', 3})
print(mi_set_inmutable)

# Boolean
es_admin = True
no_es_admin = False

python_mola = True
JS_mola = False

resultado = python_mola and JS_mola
resultado_2 = not (python_mola or JS_mola)

print(resultado)
print(resultado_2)

 # representación binaria del entero
print(format(1, '032b'))
print(format(2, '032b'))
print(format(3, '032b'))
print(bin(1))

# Cuando no se sepa el valor de algo se pone None
valor_unknown = None
bool(None) # mapea a False