def invertValor (num):
    inverso = []
    cont=0
    while (num>0):
        resto = num%10
        num = num//10
        inverso.append(resto)
    numero = ''.join(str(numero) for numero in inverso)
    numero = int(numero)
    return (numero)
        

def verificaInverso(num1,num2):
    if (num1%2) == 0 and (num2%2) == 0:
        return True
    elif (num1%2) != 0 and (num%2) != 0:
        return True
    else:
        return False

num = int(input("DIGITE UM NUMERO: "))
inverso = invertValor(num)
verificador=verificaInverso(num,inverso)
print (f"O VALOR DIGITADO INVERTIDO É: {inverso}")
print (f"SE AMBOS OS NUMEROS SÃO PARES OU IMPARES: {verificador}")


