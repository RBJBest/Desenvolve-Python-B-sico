sal_hora = 20.00
horas_trab = 40
salario_bruto = sal_hora*horas_trab
inss = (salario_bruto*10)/100
sind = (salario_bruto*5)/100
salario_liquido = salario_bruto - (inss+sind)
print (f"O SALÁRIO SEMANAL BRUTO É: {salario_bruto}")
print (f"O TAXA SEMANAL DO INSS É: {inss}")
print (f"O TAXA SEMANAL DO SINDICATO É: {sind}")
print (f"O SALÁRIO SEMANAL LÍQUIDO É: {salario_liquido}")