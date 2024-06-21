import random
num_elementos = random.randint (5,20)
lista = []
for i in range (num_elementos):
    num = random.randint(1,10)
    lista.append(num)
print (lista)
print (sum(lista))
print (f"{sum(lista)/len(lista):.2f}")