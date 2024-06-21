def tem_elementos_comuns (lista1, lista2):
        result = lista1.intersection(lista2)
        result = len(result)
        if result > 0: 
              return True
        else: 
              return False

lista1 = set([1,2,3,4])
lista2 = set([3,4,5,6,7])
resultado = tem_elementos_comuns(lista1, lista2)
print(resultado) 