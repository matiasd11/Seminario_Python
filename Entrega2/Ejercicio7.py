import string
texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
 """

cantMayu = 0
cantMinu = 0
cantNoLet = 0
for i in texto:
    if i in string.ascii_uppercase:
        cantMayu += 1
    else:
        if i in string.ascii_lowercase:
            cantMinu += 1
        else:
            if not(i in string.ascii_letters):
                cantNoLet += 1

texto = texto.lower().split()
lista = set(texto)
print(f"Cantidad mayus: {cantMayu}")
print(f"Cantidad minus: {cantMinu}")
print(f"Cantidad no letras: {cantNoLet}")
print(len(lista))
