def circuit1(expresion):
    while expresion:
        if len(chars) > 1:
            if expresion[0] == "a" and expresion[1] == "a":
                expresion.pop(0)
                expresion.pop(0)
            elif expresion[0] == "b":
                expresion.pop(0)
                pass
            else:
                break
        else:
            if expresion[0] == "b":
                expresion.pop(0)
                pass
            else:
                break
    return False

def circuit2(expresion):
     if circuit1(expresion) == False:
        while expresion:
            if len(expresion) > 1:
                if expresion[0] == "b" and expresion[1] == "b":
                    expresion.pop(0)
                    expresion.pop(0)
                elif expresion[0] == "a":
                    expresion.pop(0)
                    pass
                else:
                    return False
            else:
                if expresion[0] == "a":
                    expresion.pop(0)
                    pass
                else:
                    return False
                
     else:
         return True
                
     

expresion = str(input("Ingrese una cadena de expresiones: "))
chars = list(expresion)
print(circuit2(chars))
