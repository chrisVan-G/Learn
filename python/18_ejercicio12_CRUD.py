# CRUD paran cargar modificar y eliminar

# PASO 3: Definir funciones
if actividad_ejecutar == 'crear':
    def cargarEstudiantes(identificacion: int, nombre: str):
        estudiantes_activos[identificacion]=[nombre]
        print("Ha sido cargado con éxito")
        return estudiantes_activos

elif actividad_ejecutar == 'mofificar':

else:
    print(f"La actividad solicitada {actividad_ejecutar} no fue encontrada, por favor digite crear, modificar o eliminar")

def cargarEstudiantes(identificacion: int, nombre: str):
    estudiantes_activos[identificacion]=[nombre]
    print("Ha sido cargado con éxito")
    return estudiantes_activos
                
# Función para imprimir toda la lista

def imprimirListadoEstudiantes(estudiantes):
    for identificacion, datos in estudiantes.items(): 
        print("Número es: ",identificacion)
        print("El nombre es: ",datos[0]) # que imprima desde la posicion cero
        print("--------------------------")


#PASO 1:  creamos un diccionario y agregamos los datos

estudiantes_activos = { 1: ["LALO LANDA"], 2: ["SARA SUAREZ"]}

#PASO 2: Crear nuevas variables para el id y nombre, para almacenar a un diccionario

print("-----------------------------------")
print("Cargar estudiantes")

actividad_ejecutar = input("¿Qué actividad necesita realizar: crear, modificar o eliminar?: ").upper()
'''
indentificacionEstudiante = int(input("Digite el ID del estudiante: "))
nombreEstudiante = str(input("Digite el nombre del estudiante: "))
estudiantes_activos = cargarEstudiantes(indentificacionEstudiante, nombreEstudiante)
'''
'''
# PASO: 4 Imprimir el listado de todos los estudiantes

print(imprimirListadoEstudiantes(estudiantes_activos))
# Si pongo un id ya existente reemplaza el anterior 
'''