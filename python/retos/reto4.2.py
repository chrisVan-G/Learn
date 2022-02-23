def box_gym(usuarios):
        
        listaEdad18_22 = 0
        listaEdad23_27 = 0
        listaEdad28_32 = 0
        listaEdad33_37 = 0
        listaEdad38_42 = 0
        listaEdadMayores = 0
    
        for identificacion, datos in usuarios.items() :
            if datos[3] >=18 and datos[3]<23:
                listaEdad18_22 += 1
            elif datos[3] >=23 and datos[3]<28:
                listaEdad23_27 += 1
            elif datos[3] >=28 and datos[3]<33:
                listaEdad28_32 += 1
            elif datos[3] >=33 and datos[3]<38:
                listaEdad33_37 += 1
            elif datos[3]>=38 and datos[3]<43:
                listaEdad38_42 += 1
            else:
                listaEdadMayores += 1

        print("Rango de edades del BOX GYM \n"
            "Entre 18 a 22: ", listaEdad18_22," usuario\n"
            "Entre 23 a 27: ", listaEdad23_27," usuario\n"
            "Entre 28 a 32: ", listaEdad28_32," usuario\n"
            "Entre 33 a 37: ", listaEdad33_37," usuario\n"
            "Entre 38 a 42: ", listaEdad38_42," usuario\n"
            "Mayores 42: ", listaEdadMayores," usuario")
        print("---------------------------------")

def listaUsuarios(usuarios):
        print("Base de datos de todos los usuarios de BOX GYM")
        print("---------------------------------")
        for identificacion, datos in usuarios.items():
            print(
            "Nombre:         ",datos[0],"\n"
            "Apellido:       ",datos[1],"\n" 
            "Identificacion: ",datos[2],"\n" 
            "Edad:           ",datos[3],"\n"
            "Jornada:        ",datos[4])
            print("---------------------------------")
