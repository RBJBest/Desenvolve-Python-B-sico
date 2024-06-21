frase = tuple("O rato roeu a roupa da Alice")
for i, letras in enumerate (frase):
    if letras.lower() in "aeiou":
        print (i, letras)