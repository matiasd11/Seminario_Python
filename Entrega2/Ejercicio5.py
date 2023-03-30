frase = input("Ingrese una frase: \n")
string = input("Ingrese un string: \n")

frase = frase.lower().split()
string = string.lower()
cant = 0
for i in frase:
    if string in i:
        cant+= 1

print(cant)