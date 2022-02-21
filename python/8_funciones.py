
# Funciones

# Una función recibe parámetros, ejecuta acciones y retorna un resultado

# Elementos de una función
# Tener presente al usar return en una función que al ejecutarse el return las lineas de código que continuen como un print no se ejecutarán

numero = int(input("Por favor ingrese un número: "))

'''
def calculo(numero):
    resultado = (numero - 3) ** 3
    return  resultado

print("El resultado del calculo es", calculo(numero))
salida = calculo(numero)
print("El resultado del calculo es", salida)

'''

# Definición de funciones

# Las funciones comienzan con def nombreFuncion(parámetros) puede o no llevar parámetros

'''
def nombreFuncion(parámetros):
    instrucciones(Código, puede tener o no retorno)
    debe ir identado
'''

# Invocación de funciones y scope

def cuenta(tope):
    i = 0
    while i < tope:
        print(i)
        i += 1

cuenta(3)

# scope las variables definidas dentro de una función, no existen fuera de ella

# Funciones como módulos



'''
total = 3
unidad = "días"
for i in range(total):
    print("Han pasado", str(i), unidad)
print("---------------------------------")

total = 3
unidad = "meses"
for i in range(total):
    print("Han pasado", str(i), unidad)
print("---------------------------------")

total = 13
unidad = "meses"
for i in range(total):
    print("Han pasado", str(i), unidad)
print("---------------------------------")

'''

'''
def mi_funcion():
    print ("Se está ejecutando la función")

mi_funcion()
'''

'''
x = range(0,5) # Devuelve los numeros del 0 - 5
print(x)
print(len(x))
'''

# Crear una función:

'''
def func(parámetro1, parámetro2):
    # código de la función <-- Identación
    return

# Llamar la función:
func(argumento1, argumento2)

# Almacenar el retorno de la función (si tiene uno):
variable = func(argumento1, argumento2)
'''

'''
def imprime_Cosas():
    print("La clase esta genial")   
    print('Python es lo máximo')
    print("----------------------------------------")
        
def repetir_funciones():
    imprime_Cosas()
    imprime_Cosas()

repetir_funciones()
'''

'''
def otra_suma(numero1, numero2):
    print(numero1 + numero2)

resultado = otra_suma(5, 7)
print(resultado)
'''

'''
def otra_suma(numero1, numero2):
    print(numero1 + numero2)
    print("----------------------------------")
    print("\n")
    print("----------------------------------")
    return numero1 + numero2    
resultado = otra_suma(5,8) 
print(resultado)
'''

'''
def mi_funcion(nombre, apellido): 
    nombre_completo = nombre, apellido 
    print(nombre_completo)

mi_funcion('Christian', 'Vanegas')
'''

'''
def saludar(nombre, mensaje='Hola'): 
    print(mensaje, nombre)

saludar('Christian') # Imprime: Hola Christian
'''

'''
def saludar(mensaje, nombre): 
    print(mensaje, nombre)

saludar(mensaje="Buen día", nombre="Juancho")
saludar("Buen día", "Juancho")
'''
