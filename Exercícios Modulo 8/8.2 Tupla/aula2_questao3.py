def ordenar_tuplas (alunos_notas):
    alunos_notas.sort(key=lambda x:x[1],reverse=True)
    return alunos_notas

alunos_notas = [('Alice', 8.5), ('Bob', 7.2), ('Charlie', 9.0), ('David', 8.8)]
resultado = ordenar_tuplas(alunos_notas)
print(resultado)

