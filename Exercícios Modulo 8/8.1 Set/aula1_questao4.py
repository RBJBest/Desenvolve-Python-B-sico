def tem_elementos_comuns (lista1, lista2):
        result = lista1.symmetric_difference(lista2)
        if result.issubset(lista1):
            print(f"O ELEMENTO {result} ESTÁ FALTANDO NA SEGUNDA LISTA")
        else:
            print(f"O ELEMENTO {result} ESTÁ FALTANDO NA PRIMEIRA LISTA")
            
A = set([1,4,5,7,9])
B = set([4,5,7,9,])
tem_elementos_comuns(A, B)
 