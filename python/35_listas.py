
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

compra = ["huevos", "queso", "arepas", "matequilla", "cafe", 15000]
print(compra)

# Adicionar elemento, las listas son mutables, podemos modificar y acceder a elementos, cada elemento tiene
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

# Inserción y eliminación en listas



'''
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
