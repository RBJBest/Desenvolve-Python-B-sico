lista1 = []
lista2 = []
lista3 = []
num1 = int(input("INSIRA A QUANTIDADE DE NUMEROS DA PRIMEIRA LISTA "))
num2 = int(input("INSIRA A QUANTIDADE DE NUMEROS DA SEGUNDA LISTA "))
for i in range(num1):
    val = int(input("INSIRA UM NUMERO DA 1ª LISTA "))
    lista1.append (val)
for i in range(num2):
    val = int(input("INSIRA UM NUMERO DA 2ª LISTA "))
    lista2.append (val) 
quant = min(len(lista1), len(lista2))
for i in range (quant):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
lista3.extend(lista1[quant:])
lista3.extend(lista2[quant:])
print (lista1, lista2, lista3) 

