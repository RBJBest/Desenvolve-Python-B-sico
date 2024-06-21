frase = input("DIGITE UMA FRASE: ")
cont = 0
for i in frase:
    if i == " ":
        cont+=1
print (f"SÃO {cont} ELEMENTOS EM BRANCOS")
