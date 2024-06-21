def contagem_caracteres(frase):
    letras = {}
    for letra in frase:
        if letra in letras:
            letras[letra] +=1
        else:
            letras[letra] = 1
    return letras
    

frase = "python programming"
resultado = contagem_caracteres(frase)
print(resultado)