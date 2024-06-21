print ("PARA VERIFICARMOS A POSSIBILIDADE DE APOSENTADORIA INSIRA: ")
sexo= input ("SEXO: M - MASCULINO OU F - FEMININO :")
idade = int(input("SUA IDADE: "))
tempo = int(input("SEU TEMPO DE SERVIÇO: "))
if sexo == 'f' and idade > 60 or sexo == 'm' and idade > 65:
    print ("VOCÊ JA PODE SE APOSENTAR")
elif tempo >= 30:
    print ("VOCÊ JA PODE SE APOSENTAR")
elif tempo >= 25 and idade > 60:
    print ("VOCÊ JA PODE SE APOSENTAR")
else:
    print ("INFELIZMENTE VOCE NÃO PODE SE APOSENTAR")