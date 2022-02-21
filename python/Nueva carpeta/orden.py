# Funciones de orden superior

frase = "Hola estamos inciando la unidad número cuatro"
tokens = frase.split()# split() convierte una cadena de caracteres en una lista desplegable

def caracteres(palabra):
    if len(palabra) > 3: # Esto es mineria de datos, no me interesan palabras como: el, la...
        return True
    
list(filter(caracteres, tokens))
