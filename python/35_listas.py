
# Listas

# Tipo de dato ‘list’
# Una lista es una secuencia de elementos de cualquier tipo y que se encuentran ordenados

'''
lista = [elemento0, elemento1..., elemento-1]
'''

'''
mesa = 7
orden = "Café"
cantidad = 2
costo = 1200
pedido = [mesa, orden, cantidad, costo, cantidad*costo]
print("Mesa|orden|cantidad|v.Unitario|v.Total")
print(pedido) 
'''

# Listas vacias

'''
vacia = []
vacia2 = list()

print(vacia)
print(vacia2)
'''

# Manipulación de listas

'''
compra = ["huevos", "queso", "arepas", "matequilla", "cafe", 15000]
print(compra)

# Adicionar elemento, las listas son mutables(no como str), podemos modificar y acceder a elementos, cada elemento tiene
# una posición o indice que inicia en 0 y termina en -1

print("Por favor no olvidar el", compra[4])
# Podemos acceder a fragmentos o slices
print(compra[1:4])
print(compra[1:4+1])
# lista[inicio:fin:step]
# Desde lista[inicio] hasta lista[fin-1], en pasos de step/posiciones que avanzaremos antes de seleccionar el siguiente elemento 

letras = ["a","b","c","d","e","f","g","h","i","j"]
#         0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 indices

print(letras[2:7])
print(letras[2:7:2])
print(letras[7:])
print(letras[:5:3])
print(letras[2:2])
print(letras[::-1])

# Recorrer una lista 

for elem in compra:
    print("No olvides", elem)

# Podemos modificar los valores de cada posición 

compra[1] = "cuajada"
compra[5] = 20000
print(compra)
'''

# Inserción y eliminación en listas

'''
adicional = ["tomates", "cebolla"]
compra = compra + adicional
print(compra)
print(adicional * 2)
'''

# append agrega un elemento al final de la lista lista.append(elemento), recibe el elemento nuevo a agregar

'''
compra.append("tomates")
print(compra)

# El método extend recibe como parámetro una lista y agrega todos los elementos de ella a la lista sobre la cual
# lo hemos llamado

compra.extend(["cebolla", "jamon"])  
print(compra)

# Agregar elementos en cualquier posición lista.insert(index, elemento), recibe 2 parámetros, el primero
# me pregunta en que posición quiero adicionar el elemento y el segundo es donde va el nuevo elemento

compra.insert(2, "panela")
print(compra)

# Eliminar lista.pop() elimina y retorna el primer elemento, lo eliminado lo entrega como valor de retorno
# por eso se debe almacenar en una variable
# Según la teoria elimina el primer elemento de la lista, en este caso me elimino el último

no_necesario = compra.pop()
print(compra)
print("No necesito llevar", no_necesario)

# remove elimina un elemento de la lista lista.remove(elemento), recibe el elemento como parámetro y 
# lo elimina de la lista 

compra.remove("arepas")
print(compra)

# Funciones sobre listas

print("Hay", len(compra), "cosas por comprar")
print("¿Hay cilintro en mis biberes?", ("ciliantro" in compra))
print("¿Hay huevos en mis biberes?", ("huevos" in compra))
print("Huevos está en la posición", compra.index("huevos")) 
# Sí el elemento no está en la lista genera error y detiene el programa
'''

# De str a lista, método split
'''
print()
lista = input("Por favor ingrese los elementos de la lista: ")
utiles = []
inicio = 0
for i in range(0, len(lista)):
    if lista[i] == ",":
        utiles.append(lista[inicio : i])
        inicio = i+1
utiles.append(lista[inicio:])
print("utiles:", utiles)

# string.split(separador) separa un string lo guarda en una lista
'''

'''
print()
lista = input("Por favor ingrese los elementos de la lista: ")
utiles = lista.split(" ")
print("utiles:", utiles)
'''

frase = "Hola estamos inciando la unidad número cuatro"
tokens = frase.split()# split() convierte una cadena de caracteres en una lista desplegable

def caracteres(palabra):
    if len(palabra) > 3: # Esto es mineria de datos, no me interesan palabras como: el, la...
        return True
    
list(filter(caracteres, tokens))

# Ordenar listas list.sort() ordena de menor a mayor alfabeticamente

'''
precios = [1800, 2300, 450, 610]
print("Original:", precios)
precios.sort()
print("Ordenada:", precios)
print()

comprar = [[11000, "huevos"], [4000, "arepas"], [5000,"queso"], [3500, "tomate"], [2000, "cebolla"]]
print("Original:", comprar)
comprar.sort()
print("Ordenada:", comprar)

nombres = ["Karla", "Johana", "Ivan", "Sofia"]
print(nombres)
# Saber el largo o dimension de la lista
print(len(nombres))
#Seleccionar un elemento
print(nombres[0])
print(nombres[3])
# Navegacion inversa -1, -2, -3,-4 (-1 inicia en el ultimo elemento de la lista y sucesi..)
print(nombres[-2])
# Imprimir un rango
print(nombres[0:2]) # Imprime los dos primeros elementos
print(nombres[3:4])
print(nombres[:]) # Imprime todo
print(nombres[4:4]) # No imprime nada
# Cambiar algun elemento de la lista, teniendo en cuenta la posicion
nombres[3] = "Daniel"
print(nombres)
nombres[0] = "Xiomara"
print(nombres) # Quitamos a Karla para el ejemplo de if-else

# Iterar la lista
for nombre in nombres:
    print(nombre)

# Revisar si el elemento existe dentro de la lista
if "Karla" in nombres:
    print("Karla si se encuentra en la lista")
else:
    print("Karla no se encuentra en la lista")
'''
