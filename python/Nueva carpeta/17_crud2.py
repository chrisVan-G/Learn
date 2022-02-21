# Para las variables uso camelCase, para las fucnciones y dicts uso esta_forma

# Cargar e imprimir - CRUD


# para datos compartidos & proceso de insercion
# se pueden hacer uniones, inserciones, diferencias y diferencia simetrica, mirar en 
# las notas

#Un colegio quiere un programa que le permita ingresar un estudiante y 
#luego imprimir todos los estudiantes que estén activos, teniendo en cuenta 
# que el colegio tiene a los siguientes estudiantes ya cargados:

#PASO 3: 
# Creamos la función para cargar el estudiante al diccionario de estudiantes_activos

def cargarEstudiantes(identificacion: int, nombre: str):
    estudiantes_activos[identificacion]=[nombre]
    print("Ha sido cargado con éxito")
    return estudiantes_activos

#Función para imprimir toda la lista

def imprimirListadoEstudiantes(estudiantes):
    for identificacion, datos in estudiantes.items(): # cuando imprimo Items() trae toda la lista
        print("Número es: ",identificacion)
        print("El nombre es: ",datos[0]) # que imprima desde la posicion cero
        print("--------------------------")

# El for me segmenta información
#PASO 1:  creamos un diccionario y agregamos los datos

estudiantes_activos = { 1: ["JUAN ARTURO VELASQUEZ DUQUE"], 2: ["JOHAN MANUEL GORDILLO MESA"], 3: ["XIOMARA POSADA FERNANDEZ"]}

#PASO 2: Crear nuevas variables para el id y nombre, para almacenar a un diccionario

print("-----------------------------------")
print("Cargar estudiantes")

indentificacionEstudiante = int(input("Digite el ID del estudiante: "))
nombreEstudiante = str(input("Digite el nombre del estudiante: "))
estudiantes_activos = cargarEstudiantes(indentificacionEstudiante, nombreEstudiante)

# PASO 4 Imprimir el listado de todos los estudiantes

print(imprimirListadoEstudiantes(estudiantes_activos))
# Si pongo un id ya existente reemplaza el anterior 

# Eliminar - CRUD

'''
#PASO 3 - Creamos las facciones que vamos a usar
#Funcion que se usa para cargar un estudiante a los estudiantes_activos

def cargarEstudiante(identifiacion: int, nombre: str):
    estudiantes_activos[identifiacion]=[nombre]
    print ("*Estudiante ingresado con exito*")
    return estudiantes_activos

#Funcion que eliminar estudiante
def numeroEstudiantes(estudiantes, nombre):
    for identifiacion,datos in estudiantes.items():
        if datos[0].lower()==nombre.lower():
            return identifiacion
    return 0

#Funcion que se usa para imprimir a todos los estudiantes
def imprimirListadoEstudiantes(estudiantes):
    for identifiacion,datos in estudiantes.items():
        print("-Número:",identifiacion)
        print("-Nombre:",datos[0])
        print ("---------------------------------")

#PASO 1 - Creamos el diccionario y se rellana con los datos
estudiantes_activos={1:["JUAN ARTURO VELASQUEZ DUQUE"], 2:["KEVIN JHOAN ALVIS GOMEZ"], 3:["NATALIA CLAVIJO PINZON"]}

#PASO 2 - Creamos una variable para identificar el estudiante que sera eliminado
print("Eliminar Estudiante")
eliminarEstudiante = int (input ("Ingrese id del estudiante a eliminar: ")) #variable para identificar el id
nombreEstudiante = estudiantes_activos[eliminarEstudiante][0] #variable para guardar el nombre del usuario que sera eliminado
eliminarEstudiante=numeroEstudiantes(estudiantes_activos, nombreEstudiante) #Procedimiento para eliminar al estudiante
if eliminarEstudiante in estudiantes_activos: #Procedimiento para eliminar al estudiante
    del estudiantes_activos[eliminarEstudiante] #Procedimiento para eliminar al estudiante
else: #Procedimiento para eliminar al estudiante
    print ("El estudiante no se encuentra registrado") #Procedimiento para eliminar al estudiante
    print ("*Estudiante: ", nombreEstudiante, ", eliminado con exito*") #Mensaje ser eliminado el estudiante

#PASO 4 - Damos la orden de imprimir los datos
imprimirListadoEstudiantes(estudiantes_activos) #Imprimir el listado de estudiantes
'''
'''
# modificar - CRUD

#PASO 3 - Creamos las facciones que vamos a usar
#Funcion que se usa para cargar un estudiante a los estudiantes_activos

def cargarEstudiante(identifiacion: int, nombre: str):
    estudiantes_activos[identifiacion]=[nombre]
    print ("*Estudiante ingresado con exito*")
    return estudiantes_activos

#Funcion que se usa para imprimir a todos los estudiantes
def imprimirListadoEstudiantes(estudiantes):
    for identifiacion,datos in estudiantes.items():
        print("-Número:",identifiacion)
        print("-Nombre:",datos[0])
        print ("---------------------------------")

#PASO 1 - Creamos el diccionario y se rellana con los datos
estudiantes_activos={1:["JUAN ARTURO VELASQUEZ DUQUE"], 2:["KEVIN JHOAN ALVIS GOMEZ"], 3:["NATALIA CLAVIJO PINZON"]}

print ("---------------------------------")

#PASO 2 - Creamos una variable para identificar el estudiante que se le hará la modificación el nombre
print("Modificar nombre")
numeroEstudiante= int (input("Ingrese un id del estudiante que quiere modificar: ")) #variable para identificar el id
estudiantes_activos[numeroEstudiante][0]= str (input("Ingrese nuevo nombre: ")) #variable para el nuevo nombre
print ("Estudiante :",estudiantes_activos[numeroEstudiante][0] , ", nombre con exito" ) #Mensaje que confirma que la nombre fue actualizado

print ("---------------------------------")
#PASO 4 - Damos la orden de imprimir los datos
print (imprimirListadoEstudiantes(estudiantes_activos)) #Imprimir el listado de estudiantes
'''