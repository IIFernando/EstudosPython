nome = 'Fernando Alves de Araujo S.A'
ru = '3880995'

print(f'Bem vindo a Companhia de Logistica {nome}')

def mostrarQuadro():
    print("Quadro de Informações dos Estados:")
    print("---------------------------------")
    print("Sigla |          Rota         ")
    print("---------------------------------")
    print("  RS  | De Rio de Janeiro até São Paulo")
    print("  SR  | De São Paulo até Rio de Janeiro")
    print("  BS  | De Brasília até São Paulo")
    print("  SB  | De São Paulo até Brasília")
    print("  BR  | De Brasília até Rio de Janeiro")
    print("  RB  | Rio de Janeiro até Brasília")
    print("---------------------------------")

def dimensoesObejto():
    while True:
        altura = input('Digite o Altura do objeto (em CM): ')
        # Validar o input1
        if not altura.isdigit():
            print('Você digitou alguma dimensão do objeto com valor não numérico.')
            continue  # volta para o início do loop

        cumprimento = input('Digite o Cumprimento do objeto (em CM): ')
        # Validar o input2
        if not cumprimento.isdigit():
            print('Você digitou alguma dimensão do objeto com valor não numérico.')
            continue  # volta para o início do loop

        largura = input('Digite o Largura do objeto (em CM): ')
        # Validar o input3
        if not largura.isdigit():
            print('Você digitou alguma dimensão do objeto com valor não numérico.')
            continue  # volta para o início do loop
        
        dimensao = int(altura) * int(largura) * int(cumprimento)

        #Validação do tamanho do pacote para retornar o multiplicador.
        if dimensao <= 1000:
            multiplicadorD = 10
        elif dimensao >= 1001 and dimensao <= 10000 :
            multiplicadorD = 20
        elif dimensao >= 10001 and dimensao <= 30000:
            multiplicadorD = 30
        elif dimensao >= 30001 and dimensao <= 100000:
            multiplicadorD = 3
        elif dimensao > 100000:
            print('Não aceitamos objetos com dimensões tão grandes.')
            continue

        # Se todas as entradas forem válidas, sair do loop
        break

    return multiplicadorD

def pesoObejto():
    
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em kg): '))
        except ValueError:
            print('Você digitou um valor inválido para o peso do objeto.')
            continue

        if peso == 0.1:
            multiplicadorP = 1
        elif peso >= 0.11 and peso <= 1 :
            multiplicadorP = 1.5
        elif peso >= 1.10 and peso <= 10:
            multiplicadorP = 2
        elif peso >= 10.1 and peso <= 30:
            multiplicadorP = 3
        else:
            print('Não aceitemos objetos tão pesados')
            continue
        break
    return multiplicadorP

def rotaObjeto():
    mostrarQuadro()

    while True:
        rota = input("Digite a rota desejada do objeto (utilize as siglas das cidades): ").upper()

        if rota == 'RS':
            multiplicador = 1
            break
        elif rota == 'SR':
            multiplicador = 1
            break
        elif rota == 'BS':
            multiplicador = 1.2
            break
        elif rota == 'SB':
            multiplicador = 1.2
            break
        elif rota == 'BR':
            multiplicador = 1.5
            break
        elif rota == 'RB':
            multiplicador = 1.5
            break
        else:
            print("Sigla de rota inválida. Por favor, digite novamente.")
    return multiplicador

dimensao = dimensoesObejto()
peso = pesoObejto()
rota = rotaObjeto()

saldoF = dimensao * peso * rota

print(f'Total a pagar(R$): {saldoF:.2f}')