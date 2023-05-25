compras = []

while True:
    
    print('Abaixo selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    if opcao == 'i':
        item = input('Valor: ')
        compras.append(item)
        
    if opcao == 'l':
        for i in enumerate(compras):
            print(i)
    
    if opcao == 'a':
        delItem = input('Valor: ')
        compras.remove(delItem)
        
    else:
        print('Opção inválida, tente novamente.')