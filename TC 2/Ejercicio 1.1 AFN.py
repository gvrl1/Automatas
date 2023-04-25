def circuit(expresion):
    for i in expresion:
        if i == "a":
            continue
        elif i == "b":
            continue
        elif i == ' ':
            continue
        else:
            return False
    return True   
expresion = str(input("Ingrese una cadena de expresiones: "))
print(circuit(expresion))