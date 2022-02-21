
# Red social

print("Bienvenido a Mi Red")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

# Primera interaccón. Solicitamos al usuario que ingrese su nombre, y lo guardamos en una variable de tipo str

nombre = input("Para empezar, dime ¿cómo te llamas?: ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

'''
Segunda interacción. Solicitamos el ingreso del año, y utilizamos este dato para estimar la edad de la persona. 
¿Por qué decimos que solo estamos "estimando" su edad?. ¿Qué ocurre si eliminamos la conversión a tipo 
de dato 'int' de la siguiente línea?
'''

year = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2021-year
print()

'''
Tercera interacción. Solicitamos la estatura, medida en metros. Utilizamos la conversión a 'int', y una 
expresíon para convertir esto a una medida en metros y centímetros
'''

estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides?. Dímelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

#Cuarta interacción. Consultamos cuántos amigos tiene el usuario.

num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))
genero = input("Por favor ingresa tu género ")
telefono = input("Por favor ingresa tu teléfono ")
residencia = input("Por favor ingresa tu lugar de residencia ")
pais_de_nacimiento = input("Por favor ingresa tu pais de nacimiento ")

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido

print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:", nombre)
print("Edad:", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:", num_amigos)
print("Género:", genero)
print("Teléfono:", telefono)
print("Residencia:", residencia)
print("Pais de nacimiento:", pais_de_nacimiento)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Finalmente, solicitamos un mensaje de prueba que sirva para publicar un estado del usuario.

mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Qué piensas hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")

'''
Ahora puedes practicar solicitando más datos al usuario. Solo tienes que usar apropiadamente input() y print()

1. Escribe 3 solicitudes de datos al usuario, por ejemplo sexo, numero de telefono, ciudad donde vive,
pais de nacimiento, direccion, etc. Guarda esos datos en variables del tipo, y finalmente escrí­belos en pantalla
utilizando print. Puedes agregar todas las líneas que necesites.
'''

continuar = True

while continuar:
    escribir_mensaje = str(input("¿Deseas escribir un mensaje? (S/N) "))
    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
            mensaje = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
            print()
            print("--------------------------------------------------")
            print(nombre, "dice:", mensaje)
            print("--------------------------------------------------")
    else:
        continuar = False

print("Gracias por usar Mi Red. ¡Hasta pronto!")
