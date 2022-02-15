#usuario_activos={1:["Pepe", "Perez", 1020433000, 20, "MAÑANA"], 2:["Tony", "Torrez", 1020433001, 23, "TARDE"], 3:["Lola", "Lara", 1020433002, 28, "NOCHE"], 4:["Donald", "Duck", 1020433003, 36, "MAÑANA"], 5:["Mickey", "Mouse", 1020433004, 42, "TARDE"], 6:["Bugs", "Bunny", 1020433005, 45, "NOCHE"]}

class Usuarios():
    def __init__(self, nombre, apellido, identificacion, edad, jornada):
        #self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        self.edad = edad
        self.jornada = jornada
    
    '''
    def listaUsuarios(self):
        print("Base de datos de todos los usuarios de BOX GYM")
        print("---------------------------------")
        print('Nombre: ', self.nombre)
        print('Apellido: ',self.apellido)
        print('Identificación:', self.identificacion)
        print('Edad: ',self.edad)
        print('Jornada: ',self.jornada)
        #print(usuario_activos.listaUsuarios())
        print("---------------------------------")
    '''
# Imprimir la cantidad de usuarios que hay por rango de edad
    def box_gym(self):
        print("Rango de edades del BOX GYM \n")
        contadorEdad18_22 = 0
        contadorEdad23_27 = 0
        contadorEdad28_32 = 0
        contadorEdad33_37 = 0
        contadorEdad38_42 = 0
        contadorEdadMayores = 0
    
        for self.edad in :
            if self.edad >= 18 and self.edad >= 22:
                contadorEdad18_22 += 1
                print(contadorEdad18_22)
            elif self.edad >= 23 and self.edad >= 27:
                contadorEdad23_27 += 1
                print(contadorEdad23_27)
            elif self.edad >= 28 and self.edad >= 32:
                contadorEdad28_32 += 1
                print(contadorEdad28_32)
            elif self.edad >= 33 and self.eda >= 37:
                contadorEdad33_37 += 1
                print(contadorEdad33_37)
            elif self.edad >= 38 and self.edad >= 42:
                contadorEdad38_42 += 1
                print(contadorEdad38_42)
            else:
                contadorEdadMayores += 1
                print(contadorEdadMayores)           
        print("---------------------------------")

# Imprimir el listado de usuarios completo
    def listaUsuarios(self):
        print("Base de datos de todos los usuarios de BOX GYM")
        print("---------------------------------")
        print('Nombre: ', self.nombre)
        print('Apellido: ',self.apellido)
        print('Identificación:', self.identificacion)
        print('Edad: ',self.edad)
        print('Jornada: ',self.jornada)
        print("---------------------------------")
'''
#usuario_activos={1:["Pepe", "Perez", 1020433000, 20, "MAÑANA"], 2:["Tony", "Torrez", 1020433001, 23, "TARDE"], 3:["Lola", "Lara", 1020433002, 28, "NOCHE"], 4:["Donald", "Duck", 1020433003, 36, "MAÑANA"], 5:["Mickey", "Mouse", 1020433004, 42, "TARDE"], 6:["Bugs", "Bunny", 1020433005, 45, "NOCHE"]}
'''
# Creación objeto

usuario1 = Usuarios("Pepe", "Perez", 1020433000, 20, "MAÑANA")
usuario2 = Usuarios("Tony", "Torrez", 1020433001, 23, "TARDE")
usuario3 = Usuarios("Lola", "Lara", 1020433002, 28, "NOCHE")

usuario1.listaUsuarios()
usuario2.listaUsuarios()
usuario3.listaUsuarios()

usuario1.box_gym()
usuario2.box_gym()
usuario3.box_gym()
'''
# Ingresar como listas

lista1 = Usuarios(["Pepe", "Perez", 1020433000, 20, "MAÑANA"], ["Tony", "Torrez", 1020433001, 23, "TARDE"], ["Lola", "Lara", 1020433002, 28, "NOCHE"])
lista1.listaUsuarios()
'''