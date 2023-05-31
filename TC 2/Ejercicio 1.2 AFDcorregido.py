states = ["A","B","C","D","E","F","G","H"]
arrows = ["a","b"]
movements = {("A","a"): "B",
             ("A","b"): "C",
             ("B","a"): "D",
             ("B","b"): "E",
             ("C","a"): "B",
             ("C","b"): "F",
             ("D","a"): "B",
             ("D","b"): "C",
             ("E","a"): " ",
             ("E","b"): "G",
             ("F","a"): "B",
             ("F","b"): "C",
             ("G","a"): "H",
             ("G","b"): "E",
             ("H","a"): "H",
             ("H","b"): "E"}
initial_state = "A"
final_state = ["A","B","C","D","E","F","G","H"]

def circuit(expresion):
    actual_state = initial_state
    for i in expresion:
        actual_state = movements.get((actual_state,i),None)
        if actual_state is None:
            return False
    return actual_state in final_state

chain = str(input("Ingrese la cadena: "))
print(circuit(chain))
