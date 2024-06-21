cpf = "473063662"

cp = ""
pf = 0
soma = 0
for i in cpf:
    if i != "." and i != "-":
        cp+=(i)
print(cpf)
print (cp)
mult = 2
for i in range (8,-1,-1):
    pf = int(cp[i])
    pf = pf*(mult)
    soma+=pf
    mult+=1
resul=soma%11
if resul < 2:
    digito = "0"
else:
    digito = str(11-(soma%11))
cpf+=digito

cp = ""
pf = 0
soma = 0
for i in cpf:
    if i != "." and i != "-":
        cp+=(i)
mult = 2
for i in range (9,-1,-1):
    pf = int(cp[i])
    pf = pf*(mult)
    soma+=pf
    mult+=1
resul=soma%11
if resul < 2:
    digito = "0"
else:
    digito = str(11-(soma%11))
cp+=digito
print (cp)
    
##################################3


