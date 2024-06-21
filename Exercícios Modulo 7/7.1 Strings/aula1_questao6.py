frase = input("DIGITE UMA FRASE: ")
palavra = sorted(input("DIGITE A PALAVRA OBJETIVO: "))
frases_lista = frase.lower().split()
for i in frases_lista:
    if sorted(i) == palavra:
        print (i)
