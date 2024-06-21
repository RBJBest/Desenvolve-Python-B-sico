n = int(input("DIGITE O TAMANHO DA MATRIZ: "))
matriz = [[i * j for j in range(n)] for i in range(n)]
for linha in matriz:
    print(linha)