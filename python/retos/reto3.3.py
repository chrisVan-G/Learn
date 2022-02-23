def cargarSocios(numero: int, nombre: str, fecha: str, cuota: str):
    usuario_activos[numero]=[nombre, fecha, cuota.lower()]
    print("Ingreso con exito")
    return usuario_activos

def usuarioEliminadoSocio(socios, nombre):
    for numero, datos in socios.items():
        if datos[0].lower()==nombre.lower():
            return numero
    return 0

def formatoFecha(fecha):
    return (fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:])

def imprimirListado(socios):
    for numero, datos in socios.items():
        print("-Número:", numero)
        print("-Nombre:", datos[0])
        print("-Ingresó:", formatoFecha(datos[1]))
        if datos[2] == "cuotaAlDia":
            print("-Estado: Cuota al día")
        else:
            print("-Estado: En deuda")
        print("---------------------------------")
