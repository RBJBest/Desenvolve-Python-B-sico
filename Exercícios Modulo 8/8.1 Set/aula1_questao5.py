def checa_panagrama(texto):
    if len(texto)==26:
        print ("É UM PANAGRAMA") 
    else:
        print ("NÃO É UM PANAGRAMA") 

texto = input("DIGITE UM TEXTO PARA SABER SE É UM PANAGRAMA:\n")
texto = texto.lower()
texto = texto.replace(" ","")
texto = set(texto)
checa_panagrama(texto)

#Exemplos de frases
#The quick brown fox jumps over the lazy dog
#Python é uma liguagem de programação