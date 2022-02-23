import pandas as pd

def boxGym(ruta):

    datos=pd.read_csv(ruta, header=0)    
    dataFrame=pd.DataFrame(datos) 
    
    i = 0 
    listaEdad18_22 = 0
    listaEdad23_27 = 0
    listaEdad28_32 = 0
    listaEdad33_37 = 0
    listaEdad38_42 = 0
    listaEdadMayores = 0

for x in dataFrame["EDAD"]:
    if dataFrame["EDAD"][i] >= 18 and dataFrame["EDAD"][i] < 23:
        listaEdad18_22 += 1
    elif dataFrame["EDAD"][i] >= 23 and dataFrame["EDAD"][i] < 28:
        listaEdad23_27 += 1
    elif dataFrame["EDAD"][i] >= 28 and dataFrame["EDAD"][i] < 33:
        listaEdad28_32 += 1
    elif dataFrame["EDAD"][i] >= 33 and dataFrame["EDAD"][i] < 38:
        listaEdad33_37 += 1
    elif dataFrame["EDAD"][i] >= 38 and dataFrame["EDAD"][i] < 43:
        listaEdad38_42 += 1
    elif dataFrame["EDAD"][i] >= 43:
        listaEdadMayores += 1
        i += 1    

    diccionarioEdad = {"Edad entre 18 a 22" :listaEdad18_22,"Edad entre 23 a 27" :listaEdad23_27,"Edad entre 28 a 32" :listaEdad28_32,"Edad entre 33 a 37":listaEdad33_37,"Edad entre 38 a 42":listaEdad38_42, "Mayores de 43":listaEdadMayores}

    i = 0
    jornadaMañana = 0
    jornadaTarde = 0
    jornadaNoche = 0
    
    for x in dataFrame['JORNADA']:
        if dataFrame['JORNADA'][i] == 'MAÑANA':
            jornadaMañana += 1
        elif dataFrame['JORNADA'][i] == 'TARDE':
            jornadaTarde += 1
        elif dataFrame['JORNADA'][i] == 'NOCHE':
            jornadaNoche += 1   
        i += 1
                               
    diccionarioJornadas = {"Jornada mañana" :jornadaMañana,"Jornada tarde" :jornadaTarde,"Jornada noche" :jornadaNoche }
    
    return diccionarioEdad,diccionarioJornadas
