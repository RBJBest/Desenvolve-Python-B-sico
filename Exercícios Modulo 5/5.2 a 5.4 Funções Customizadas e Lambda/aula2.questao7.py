opcao = int(input("OPÇÃO: 01 - MAIOR           02 - MENOR\n "))
if opcao == 1:
    num2 = float('-inf')
    num = 1
    while num != 0:
        num = int(input("INSIRA UM NUMERO QUALQUER: "))
        verifica = (lambda num,num2:num > num2)(num,num2)
        if verifica == True:
            num2 = num
    print (f"O MAIOR NUMERO DIGITADO FOI: {num2}")
else:
    num2 = float('inf')
    num=1
    while num != 0:
        num = int(input("INSIRA UM NUMERO QUALQUER: "))
        if num == 0: break
        verifica = (lambda num,num2:num < num2)(num,num2)
        if verifica == True:
            num2 = num
    print (f"O MENOR NUMERO DIGITADO FOI: {num2}")        


    