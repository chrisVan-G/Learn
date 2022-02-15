# Tuplas

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
print(frutas[:])
print(frutas[2:2])
print(frutas[:2])
print(frutas[2:])

# Modificar, no se puede hacer como en las listas
frutas[0] = "Guayaba"
frutaslista = list(frutas)
frutaslista[0] = "Guayaba"
frutas = tuple(frutaslista)
print(frutas)
print(frutas[0])

# las listas son dinamicas y mutables mientras que las tuplas son inmutables
