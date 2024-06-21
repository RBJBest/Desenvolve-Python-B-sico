import os,random
texto = []
palavra = ""
palavra_mod = []
escolha = random.randint(1,3)
chances=1
f = open("gabarito_forca.txt")
for linhas in f:
    if escolha == 1:
        if linhas.startswith('fruta'):
            palavra = linhas.split(" ")
            palavra = palavra[random.randint(1,10)]
            print(palavra)
            print (f"A PAVARA SORTEADO É UMA FRUTA DE {len(palavra)} LETRAS\n E VOCÊ TEM 06 CHANCES PARA DESCOBRI-LÁ.\n")
    elif escolha ==2:
        if linhas.startswith('cidade'):
            palavra = linhas.split(" ")
            palavra = palavra[random.randint(1,10)]
            print(palavra)
            print (f"A PAVARA SORTEADO É UMA CIDADE BRASILEIRA DE {len(palavra)} LETRAS\n E VOCÊ TEM 06 CHANCES PARA DESCOBRI-LÁ.\n")
    elif escolha == 3:
        if linhas.startswith('animal'):
            palavra = linhas.split(" ")
            palavra = palavra[random.randint(1,10)]
            print(palavra)
            print (f"A PAVARA SORTEADO É UM ANIMAL DE {len(palavra)} LETRAS\n E VOCÊ TEM 06 CHANCES PARA DESCOBRI-LÁ.\n")
f.close()
palavra_mod=list(palavra)
for i in palavra:
    palavra=palavra.replace(i,"*")
palavra = list(palavra)
for i in range (6):
    letra = input("INSIRA UMA LETRA:")
    soma=0
    erro=0
    for i in range (len(palavra_mod)):
        if letra == palavra_mod[i]:
            palavra[i]=letra
            print(palavra)
        else:
            soma+=1
    if soma == (len(palavra_mod)):
        print ("ESTA LETRA NÃO EXITE")
        erro+=1
        with open('gabarito_forca.txt','r', encoding='utf=8') as linhas:
            for i in range(5):
                texto_linhas = linhas.readline()
                if texto_linhas:  
                    print(texto_linhas)
    elif palavra == palavra_mod:
        print ("voce ganhou")
        break
    print (soma)
    chances+=1
    

        



            
