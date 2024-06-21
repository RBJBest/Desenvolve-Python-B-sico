distancia = int(input("INSIRA A DISTÂNCIA DA ENTREGA:"))
peso = int(input("AGORA INSIRA O PESO DO PACOTE A SER ENTREGUE: "))
if distancia <= 100:
    if peso > 10:
        print ("O VALOR DE ENTREGA SERÁ: ", (peso*1)+10)
    else:
        print ("O VALOR DE ENTREGA SERÁ: ", (peso*1))
if 100 < distancia <= 300:
    if peso > 10:
        print ("O VALOR DE ENTREGA SERÁ: ", (peso*1.5)+10)
    else:
        print ("O VALOR DE ENTREGA SERÁ: ", (peso*1.5))
else:
    if peso > 10:
        print ("O VALOR DE ENTREGA SERÁ: ", (peso*2)+10)
    else:
        print ("O VALOR DE ENTREGA SERÁ: ", (peso*2))

