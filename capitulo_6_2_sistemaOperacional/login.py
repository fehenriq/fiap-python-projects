import getpass

usuario = input("Digite o usuario: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "BITMED" and senha == "felipe":
    print("Usuario logado")
else:
    print("Login Negado")
