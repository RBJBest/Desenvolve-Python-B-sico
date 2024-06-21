print ("CALCULADORA\n")
num1=float(input("DIGITE O 1º OPERADOR: "))
op=input("DIGITE A OPERAÇÃO (+ , - , * , / , **): ")
num2=float(input("DIGITE O 2º OPERADOR: "))
if op == '+':
    print (f"{num1} {op} {num2} = {num1+num2}")
elif op == '-':
    print (f"{num1} {op} {num2} = {num1-num2}")
elif op == '*':
    print (f"{num1} {op} {num2} = {num1*num2}")
elif op == '/':
    print (f"{num1} {op} {num2} = {num1/num2}")
elif op == '**':
    print (f"{num1} {op} {num2} = {num1**num2}")
elif op != '+-*/**':
    print ("OPERADOR INVÁLIDO")        