import os

f = open ("shakespeare.txt","r")
linhas=[]
verificador = {}
linhas = f.readlines()
for linha in linhas:
    palavra = linha.split(" ")
    for palavra in linhas:
        if palavra in linhas:
            verificador[palavra] +=1
        else:
            verificador[palavra] = 1
f.close()

   