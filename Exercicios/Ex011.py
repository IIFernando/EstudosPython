def multiplica(*args):
    
    total = 1
    for n in args:
        total *= n
    return total

multiplicacao = multiplica(10, 2, 3, 4, 5)

print(multiplicacao)
