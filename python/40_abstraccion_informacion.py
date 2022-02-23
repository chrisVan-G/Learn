
# Abstracción de información importante, filtrar informacion de una lista

'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)

personas = [
 Persona("Laura", 15),
 Persona("José", 35),
 Persona("Melissa", 2),
 Persona("Xiomara", 31)
]

menores = filter(lambda persona: persona.edad < 18, personas)

for menor in menores:
    print(menor)
'''

'''
# Conversor de decimal a binario, octal y hexadecimal

def conversor(sis):
    def sis_bin(numero):
        print("dec: ", numero, "bin: ", bin(numero))
    
    def sis_oct(numero):
        print("dec: ", numero, "oct: ", oct(numero))
    
    def sis_hex(numero):
        print("dec: ", numero, "hex: ", hex(numero))
        
    sis_func = {"bin": sis_bin, "oct": sis_oct, "hex": sis_hex}
    return sis_func[sis]

# Se crearon funciones y subfunciones y ahora se va a crear una instancia
# del conversor hexadecimal

conversorhex = conversor("hex")

# Convertir un 100 decimal a hexadecimal

conversorhex(10) # En hexadecimal el número 10 es una 'a'

# Convertir un decimal a binario
conversor("bin")(100)
'''

# Ejercicio de los aviones
# set() se usa para conjuntos que van a ser mutables en el tiempo

# Para escribir el código del ejemplo de los aviones ver el video de la clase 10
# en el punto 1: 30: 24 del video

#avion_con_mayor_uso
vuelosEjemplo = [{"aerolinea": "AVIANCA", 'codigo': "AHF21", "origen": "BOG", "destino":
"CTG", "distancia": 295, "retraso": 5, "duracion": 120, "salida":600},
        {"aerolinea": "VIVAAIR", 'codigo': "VVE01", "origen": "BOG", "destino":
"CTG", "distancia": 295, "retraso": 2, "duracion": 115, "salida":555},
        {"aerolinea": "AVIANCA", 'codigo': "AHF21", "origen": "CTG", "destino":
"BOG", "distancia": 295, "retraso": 15, "duracion": 120, "salida":830},
        {"aerolinea": "VIVAAIR", 'codigo': "VVE01", "origen": "CTG", "destino":
"PEI", "distancia": 325, "retraso": 5, "duracion": 135, "salida":800},
        {"aerolinea": "AVIANCA", 'codigo': "AHF23", "origen": "BOG", "destino":
"CLO", "distancia": 255, "retraso": 25, "duracion": 170, "salida":605},
        {"aerolinea": "VIVAAIR", 'codigo': "VVE01", "origen": "PEI", "destino":
"BOG", "distancia": 220, "retraso": 5, "duracion": 60, "salida":1030},
        {"aerolinea": "AVIANCA", 'codigo': "AHF23", "origen": "CLO", "destino":
"CTG", "distancia": 400, "retraso": 20, "duracion": 160, "salida":1200}]
# calcular los diferentes aviones
aviones = set()
for vuelo in vuelosEjemplo:
    aviones.add(vuelo['codigo'])
    
#alistar en un diccionario calcular el uso de cada avion
miDiccionario = dict()
for avion in aviones:
    miDiccionario[avion] = 0

#realizar la acumulacion de duraciones cada avion del listado de vuelos
mayorDuracion = -1
for avion in aviones:
    for vuelo in vuelosEjemplo:
        if avion == vuelo['codigo']:
            miDiccionario[avion]= miDiccionario[avion] + vuelo['duracion']
        #aprovechar los fors para encontrar el avion con mayor duracion
        if miDiccionario[avion]> mayorDuracion:
            mayorDuracion =miDiccionario[avion]
            avionConMayorDuracion = avion

# preparacion de la tupla de salida
miTupla = (avionConMayorDuracion, miDiccionario[avionConMayorDuracion])

print (miTupla)
