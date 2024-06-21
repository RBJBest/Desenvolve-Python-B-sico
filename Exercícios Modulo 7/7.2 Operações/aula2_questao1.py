nasc = input("INSIRA SUA DATA DE NASCIMENTO: ")
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho","Agosto","Setembro", "Outubro", "Novembro", "Dezembro"]
nasc = nasc.split("/")
mes = int(nasc[1])
print (type(mes))
print (mes)
print (f"VOCÊ NASCEU EM {nasc[0]} DE {meses[mes-1]} DE {nasc[2]}")

