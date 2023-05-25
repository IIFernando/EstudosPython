def parImpar():
    
    a = int(input('Valor: '))
    
    if a % 2 == 0:
        return 'PAR'
    return 'ÍMPAR'

print(parImpar())