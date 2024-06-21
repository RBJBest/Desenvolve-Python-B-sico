def inverter_numero(numero):
    # Converte o número para string
    numero_str = str(numero)
    # Inverte a string
    numero_invertido_str = numero_str[::-1]
    # Converte a string invertida de volta para inteiro
    numero_invertido = int(numero_invertido_str)
    return numero_invertido

# Teste da função
numero = 951
numero_invertido = inverter_numero(numero)
print(f'O número {numero} invertido é {numero_invertido}')