class Persona:
    
 def __init__(self, nombre, apellido, genero, edad, estatura): # lo que va dentro de los () son los parámetros
     self.__nombre = nombre # Estas son las variables
     self.__apellido = apellido
     self.__genero = genero
     self.__edad = edad
     self.__estatura = estatura
 
 def __str__(self):
     return "Nombre: " + self.__nombre + " Apellido: " + self.__apellido + " Genero: " + self.__genero + " - edad: " + str (self.__edad) + " Estatura: " + str (self.__estatura)
