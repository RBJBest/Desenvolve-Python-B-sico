frase = input("DIGITE UMA FRASE: ")
frase = frase.replace(" ","")
frase = frase.lower()
frase = sorted(set(frase))
print (frase)

