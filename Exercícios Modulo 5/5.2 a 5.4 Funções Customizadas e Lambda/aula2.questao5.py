import math
def calcula_perimetro_triangulo(num1,num2,num3):
    perimetro = num1+num2+num3
    return perimetro
def calcula_perimetro_circulo(num1):
    perimetro = (2*num1*math.pi)
    return perimetro
def calcula_perimetro_retangulo(forma,num1,num2):
    if forma == 1:
        perimetro = (num1*4)
        return perimetro
    else:
        perimetro = (num1*2)+(num2*2)
        return perimetro

escolha=1
while escolha != 4:
    escolha = int(input (" 1 - CALCULAR PERÍMETRO DE UM TRIANGULO\n 2 - CALCULAR PERÍMETRO DE UMA CIRCUNFERÊNCIA\n\
 3 - CALCULAR PERÍMETRO DE UM RETÂNGULO\n 4 - SAIR\n"))
    if escolha == 1:
        num1 = int(input("INSIRA O PRIMEIRO LADO: "))
        num2 = int(input("INSIRA O SEGUNDO LADO: "))
        num3 = int(input("INSIRA O TERCEIRO LADO: "))
        perimetro = calcula_perimetro_triangulo(num1,num2, num3)
        print(f"\nO PERIMETRO DO TRINAGULO É: {perimetro}\n") 
        continue
    elif escolha == 2:
        num1 = float(input("INSIRA O RAIO DA CIRCUNFERÊNCIA: "))
        perimetro = calcula_perimetro_circulo(num1)
        print(f"\nO PERIMETRO DA CIRCUNFERÊNICA É: {perimetro:.2f}\n") 
        continue
    elif escolha == 3:
        forma = int(input (" PARA UM QUADRADO ESCOLHA 1\n PARA UM RETANGULO ESCOLHA 2\n"))
        if forma == 1:
            num1 = int(input("INSIRA O LADO QUADRADO: "))
            num2=0
            perimetro = calcula_perimetro_retangulo(forma,num1,num2) 
            print(f"\nO PERIMETRO DO QUATRADO É: {perimetro}\n")
        elif forma == 2:
            num1 = int(input("INSIRA O LADO MAIOR DO RETANGULO: "))
            num2 = int(input("INSIRA O LADO MENOR DO RETANGULO: "))
            perimetro = calcula_perimetro_retangulo(forma,num1,num2)
            print(f"\nO PERIMETRO DO RETANGULO É: {perimetro}\n")
        continue
    elif escolha == 4:
        break