import random
def alterar_nomes(lista_nomes, key):
    nomes_alterados = []
    for nome in lista_nomes:
        nome_alterado = ""
        for letra in nome:
            novo_codigo = ord(letra) + (key)
            nova_letra = chr(novo_codigo)
            nome_alterado += nova_letra
        nomes_alterados.append(nome_alterado)
    return nomes_alterados

lista = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
chave = random.randint(1,10)
nomes_alterados = alterar_nomes(lista,chave)
print(nomes_alterados)
