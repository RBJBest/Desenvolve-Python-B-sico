nota=int(input("PARA SABER SUA CLASSIFICAÇÃO INSIRA SUA PONTUAÇÃO: "))
if nota < 70:
    print ("CLASSIFICAÇÃO: INSATISFATÓRIA")
elif nota >= 70 and nota < 80:
    print ("CLASSIFICAÇÃO: REGULAR")
elif nota >= 80 and nota < 90:
    print ("CLASSIFICAÇÃO: BOM")
elif nota >= 90:
    print ("CLASSIFICAÇÃO: EXCELENTE")