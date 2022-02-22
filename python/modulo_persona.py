
# Modulo persona

class Persona:
    
 def __init__(self, nombre, apellido, genero, edad, estatura): # lo que va dentro de los () son los parámetros
     self.__nombre = nombre # Estas son las variables
     self.__apellido = apellido
     self.__genero = genero
     self.__edad = edad
     self.__estatura = estatura
 
 def __str__(self):
     return "Nombre: " + self.__nombre + " apellido: " + self.__apellido + " genero: " + self.__genero + " - edad: " + str (self.__edad) + " estatura: " + str (self.__estatura)

# random es un modulo que permite generar pseudoaleatorios
# math es un modulo que permite realizar calculos complejos y acceder a constantes conocidas
