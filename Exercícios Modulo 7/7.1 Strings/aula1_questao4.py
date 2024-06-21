telefone = input ("INSIRA SEU TELEFONE CELULAR: ")
quant = len(telefone)
tel=""
if quant < 9:
    telefone = ("9"+telefone)
for i in range(len(telefone)):
    if i == 4:
        tel+=telefone[i]+"-"
    else:
        tel+=telefone[i]

print (f"O TELEFONE É: {tel}")