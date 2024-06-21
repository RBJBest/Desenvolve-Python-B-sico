print ("DEFININDO O TIPO DE TRIÂNGULO\n")
lado1=int(input("DIGITE O TAMANHO DO 1º LADO: "))
lado2=int(input("DIGITE O TAMANHO DO 2º LADO: "))
lado3=int(input("DIGITE O TAMANHO DO 3º LADO: "))
if lado1 == lado2 and lado2 == lado3:
    print ("TRIÂNGULO EQUILÁTERO")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print ("TRIÂNGULO ESCALENO")
else:
    print("TRIÂNGULO iSÓCELES")