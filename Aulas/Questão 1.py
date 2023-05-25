# Questão 1
nome = 'Fernando Alves de Araujo'
ru = '3880995'

print(f'Bem vindo a loja do {nome}.')

v_produto = float(input('Informe o valor unitário do produto: R$ '))
q_produto = int(input('Informe a quantidade do produto'))

print(f'O valor sem desconto foi: R$ {q_produto * v_produto:.2f}')

if q_produto <= 9:
    print(f'O valor sem desconto foi: R$ {q_produto * v_produto:.2f} (desconto 0%)')

elif q_produto >= 10 and q_produto <= 99:
    desc = (v_produto * q_produto) * 5/100
    print(f'O valor com desconto foi: R$ {q_produto * v_produto - desc :.2f} (desconto 5%)')

elif q_produto >= 100 and q_produto <= 999:
    desc = (v_produto * q_produto) * 10/100
    print(f'O valor com desconto foi: R$ {q_produto * v_produto - desc :.2f} (desconto 10%)')

else:
    desc = (v_produto * q_produto) * 15/100
    print(f'O valor com desconto foi: R$ {q_produto * v_produto - desc :.2f} (desconto 15%)')
