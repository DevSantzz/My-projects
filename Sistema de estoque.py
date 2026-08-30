print("=== SISTEMA DE CONTROLE DE ESTOQUE ===")

estoque = {}

while True:
    print("\n1 - Cadastrar produto")
    print("2 - Listar estoque")
    print("3 - Adicionar quantidade")
    print("4 - Remover quantidade")
    print("5 - Excluir produto")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")

        if nome in estoque:
            print("Produto já cadastrado!")
        else:
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: R$ "))

            estoque[nome] = {
                "quantidade": quantidade,
                "preco": preco
            }

            print("Produto cadastrado!")

    elif opcao == "2":
        print("\n=== ESTOQUE ===")

        if not estoque:
            print("Estoque vazio.")
        else:
            for nome, produto in estoque.items():
                total = produto["quantidade"] * produto["preco"]

                print(f"\nProduto: {nome}")
                print(f"Quantidade: {produto['quantidade']}")
                print(f"Preço: R$ {produto['preco']:.2f}")
                print(f"Valor total: R$ {total:.2f}")

    elif opcao == "3":
        nome = input("Produto: ")

        if nome in estoque:
            quantidade = int(input("Quantidade para adicionar: "))
            estoque[nome]["quantidade"] += quantidade
            print("Quantidade adicionada!")
        else:
            print("Produto não encontrado!")

    elif opcao == "4":
        nome = input("Produto: ")

        if nome in estoque:
            quantidade = int(input("Quantidade para remover: "))

            if quantidade <= estoque[nome]["quantidade"]:
                estoque[nome]["quantidade"] -= quantidade
                print("Quantidade removida!")
            else:
                print("Quantidade insuficiente no estoque!")
        else:
            print("Produto não encontrado!")

    elif opcao == "5":
        nome = input("Produto que deseja excluir: ")

        if nome in estoque:
            del estoque[nome]
            print("Produto excluído!")
        else:
            print("Produto não encontrado!")

    elif opcao == "6":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")
