import datetime
data_atual = datetime.datetime.now()
hora_bras = '{}:{}'.format(data_atual.hour, data_atual.minute)
data_bras = data_atual.strftime('%d/%m/%Y')
print ("Data: ",data_bras)
print ("Horas: ",hora_bras)