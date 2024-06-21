jogos = int(input("INSIRA A QUANTIDADE DE JOGOS DO CABULOSO: "))
vitoria, empate, derrota = 0, 0, 0
for i in range (1,jogos+1):
    print (f"INSIRA O PLACAR DO JOGO 0{i}")
    gols_cruzeiro = int(input("GOLS DO CRUZEIRO: "))
    gols_adversario = int(input("GOLS DO ADVERSARIO: "))
    if gols_cruzeiro > gols_adversario:
        vitoria += 1 
    elif gols_cruzeiro == gols_adversario:
        empate += 1
    else:
        derrota +=1
potuacao = (vitoria*3)+empate
print (f"\nNUMEROS DE VIÓRIAS: {vitoria}")
print (f"\nNUMEROS DE EMPATES: {empate}")
print (f"\nNUMEROS DE DERROTAS: {derrota}")
print (f"\nPONTUAÇÃO DO CABULOSO: {potuacao}")

