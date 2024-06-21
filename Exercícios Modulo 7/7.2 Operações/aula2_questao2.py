frase = input("DIGITE UMA FRASE: ")
frase_mod = ''
for i in range (len(frase)):
    if frase[i].lower( ) in "aeiou":
        frase_mod = frase_mod + "*"
    else:
        frase_mod+= (frase[i])   
print (frase_mod)