import os,sys
texto = ""
palavra = []
with open ("frase.txt",'r') as f:
    texto=f.readline()
palavra=texto.split(" ")
for i in range (len(palavra)):
    f=open('palavras.txt','a')
    f.write(palavra[i]+'\n')
    f.close()
diretorio = os.getcwd()
print (diretorio)