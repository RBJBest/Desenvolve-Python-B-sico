cont = 1
resultado = 0
while (cont>0):
    num = int(input("INSIRA UM NUMERO: "))
    ope = input("INSIRA O OPERADOR: ")
    if ope == '+':
        resultado += num
    elif ope == '-':
        resultado -= num
    elif ope =='fim':
        break
print (f"\n RESULTADO {resultado}")
