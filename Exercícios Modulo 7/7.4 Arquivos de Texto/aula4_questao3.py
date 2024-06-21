import os,sys
texto_linha = ""
quant_linhas = ""
maior_linha = float('-inf')
frase_maior = ''
with open('estomago.txt','r', encoding='utf=8') as linhas:
    for i in range(25):
        texto_linhas = linhas.readline()
        if texto_linhas:  
            print(texto_linhas)
    quant_linhas=linhas.readlines()
    for i in range (len(quant_linhas)):
        if (len(quant_linhas[i])) > maior_linha:
            maior_linha = len(quant_linhas[i])
            frase_maior=quant_linhas[i]
print (len(quant_linhas))
print (frase_maior)