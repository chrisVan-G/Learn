'''
monedas = {'Euro':'€ ', 'Dolar':'$', 'Yen':'¥'}
moneda = input("Ingrese la divisa: ")

if moneda.title() in monedas: # Title sirve para aceptar mayúsculas y minúsculas en lo que ingresan por teclado
    print(monedas[moneda.title()])

else:
    print("La divisa no se encuentra registrada")'''

'''
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su direccion: ")
telefono = input("Ingrese su telefono: ")

persona = {'nombre':nombre, 'edad':edad, 'direccion':direccion, 'telefono':telefono}

print(persona['nombre'],'tiene la edad de', persona ['edad'], 'su direccion es', persona ['direccion'], 'su telefono es', persona ['telefono'])
'''

# Escriba un programa que guarde un diccionario de los precios de las frutas de la tabla, pregunte al 
# usuario por una fruta, la cantidad de kilos que desee llevar y muestre por pantalla el precio a pagar. 
# Si la fruta no esta en el diccionario debe mostar un mensaje de error

'''frutas = {'Pera':2000, 'Manzana':1500, 'Mandarina':1250, 'Banano':800}

pregunta = input("¿Qué fruta desea comprar?: ").title()
kg = int(input("¿Cuántos kilos desea comprar?: "))

if pregunta in frutas:
    print(kg,'kilos de', pregunta,'cuestan', frutas[pregunta]*kg)

else:
    print("Lo sentimos pero la fruta solicitada no está disponible")'''

# Cuando uso title se debe poner en mayúscula la letra con que inicia la palabra del articulo


# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma 
# fecha en formato dd del "mes" del "año"

meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

fecha = input("Introduzca una fecha en formato dd/mm/aa: ")

fecha = fecha.split('/') # split me permite sacar la inforamción de la fecha

print(fecha[0], 'de', meses[int(fecha[1])], fecha[2])


'''diccionario = {"a":10, "b":20}

if diccionario["a"] == diccionario["b"]:
    print("Los números", diccionario["a"], "y", diccionario["b"], "son iguales")

elif diccionario["a"] < diccionario["b"]:
    print("El número", diccionario["a"], "es menor que ", diccionario["b"])

else:
    print("El número", diccionario["b"], "es menor que ", diccionario["a"])'''


# Escribe un programa que responda a un usuario el cual desea comprar un helado y este desea agregar un 
# adiocional
# el helado cuesta 5000 
# adicional de oreo 2000
# adicional kit-Kat 1500
# adicional brownie 1200
# adicional lacazitos 1000
# en caso de no disponer del adicional solicitado el programa debera mostrar por pantalla no tenemos 
# este adicional

'''adicionales = {1:'oreo', 2:'kit-Kat', 3: 'brownie', 4:'lacazitos'}

adicionalSeleccionado = adicionales[4]

precio = 0.00; # Usar (;) es un acuerdo, se debe utilizar cuando algo arranca en cero

helado = 5000;

precioFinal = 0.00;

if (adicionalSeleccionado == "oreo"):
    precio = 2000;

elif (adicionalSeleccionado == "kit-cat"):
    precio = 1500;

elif (adicionalSeleccionado == "brownie"):
    precio = 1200;

elif (adicionalSeleccionado == "lacazitos"):
    precio = 1000;

else:
    print("No tenemos este adicional en nuestro menu")

precioFinal = helado + precio
print("El helado cuesta $", precioFinal)'''

# Hacer un programa que me pida un número y me indique si es positivo, o negativo, y para 0 es nulo.
# Se debe hacer implementando diccionarios
'''
numero = int(input("Digita el número a evaluar: "))

diccionario = {"n": 0}

if numero > diccionario['n']:
    print(f'el numero {numero} es positivo')
    
elif numero < diccionario['n']:
    print(f'el numero {numero} es negativo')

else:
    print(f'el numero {numero} es null')
 '''
# Items() me permite imprimir todo lo que tiene el dict