
# Importación y llamado de módulos

from modulo_persona import Persona

print()

nombre = input("Ingrese su nombre por favor: ")
apellido = input("Ingrese su apellido por favor: ")
genero = input("Ingrese su genero por favor: ")
edad = int(input("Ingrese su edad por favor: "))
estatura = float(input("Ingrese su estatura por favor: "))

print()
print("-----------------------------------------------------")

'''
p1 = Persona("Johan", "Perez", "M", 33, 1.65)
print(p1)
'''
p1 = Persona(nombre, apellido, genero, edad, estatura)
print(p1)
p2 = Persona("Sara", "Lopez", "F", 25, 1.75)
print(p2)
p3 = Persona("Camilo", "Salgado", "M", 19, 1.50)
print(p3)
p4 = Persona("Eliana", "Alvarez", "F", 30, 1.62)
print(p4)
p5 = Persona("Chris", "Van", "M", 28, 1.90)
print(p5)

print("-----------------------------------------------------")
