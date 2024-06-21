import os,sys
texto = input("INSIRA SUA FRASE: ")
f = open ("frase.txt",'w')
f.write(texto)
f.close()
diretorio = os.getcwd()
print (diretorio)

#MÉTODO WITH
#import os,sys
#texto = input("INSIRA SUA FRASE: ")
#with ope('com_with.txt','w') as f:
#    f.write(texto)
#diretorio = os.getcwd()
#print (diretorio)