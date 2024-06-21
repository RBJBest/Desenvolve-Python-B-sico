def validador_senha(senha):
    tamanho = len(senha)
    senha_dec = ''
    op_num, op_min, op_mai, op_sim = 0,0,0,0
    for num in senha:
        senha_dec=(ord(num))
        if 48 <= senha_dec <= 57:
            op_num+=1
        elif 97 <= senha_dec <= 122:
            op_min+=1
        elif 65 <= senha_dec <= 90:
            op_mai+=1
        else:
            op_sim+=1
    if op_sim>0 and op_mai>0 and op_min>0 and op_num>0 and tamanho>8:
        return True
    else:
        return False
    
senha = input("INSIRA SUA SENHA: ")
validador = validador_senha(senha)
print (f"SENHA {validador}")