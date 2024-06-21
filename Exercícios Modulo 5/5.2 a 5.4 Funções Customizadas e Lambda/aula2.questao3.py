def soma_digito(num):
    soma=0
    while (num>0):   
        x = num%10
        soma=soma + x
        num=int(num/10)
    return soma
    

num1 = int(input("INSIRA UM NUMERO: "))
print (f"A SOMA DOS DIGITOS DO NUMERO DIGITADO É: {soma_digito (num1)}")
