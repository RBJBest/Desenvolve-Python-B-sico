import random
lista1 = []
for i in range (20):
    lista1.append(random.randint (-10,10))
num_ind_ini, num_ind_fin, num_valor, num_val_maior = 0,0,0,0
for i in range (len(lista1)):
    if lista1[i] < 0:
        num_valor += 1
        if num_valor == 1:
            num_ind_ini = i
        elif num_valor > 1:
            num_ind_fin = i
    else:
        if num_valor < num_val_maior:
            num_valor=0
print (num_ind_ini)  
print (num_ind_fin)    
print (num_valor)      
print (lista1)  
print (lista1.index(max(lista1)))
print (max(lista1))


##### SEM SOLUÇAO AINDA