n = int(input ( "INSIRA UM NUMERO: "))
maior = 0
while n > 0 :
    x= int(input ( "INSIRA UM OUTRO  NUMERO: "))
    if x > maior :
        maior = x
        n -= 1
    else:
        n -=1
print (maior)
