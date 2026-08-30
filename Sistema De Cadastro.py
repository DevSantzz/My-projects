print("=== SISTEMA DE CADASTRO ===")

cadastros = []

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar cadastros")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        email = input("E-mail: ")

        cadastro = {
            "nome": nome,
            "idade": idade,
            "email": email
        }

        cadastros.append(cadastro)
        print("Cadastro realizado com sucesso!")

    elif opcao == "2":
        print("\n=== CADASTRADOS ===")

        if len(cadastros) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in cadastros:
                print(f"Nome: {pessoa['nome']}")
                print(f"Idade: {pessoa['idade']}")
                print(f"E-mail: {pessoa['email']}")
                print("-------------------")

    elif opcao == "3":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")
