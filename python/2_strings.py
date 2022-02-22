
# Strings (Cadenas de texto)

# Se pueden escribir usando comillas simples('') o dobles("")

'''
Se pueden concatenar usando + o se pueden repetir usando *
Los strings son inmutables, es decir una ve definido el objeto este no cambiará a menos que se defina nuevamente
'''

# Manipulación de strings

print("Martes"[0])
print("Martes"[5])
print("Martes"[-1])
print("Martes"[4])
print("Martes"[-2])

# slicing

print("Martes"[0 : 5])
print("Martes"[0 : 5 + 1]) # Adiciono el +1 ya que en este intervalo el último caracter no está incluido

# Cambios de linea

print("Primer párrafo. \nSegundo párrafo.") # n significa new line y permite hacer una nueva linea

# para escribir un backslash debo escribirlo 2 veces

print("Necesito usar un backslash en mi código \\") # El primero indica caracter especial y el segundo indica el backslash

# Funciones sobre strings

# len abreviación de length/longitud retorna el largo(cantidad de caracteres) del string que se pase como parámetro

print(len("Martes"))
print(len("Test"))

# Pasar todo un string a mayúsculas o minúsculas string.upper() / string.lower()

print("Martes".upper())
print("Martes".lower())

# strip me permite remover simbolos de los extremos, requiere el elemento a remover como parámetro

a = "string de prueba para el uso de strip." # Solo podemos remover lo de los extremos
print(a.strip("."))
print(a.strip("s"))

# replace cuyos parámetros deben ser el simbolo o caracter antiguo y el nuevo

b = "Hola!1!"
print(b.replace("1", "!"))


'''
mensaje = "Hola"
mensaje += " "
mensaje += "Chris"
print(mensaje)
'''

'''
saludo = "Hola"
espacio = " "
nombre = "Eliana"
print(saludo + espacio + nombre) 
'''

'''
numero_uno = 45
numero_dos = 50
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado es: " + resultado)
'''
