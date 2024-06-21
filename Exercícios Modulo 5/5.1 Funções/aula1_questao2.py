import math
import random
num = int(input("ESCOLHA A QUANTIDADE DE NUMEROS ALEÁTORIOS: "))
soma = 0
for i in range(num):
   num2 = random.randint(0,100)
   print (num2, end=" ")
   soma += num2
resultado  = math.sqrt(soma)   
print ( "\n", resultado)
