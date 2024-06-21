personagem = input("ESCOLHA UM PERSONAGEM: GUERREIRO, MAGO OU ARQUEIRO: ")
print ("A SEGUIR VOCÊ TERÁ 25 FICHAS PARA PERSONALIZAR SEU PERSONAGEM, PODENDO DISTRIBUI-LAS ENTRE FORÇA E MÁGIA")
forca = int(input("INSIRA A FORÇA DE SEU PERSONAGEM: "))
magia = int(input("INSIRA A MÁGIA DE SEU PERSONAGEM: "))
if forca>=15 and magia<=10 and personagem=="guerreiro":
    print ("PARABÉNS! VOCÊ ESCOLHEU O PERSONAGEM IDEAL")
if forca<=10 and magia>=15 and personagem=='mago':
    print ("PARABÉNS! VOCÊ ESCOLHEU O PERSONAGEM IDEAL")
if 5<forca<=15 and 5<magia<=15 and personagem=="arqueiro":
    print ("PARABÉNS! VOCÊ ESCOLHEU O PERSONAGEM IDEAL")    
else:
    print ("QUE PENA! SEU PERSONAGEM NÃO CONDIZ COM A REALIDADE")
