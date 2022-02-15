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

saludar('Christian') # Imprime: Hola Pepe Grillo
'''

def saludar(mensaje, nombre): 
    print(mensaje, nombre)

saludar(mensaje="Buen día", nombre="Juancho")
saludar("Buen día", "Juancho")
