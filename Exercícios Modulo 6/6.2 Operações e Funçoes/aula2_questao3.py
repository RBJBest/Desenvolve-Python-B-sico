import random
lista1 = []
lista2 = []
lista3 = []
for i in range (20):
   num1 = random.randint (0,50)
   lista1.append(num1) 
   num2 = random.randint (0,50)
   lista2.append(num2)
lista1.sort()
lista2.sort()
for i in lista1:
    for n in lista2:
        if i==n and i not in lista3:
            lista3.append(i)
print (f"LISTA 01: {lista1}")
print (f"LISTA 02: {lista2}")
print (f"LISTA DE INTERSEÇÃO: {lista3}\n")
for i in lista3:
    print (f"{i}: Lista 1 = {lista1.count(i)}, Lista 2 = {lista2.count(i)}")