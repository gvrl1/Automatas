#Ejercicio 2 - Aldana G. Moreno y Dante Illesca.

def solve(string: str):
    chr = string.split("+")
    for i in range(0, len(chr)):
        chr2 = chr[i]
        if "*" in chr2:
            m = chr2
            num = m.split("*")
            num = [int(x) for x in num]
            r2 = 1
            for chr2 in num:
                r2 *= chr2
            chr[i] = r2
        else:
            continue
    chr = [int(x) for x in chr]
    total = sum(chr)
    return total


op = str(input("Ingrese la operación que desea realizar: "))
print("El resultado es:", solve(op))
