def comprimir_tuplas(tuplas_originais):
    resultado = []
    for palavra, numero in tuplas_originais:
        encontrado = False
        for i, (palavra_res, numero_res) in enumerate(resultado):
            if palavra_res == palavra:
                resultado[i] = (palavra_res, numero_res + numero)
                encontrado = True
                break
        if not encontrado:
            resultado.append((palavra, numero))
    return resultado

tuplas_originais = [("maçã", 2), ("banana", 3), ("maçã", 1), ("laranja", 4), ("banana", 1)]
nova_tupla = comprimir_tuplas(tuplas_originais)
print (nova_tupla)
