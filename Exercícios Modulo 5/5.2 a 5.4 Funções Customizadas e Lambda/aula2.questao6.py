num=1
while num != 0:
    num = int(input("INSIRA UM NUMEROA QUALQUER: "))
    verifica = (lambda num:num%2)(num)
    if num == 0:
        break
    if verifica == 0:
        print (f"{num} É UM NUMERO PAR\n")
    else:
        print (f"{num} É UM NUMERO IMPAR\n")


         
        

    

    

    
