n1, n2, n3 = int(input("DIGITE A PRIMEIRA NOTA: ")), int(input("DIGITE A SEGUNDA NOTA: ")), int(input("DIGITE A TERCEIRA NOTA: "))
m = (n1+n2+n3)/3
if m>=60:
    print ("APROVADO")
elif 40<=m<60:
    print ("RECUPERAÇÃO")
else:
    print ("REPROVADO")
print ("\n\nFIM")