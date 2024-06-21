produto = 1
while True:
    num = int(input("INSIRA UM NUMERO: "))
    if num == 0:
        break
    elif num<0:
        continue
    else:
        produto *= num
print (f"\nO RPODUTO DOS VALORES POSITIVOS DIGITADOS É: {produto}")
