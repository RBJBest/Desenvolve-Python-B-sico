valor=int(input("DIGITE O VALOR DA COMPRA: "))
if valor < 50:
    print (f"VOCÊ NÃO POSSUI DESCONTO. O VALOR DA COMPRA É {valor:,.2f} REAIS") 
elif valor >= 50 and valor < 100:
    print (f"VOCÊ POSSUI 10% de DESCONTO. O VALOR DA COMPRA É {(valor*90)/100:,.2f} REAIS") 
elif valor > 100:
    print (f"VOCÊ POSSUI 20% de DESCONTO. O VALOR DA COMPRA É {(valor*80)/100:,.2f} REAIS") 
