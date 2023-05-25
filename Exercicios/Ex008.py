import os

pSecreta= 'perfume'
lAcertadas = ''
nTentativas = 0

while True:
    
    letra_digitada = input('Digite apenas uma letra: ')
    nTentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
    if letra_digitada in pSecreta:
         lAcertadas += letra_digitada
    
    pFormada = ''
    for lSecreta in pSecreta:
        if lSecreta in lAcertadas:
            pFormada += lSecreta
        else:
            pFormada += '*'
            
    print('Palavra formada:', pFormada)
    
    if pFormada == pSecreta:
        os.system('clear')
        print('Parabens você ganhou !!!')
        print('A palavra secreta é: ', pSecreta)
        print('Tentativas: ', nTentativas)
        break