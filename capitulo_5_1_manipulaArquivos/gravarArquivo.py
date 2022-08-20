with open("primeiroArquivo.txt", "a") as arquivo:
    arquivo.write("\nMuito bom!")

with open("primeiroArquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
