'''nombres = ["Karla", "Johana", "Ivan", "Sofia"]
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
# Cmabiar algun elemento de la lista, teniendo en cuenta la posicion
nombres[3] = "Daniel"
print(nombres)
nombres[0] = "Xiomara"
print(nombres)# Quitamos a Karla para el ejemplo de if-else
# Iterar la lista
for nombre in nombres:
    print(nombre)
# Revisar si el elemento existe dentro de la lista
if "Karla" in nombres:
    print("Karla si se encuentra en la lista")
else:
    print("Karla no se encuentra en la lista")'''

nombres = ["Karla", "Johana", "Ivan", "Sofia"]
print(nombres)
#sabe el largo o dimensión de la lista
print(len(nombres))
#seleccionar un elemento de la lista
print( nombres[0])
#navegación inversa
print(nombres[-2])
#imprimir un rango
print(nombres[4:4])
#cambiar algún elemento de la lista, teniendo en cuenta
#la posición 
nombres[3] = "Daniel"
print(nombres)
nombres[0] = "Xiomara"
print(nombres)
#iterar la lista
for nombre in nombres:
    print(nombre)
#revisar si el elemento existe dentro de la lista

if "Karla" in nombres:
    print("Karla si se encuentra en la lista")
else:
    print("Karla no se encuentra en la lista")
 