soma = 0
for i in range(1,11):
    num = int(input(f"INSIRA O NUMERO 0{i}: "))
    soma += num
media = soma/10
print (f"A MEDIA DOS VALORES DIGITADO É: {media:.2f}")