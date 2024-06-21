def insirir_cadastro ():
    nome = input("INSIRA O NOME: ")    
    idade = int(input("INSIRA A IDADE: "))
    return nome,idade

def org_lista (cadastro):
    lista_maior = []
    lista_menor = []
    for nome, idade in cadastro:
        if idade>=18:
            lista_maior.append(nome)
        else:
            lista_menor.append(nome)
    return lista_maior,lista_menor

verif = 1
cadastro =[]
while verif==1: 
    verif = int(input("\nCADASTRAR USURARIO: 1 - SIM    NÃO - 2: "))
    if verif !=1:
        break
    cadastro.append((insirir_cadastro()))
lista_maior, lista_menor=(org_lista(cadastro)) 
print (f"\nLISTA COM OS MAIORES DE IDADE: {lista_maior}")
print (f"\nLISTA COM OS MENORES DE IDADE: {lista_menor}")