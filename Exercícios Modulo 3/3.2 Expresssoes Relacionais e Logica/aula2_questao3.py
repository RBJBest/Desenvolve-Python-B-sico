idade = int(input("DIGITE SUA IDADE: "))
partida = input("VOCE JA JOGOU PELO MENOS 3 PARTIDAS DE TABULEIRO - TRUE/FALSE: ")
vitoria = int(input("DIGITE QUANTAS VEZES VOCÊ JA VENCEU UMA PARTIDA DE TABULEIRO: "))
resultado = 16 <= idade <= 18 and partida == "true" and vitoria >=1
print (f"Apto para ingressar no clube de jogos de tabuleiro: {resultado}")