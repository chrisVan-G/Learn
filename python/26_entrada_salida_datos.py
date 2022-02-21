
# Entrada y salida de datos

# Escribiendo en pantalla. print.

pesos_por_hora = 200
llegada = 20
salida = 22
precio = (salida - llegada) * pesos_por_hora
print("El precio del estacionamiento es de", precio, "pesos")

print("-----------------------------------------------------")

# Con end puedo hacer que el print no me cambie de linea, pero solo lo hace donde uso el end
nombre = input("Ingrese su nombre por favor ")
edad = 31
print("Soy", nombre, end=" ")
print("y tengo", edad, "años")
print("cumplidos")

# Cambiar elseparador de expresiones
print("El tesoro", "está", "en", sep="...")


# Recibiendo datos del usuario. input

'''
resultado = input("Digite un valor: ")
print("El resultado es: ", resultado)
'''
print("-----------------------------------------------------")

saludo = "Hola,"
pregunta = "¿Cómo estas hoy?"
print(saludo, nombre, pregunta)

# input siempre entrega un string por lo que si necesito operar con los datos ingresados debo formatearlos
