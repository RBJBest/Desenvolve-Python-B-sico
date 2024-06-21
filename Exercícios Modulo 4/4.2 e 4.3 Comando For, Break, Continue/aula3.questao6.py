cont = 1
maior = float("-inf")
menor = float("inf")
while (cont>0):
    num = int(input("INSIRA UM NUMERO: "))
    if num == 0:
        break
    elif num > maior:
        maior = num
    elif num<menor:
        menor = num
print (f"\nMAIOR NUMERO DIGITADO: {maior}")
print (f"MENOR NUMERO DIGITADO: {menor}")