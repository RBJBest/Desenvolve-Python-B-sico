colunas = int(input("INSIRA A QUANTIDADE DE COLUNAS: "))
linhas = int(input("INSIRA A QUANTIDADE DE LINAS: "))
for i in range (colunas+1):
    if i == 0:
        print (" ", end = " ") 
    else:
        print(i, end = " ") 
for i in range (1, linhas+1):
    print()
    print(i, end=" ")
    for i in range (colunas):
         print ("/", end=" ") 
         
           
    
