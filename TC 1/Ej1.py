#Ejercicio 1- Aldana G. Moreno y Dante Illesca.

def validate_string(string: str):
    print(any(chr.isalnum() for chr in string))
    print(any(chr.isalpha() for chr in string))
    print(any(chr.isupper() for chr in string))
    print(any(chr.islower() for chr in string))
    print(any(chr.isdigit() for chr in string))
    print(len(string) >= 8)


validate_string("xy@z!")
