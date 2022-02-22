
# Recuperando información

'''
Para abrir archivos en python debo usar la palabra open y le damos como parámetro el nombre del archivo
incluyendo la terminación después del punto
a = open("01_python.py")
'''

# Requiere de un segundo parámetro, si queremos leer("r"/read) o escribir("w"/write)
# Si no se entrega el segundo parámetro, python asume que vamos a leer

# Para leer el archivo se debe llamar al método read sobre la variable que guarda al objeto open

lectura = open("01_python.py", "r")
leer = lectura.read()
print(leer)

# Si el archivo es muy grande y solo necesitamos leer un fragmento o linea ponemos usar .readline(), cada vez
# que se llama a la función, esta lee la siguiente línea

leer = lectura.readline()
print(leer)
leer2 = lectura.readline()
print(leer2)

# Guardando información

# Para escribir abrimos el modo "w", Cuidado: si el archivo existe se borrará para crear uno nuevo
# Usamos el método write() y le pasamos como parámetro lo que vamos a escribir en el archivo

escritura = open("nuevoFichero.txt", "w")
escritura.write("Esto es una prueba de escritura en nuevoFichero")

# Para escribir más lineas se deben indicar los altos de línea

escritura.write("Uno \nDos \nTres")

# Similiar a open existen la función close, debe llamarse una vez terminado el trabajo.

nuevoFichero.close() # close no toma parámetros

