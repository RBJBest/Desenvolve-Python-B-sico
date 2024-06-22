import os

def carregar_usuarios(arquivo):
    users = {}
    try:
        with open(arquivo, 'r') as file:
            for line in file:
                username, password = line.strip().split(':')
                users[username] = password
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
    return users

def login_usuario():
    users = carregar_usuarios("usuarios.txt")
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")
    if username in users and users[username] == password:
        print("Login bem-sucedido!")
        return True
    else:
        print("Nome de usuário ou senha incorretos.")
        return False

def cadastrar_produto():
    caracteristica = input("Digite a característica do produto: ")
    tipo = input("Digite o tipo do produto: ")
    nome = input("Digite o nome do produto: ")
    quantidade = input("Digite a quantidade do produto em estoque: ")
    preco = input("Cadastre o preço do produto: ")
    with open("produtos.txt", 'a') as f:
        f.write(f"{caracteristica},{tipo},{nome},{quantidade},{preco}\n")
    print("Produto cadastrado com sucesso!")

def cadastrar_usuario():
    username = input("Digite o nome do usuário: ")
    password = input("Digite a senha do usuário: ")
    with open("usuarios.txt", 'a') as f:
        f.write(f"{username}:{password}\n")
    print("Usuário cadastrado com sucesso!")
def verificar_estoque():
    try:
        with open("produtos.txt", 'r') as f:
            produtos = f.readlines()
            if produtos:
                for produto in produtos:
                    print(produto.strip())
            else:
                print("Estoque vazio.")
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")

def main():
    print("DISTRIBUIDORA NOS TRUPICA MAS NÃO CAI")
    if not login_usuario():
        return

    while True:
        opcao = int(input("\nMENU\n 1 - CADASTRAR PRODUTO\n 2 - VERIFICAR ESTOQUE\n 3 - CADASTRAR USUÁRIO\n 4 - Sair\nESCOLHA UMA OPÇÃO: "))
        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            verificar_estoque()
        elif opcao == 3:
            cadastrar_usuario()
        elif opcao == 4:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
