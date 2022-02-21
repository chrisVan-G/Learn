def estudiante (nota1: float, nota2: float, nota3: float, nota4: float,)-> str:    
    
    promedioDato1 = nota1 * 0.3  # La nota 1 es multiplicada por el porcentaje asociado (30%)
    promedioDato2 = nota2 * 0.25 # La nota 2 es multiplicada por el porcentaje asociado (25%)
    promedioDato3 = nota3 * 0.25 # La nota 3 es multiplicada por el porcentaje asociado (25%)
    promedioDato4 = nota4 * 0.2  # La nota 4 es multiplicada por el porcentaje asociado (20%)
    promedioTotal = promedioDato1 + promedioDato2 + promedioDato3 + promedioDato4
    
    return "El promedio del estudiante es de: {} " .format(promedioTotal, nota1, nota2, nota3, nota4)

    nota1 = float(input("Ingrese el valor obtenido por el/la estudiante en la nota de seguimiento: "))
    nota2 = float(input("Ingrese el valor obtenido por el/la estudiante en la nota del parcial número 1: "))
    nota3 = float(input("Ingrese el valor obtenido por el/la estudiante en la nota del parcial número 2: "))
    nota4 = float(input("Ingrese el valor obtenido por el/la estudiante en la nota del trabajo final: "))
    
    print(estudiante(nota1, nota2, nota3, nota4))
 