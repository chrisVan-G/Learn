
# Ejercicio con dicccionarios

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []

for asignatura in asignaturas:
    nota = float(input("Ingrese la nota de: "+ asignatura + "? "))
    while nota < 0 or nota > 5:
        print("Nota errada, por favor ingrese una nota correcta")
        break
        
    if nota >= 3 and nota <= 5:
        passed.append(asignatura)
        
for asignatura in passed:
    asignaturas.remove(asignatura)
        
print("tienes que repetir: "+ str(asignaturas))

# Pendiente terminarlo
