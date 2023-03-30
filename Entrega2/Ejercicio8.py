from collections import Counter
palabra = input("Ingrese una palabra o frase: ").lower()

c = Counter(palabra)
dicc = dict(c)
ok = True
for i in dicc:
    if dicc[i] > 1:
        ok = False
        break
print(f"Es heterograma: {ok}")