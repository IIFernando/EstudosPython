nome = 'Fernando Alves de Araujo S.A'
ru = '3880995'

print(f'Bem vindo ao Controle de Estoque da Bicicletaria do {nome}')


def cadastrarPeca(pecas, contador_codigo):
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite o fabricante da peça: ")
    valor = float(input("Digite o valor da peça: "))

    peca = {
        "Código": contador_codigo,
        "Nome": nome,
        "Fabricante": fabricante,
        "Valor": valor
    }

    pecas.append(peca)
    print(f"Peça cadastrada com sucesso! Código: {contador_codigo}")


def consultarTodasPecas(pecas):
    print("\n--- Consultar Todas as Peças ---")
    if pecas:
        for peca in pecas:
            print(peca)
    else:
        print("Nenhuma peça cadastrada.")


def consultarPecaPorCodigo(pecas):
    print("\n--- Consultar Peças por Código ---")
    codigo = input("Digite o código da peça: ")
    for peca in pecas:
        if peca["Código"] == int(codigo):
            print(peca)
            return
    print("Peça não encontrada.")


def consultarPecaPorFabricante(pecas):
    print("\n--- Consultar Peças por Fabricante ---")
    fabricante = input("Digite o fabricante da peça: ")
    for peca in pecas:
        if peca["Fabricante"] == fabricante:
            print(peca)


def removerPeca(pecas):
    codigo = input("Digite o código da peça que deseja remover: ")
    for peca in pecas:
        if peca["Código"] == int(codigo):
            pecas.remove(peca)
            print("Peça removida com sucesso!")
            return
    print("Peça não encontrada.")


# Menu principal
pecas = []
contador_codigo = 1

while True:
    print("\n--- Menu ---")
    print("1. Cadastrar Peça")
    print("2. Consultar Peça")
    print("3. Remover Peça")
    print("4. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrarPeca(pecas, contador_codigo)
        contador_codigo += 1
    elif opcao == "2":
        while True:
            print("\n--- Menu de Consulta ---")
            print("1) Consultar Todas as Peças")
            print("2) Consultar Peças por Código")
            print("3) Consultar Peças por Fabricante")
            print("4) Retornar")

            opcao_consulta = input("Digite a opção desejada: ")

            if opcao_consulta == "1":
                consultarTodasPecas(pecas)
            elif opcao_consulta == "2":
                consultarPecaPorCodigo(pecas)
            elif opcao_consulta == "3":
                consultarPecaPorFabricante(pecas)
            elif opcao_consulta == "4":
                break
            else:
                print("Opção inválida. Digite novamente.")
    elif opcao == "3":
        removerPeca(pecas)
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Digite novamente.")

print("Encerrando o programa.")
