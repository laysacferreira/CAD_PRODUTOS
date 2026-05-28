import os

opcao = 0

while (opcao != 4):
    print("~~~~~~ MENU ~~~~~~")
    print("1 - para cadastrar produto")
    print("2 - para listar produtos")
    print("3 - para excluir produto")
    print("4 - para sair")
    print("~~~~~~~~~~~~~~~~~~~~")
 
    opcao = int(input("Escolha a opção: "))
 
    if opcao == 1:
        print("~~~~~~~~ CADASTRAR PRODUTOS ~~~~~~~~")
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto: ")
        quantidade = input("Digite a quantidade de produto: ")

        arquivo = open("produtos.txt", "a")
        arquivo.write(f"{codigo}|{nome}|{preco}|{quantidade}\n")
        arquivo.close()
       
 
        print("Produto cadastrado com sucesso")

        input()
        os.system("cls")

    elif (opcao == 2):
        print("~~~~~~~~ LISTAR PRODUTOS ~~~~~~~~")

        arquivo = open("produtos.txt", "r")

        for produto in arquivo:
            codigo, nome, preco, quantidade  = produto.strip().split("|")
            print(f"~~~~~~~~PRODUTO~~~~~~~~")
            print(f"O códido do produto é: {codigo}")
            print(f"O nome do produto é: {nome}")
            print(f"o preço do produto é: {preco}")
            print(f"A quantidade é: {quantidade}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

        arquivo.close()

        input()
        os.system("cls")

    elif (opcao == 3):
        arquivo = open("produtos.txt", "r")
        linhas = arquivo.readlines() # leitura das linhas e armazenado em uma lista
        arquivo.close() # fechei o arquivos produtos.txt

        remover = int(input("Digite a linha que deseja remover: "))
        remover = remover - 1
        linhas.pop(remover)

        arquivo = open("produtos.txt", "w")
        for linha in linhas:
            arquivo.write(linha)
        arquivo.close()
        

        print("Produto removido com sucesso!!")

        input()
        os.system("cls")