exp = str(input("Ingrese la expresion: "))
state = "A"
error = False
dict = {("A","a"): "B", ("A","b"): "C",
("B","a"): "D", ("B","b"): "E", ("C","a"): "B", ("C","b"): "F",
("D","a"): "B", ("D","b"): "C", ("E","a"): " ", ("E","b"): "G", 
("F","a"): "B", ("F","b"): "C", ("G","a"): "H", ("G","b"): "E",
("H","a"): "H", ("H","b"): "E",}

print(len(exp))
if len(exp) == 0:
    error = True
for i in exp:
    state = dict[(state, i)]
    print(state)
    if (i != "a") and (i != "b"):
        error = True

if ((state == "A") or (state == "B") or (state == "C") or (state == "D")) and (error == False):
    print("El estado final es:", state)

elif error == True:
    print("Algo ha salido mal")