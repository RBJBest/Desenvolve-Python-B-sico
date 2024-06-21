frase = input("DIGITE UMA FRASE: ")
vogais_indices = []
quant=0
for i in range (len(frase)):
    if frase[i].lower( ) in "aeiou":
        vogais_indices.append (i)
        quant+=1
print (f"SÃO {quant} VOGAIS")
print (vogais_indices)
