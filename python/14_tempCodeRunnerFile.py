diccionario = {"a":10, "b":20}

if diccionario["a"] == diccionario["b"]:
    print("Los números", diccionario["a"], "y", diccionario["b"], "son iguales")

elif diccionario["a"] < diccionario["b"]:
    print("El número", diccionario["a"], "es menor que ", diccionario["b"])

else:
    print("El número", diccionario["b"], "es menor que ", diccionario["a"])