states = ["A","B","C"]
arrows = ["a","b"]
movements = {("A","a"): "B",
             ("A","b"): "C",
             ("B","a"): "B",
             ("B","b"): "C",
             ("C","a"): "B",
             ("C","b"): "C"}
initial_state = "A"
final_state = ["A","B","C"]

def circuit(expresion):
    actual_state = initial_state
    for i in expresion:
        actual_state = movements.get((actual_state,i),None)
        if actual_state is None:
            return False
    return actual_state in final_state

chain = str(input("Ingrese la cadena: "))
print(circuit(chain))