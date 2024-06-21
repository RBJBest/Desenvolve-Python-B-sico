def ordena_por_comprimento(lista):
    return sorted(lista, key=lambda x: len(x))

nomes = ["Joao", "Maria", "Jose", "Gabriela", "Sol", "Luna", "Bento", "Enzo", "Fernanda"]
lista=ordena_por_comprimento(nomes)
print("LISTA ORDENADA POR ORDEM DE TAMANHO")
print (lista)