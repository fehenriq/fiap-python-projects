nivel = input("Nivel de acesso: ").upper()

if nivel == "ADM" or nivel == "USR":
    genero = input("Genero: ").upper()
    if nivel == "ADM":
        if genero == "MASCULINO":
            print("Olá Administrador")
        else:
            print("Olá Administradora")
    elif nivel == "USR":
        if genero == "MASCULINO":
            print("Olá Usuário")
        else:
            print("Olá Usuária")
elif nivel == "GUEST":
    print("Olá visitante")
else:
    print("Olá desconhecido")
