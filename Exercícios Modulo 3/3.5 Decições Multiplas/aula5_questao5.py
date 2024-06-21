iris1_a1, iris1_a2, iris1_a3 = 123, 456, 789
iris2_a1, iris2_a2, iris2_a3 = 987, 654, 321
iris3_a1, iris3_a2, iris3_a3 = 111, 222, 333
iris4_a1, iris4_a2, iris4_a3 = 444, 555, 666
print ("PARA ACESSAR O SISTEMA, INFORME OS ATRIBUTOS DA IRÍS:")
atributo1=int(input("INSIRA O PRIMEIRO ATRÍBUTO: "))
atributo2=int(input("INSIRA O SEGUNDO ATRÍBUTO: "))
atributo3=int(input("INSIRA O TERCEIRO ATRÍBUTO: "))
if abs(atributo1-iris1_a1)<=5 and abs(atributo2-iris1_a2)<=5 and abs(atributo3-iris1_a3)<=5:
    print ("AUTENTICAÇÃO VALIDA\nUSUÁRIO 01")
elif abs(atributo1-iris2_a1)<=5 and abs(atributo2-iris2_a2)<=5 and abs(atributo3-iris2_a3)<=5:
    print ("AUTENTICAÇÃO VALIDA\nUSUÁRIO 02")
elif abs(atributo1-iris3_a1)<=5 and abs(atributo2-iris3_a2)<=5 and abs(atributo3-iris3_a3)<=5:
    print ("AUTENTICAÇÃO VALIDA\nUSUÁRIO 03")
elif abs(atributo1-iris4_a1)<=5 and abs(atributo2-iris4_a2)<=5 and abs(atributo3-iris4_a3)<=5:
    print ("AUTENTICAÇÃO VALIDA\nUSUÁRIO 04")
else:
    print ("AUTENTICAÇÃO INVALIDA")