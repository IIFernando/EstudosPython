n1 = input('Informe um número: ')

try:
    
    n1 = int(n1)
    
    if n1 % 2 == 0:
        print('Este número é PAR')
    elif n1 % 2 == 1:
        print('Este número é IMPAR')
    else:
        print('Você não digitou um número inteiro.')

except:
    
    print('Você não digitou um número inteiro.')