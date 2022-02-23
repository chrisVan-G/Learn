
# Tuplas

# las listas son dinamicas y mutables mientras que las tuplas son inmutables
# Mientras que las listas van entre [], las tuplas van entre ()

frutas = ("Papaya", "Naranja", "Manzana", "Banana")
print(frutas)

# Largo de una tupla
print(len(frutas))

# Acceder a un elemento
print(frutas[0])
print(frutas[1])

# Navegación inversa
print(frutas[-1])

# Rango
print(frutas[:]) # Esto imprime toda la tupla
print(frutas[2:2]) # No imprime nada
print(frutas[:2]) # imprime las 2 primeras posiciones
print(frutas[2:]) # imprime las últimas 2 posiciones

# Modificar, no se puede hacer como en las listas
frutas[0] = "Guayaba"

# Para modificar una tupla primero debo convertirla a una lista, hacer el cambio y nuevamente convertirla en una tupla
frutaslista = list(frutas)
frutaslista[0] = "Guayaba"
frutas = tuple(frutaslista)
print(frutas)
print(frutas[0])
