def calcula_area_perimetro (dimensoes):
    area = dimensoes[0]*dimensoes[1]
    perimetro = 2*(dimensoes[0]+dimensoes[1])
    return area,perimetro

dimensoes = 2,5
area, perimetro = calcula_area_perimetro(dimensoes)
print (f"A AREA DO TERRENO É {area} E O PERIMETRO {perimetro}")