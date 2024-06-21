lista1 = []
num = 1
while (num!=0):
    num = int(input("INSIRA UM NUMERO: "))
    lista1.append(num)
print (f"\nLISTA ORIGINAL : {lista1}")
print (f"3 PRIMEIROS ELEMENTOS DA LISTA: {lista1[:3]}")
print (f"2 ULTIMOS ELEMENTOS DA LISTA: {lista1[-2:]}")
print (f"LISTA INVERTIDA: {lista1[::-1]}")
print (f"LISTA DOS INDICES PARES: {lista1 [::2]}")
print (f"LISTA DOS INDICES IMPARES: {lista1[1::2]}")


