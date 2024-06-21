import random
num = random.randint(1,10)
for i in range(10):
    escolha = int(input( "ADIVINHE O NUMERO: "))
    if escolha == num:
        print ("\nPARABENS. VOCÊ ACERTOU.")
        break
    elif escolha > num:
        print ("\nUHHH. O NUMERO SEGRETO É MENOR.")
        continue
    else:
        print ("\nUHHH. O NUMERO SEGRETO É MAIOR.")
        continue