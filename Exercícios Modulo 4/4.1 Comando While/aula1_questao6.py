total_exper = int(input("INSIRA A QUANTIDADE DE EXPERIMENTOS REALIZADOS: "))
cont = 0
sapo = 0
rato = 0
coelho = 0
while total_exper > cont:
    sapo += int(input("INSIRA A QUANTIDADE DE SAPO UTILIZADO NESTE EXPERIMENTO: "))
    rato += int(input("INSIRA A QUANTIDADE DE RATO UTILIZADO NESTE EXPERIMENTO: "))
    coelho += int(input("INSIRA A QUANTIDADE DE COELHO UTILIZADO NESTE EXPERIMENTO: "))
    cont += 1
print(f"\n\nA QUAUNTIDADE DE COBAIAS UTILIZADAS FORAM DE: {sapo+rato+coelho} ANIMAIS ")
print(f"\nA QUAUNTIDADE TOTAL DE SAPOS UTILIZADAS FORAM DE: {sapo} SAPOS ")
print(f"\nA QUAUNTIDADE TOTAL DE RATOS UTILIZADAS FORAM DE: {rato} RATOS ")
print(f"\nA QUAUNTIDADE TOTAL DE COLEHOS UTILIZADAS FORAM DE: {coelho} COELHOS ")
print(f"\nA QUAUNTIDADE DE SAPOS UTILIZADAS FOI DE: {(sapo*100)/(sapo+rato+coelho):,.2f}% ")
print(f"\nA QUAUNTIDADE DE RATOS UTILIZADAS FOI DE: {(rato*100)/(sapo+rato+coelho):,.2f}% ")
print(f"\nA QUAUNTIDADE DE COLEHOS UTILIZADAS FOI DE: {(coelho*100)/(sapo+rato+coelho):,.2f}% ")
