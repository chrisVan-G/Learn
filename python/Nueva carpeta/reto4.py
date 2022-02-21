
def box_gym(numero: int, nombre: str, apellido: str, identificacion: str, edad: str, jornada: str):
    usuarios[numero] = [nombre, apellido, identificacion, edad, jornada]
    return usuarios
    #print("Rango de edades del BOX GYM \n")
    #print("---------------------------------")

def listaUsuarios(): 
    print("Base de datos de todos los usuarios de BOX GYM") 
    print("---------------------------------")
    for datos in usuarios.items():
        print("-Nombre:", nombre[0])
        print("-Apellido:", apellido[1])
        print("-Identificacion:", identifciacion[2])
        print("-Edad:", edad[3])
        print("-Jornada:", jornada[4])
    print("---------------------------------")

usuarios = {1:["Pepe", "Perez", 1020433755, 30, "NOCHE"]}
# Listas
'''listaEdad18_22 = []
listaEdad23_27 = []
listaEdad28_32 = []
listaEdad33_37 = []
listaEdad38_42 = []
listaEdadMayores = []'''
