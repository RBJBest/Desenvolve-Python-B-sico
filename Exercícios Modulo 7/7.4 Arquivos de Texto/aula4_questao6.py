import os
with open ("spotify-2023.csv","r", encoding="latin-1") as linhas:
    for i in range (5):
        texto = linhas.readline()
        print (texto)