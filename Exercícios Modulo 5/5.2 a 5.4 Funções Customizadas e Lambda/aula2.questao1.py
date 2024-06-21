def fatorial(n):
    fat = 1
    for i in range(1,n+1):
        fat*=i
    return fat

n = int(input("INSIRA UM NUMERO PRA CALCULAR FATORIAL: "))
resultado = fatorial(n)
print (f"O VALOR DE FATORIAL DE {n} é: {resultado}")