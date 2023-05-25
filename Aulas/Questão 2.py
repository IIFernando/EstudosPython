# Questão 2

nome = 'Fernando Alves de Araujo'
ru = '3880995'
saldoC = 0

print(f'Bem vindo a Lanchonete do {nome}')
print(f'''{'*' * 15} Cardápio {'*' * 15}
|Código|  Descrição           |Valor(R$)|
|100| Cachorro-Quente             |9,00|
|101| Cachorro-Quente Duplo      |11,00|
|102| X-Egg                      |12,00|
|103| X-Salada                   |13,00|
|104| X-Bacon                    |14,00|
|105| X-Tudo                     |17,00|
|200| Refrigerante Lata           |5,00|
|201| Chá Gelado                  |4,00|''')


def produtos(item):
    Produtos = {
        "P100": {"nome": "Cachorro Quente", "preco": 9.00},
        "P101": {"nome": "Cachorro Quente Duplo", "preco": 11.00},
        "P102": {"nome": "X-Egg", "preco": 12.00},
        "P103": {"nome": "X-Salada", "preco": 13.00},
        "P104": {"nome": "X-Bacon", "preco": 14.00},
        "P105": {"nome": "X-Tudo", "preco": 17.00},
        "P200": {"nome": "Refrigerante Lata", "preco": 5.00},
        "P201": {"nome": "produto 8", "preco": 4.00}
    }
    return Produtos.get(item)


while True:
    item = input('Entre com o código desejado: ')

    nitem = 'P' + item
    produto = produtos(nitem)

    if produto is not None:
        nome = produto.get("nome")
        preco = produto.get("preco")
        print(f'Você pediu {nome} no valor de {preco:.2f}')
        saldoC += preco

    else:
        print('Opção inválida.')
        continue

    print('''Deseja pedir mais alguma coisa?
    1 - Sim
    0 - Não''')
    resp = input()

    if resp == '1':
        continue
    if resp == '0':
        break

print(f'O total a ser pago é: {saldoC:.2f}')
