
# Ejercicios dicccionarios

'''
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo, Matemáticas, Física, Química, Historia y Lengua) en una lista 
y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
donde <asignatura> es cada una de las asignaturas de la lista.
'''

'''
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for materia in asignaturas:
    print("Yo estudio: " + materia)
'''

#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo, Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> 
# has sacado <nota> donde <asignatura> es cada una de las asignaturas de 
# la lista y <nota> cada una de las correspondientes notas introducidas 
# por el usuario.
#scores = notas    score = nota

'''
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []

for asignatura in asignaturas:
    score = input("Qué nota has sacado en: " + asignatura + "? ") # como no voy a hacer operaciones lo dejo como string
    scores.append(score) # append significa añadir, seria añadir a scores

print("------------------------------------------------------------")
   
for i in range(len(asignaturas)):
    print("en " + asignaturas[i] + " has sacado " + scores[i])    
'''

# Escribir un programa que pregunte al usuario los números ganadores 
# de la lotería primitiva, los almacene en una lista y los muestre por 
# pantalla ordenados de menor a mayor.

'''
loteria = []
for i in range(6):
    loteria.append(int(input("Introduce un número ganador: ")))
loteria.sort() # sort organiza de menor a mayor, sort significa clasiricar

print("------------------------------------------------")

print("Los números ganadores son: " + str(loteria))
'''

# Escribir un programa que almacene en una lista los números del 1 al 10 
# y los muestre por pantalla en orden inverso separados por comas.

'''
numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(1,11):
    print(numeros[-i], end=(","))
'''

'''
numeros = [1,2,3,4,5,6,7,8,9,10]
numeros.reverse() # imprimalos de atras hacia adelante
print(numeros)
'''

'''
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []

for asignatura in asignaturas:
    nota = float(input("Ingrese la nota de: " + asignatura + "? "))
    if nota >= 3:
        passed.append(asignatura)
                
for asignatura in passed:
    asignaturas.remove(asignatura)
        
print("tienes que repetir: "+ str(asignaturas))
'''

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lenguas"]
aprobado = []
reprobado = []

for asignatura in asignaturas: 
    nota = float(input("Ingrese la nota de " + asignatura +": "))
    if nota >= 3 and nota <= 5 :
            aprobado.append(asignatura)
    elif nota < 0 or nota > 5:
            reprobado.append(asignatura)
            print( "Nota fuera de rango.")
for asignatura in aprobado: 
    asignaturas.remove(asignatura)
for asignatura in reprobado: 
    asignaturas.remove(asignatura)
print("Tienes que repetir: " +str(asignaturas))
