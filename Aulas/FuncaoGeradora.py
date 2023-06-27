# Introdução função Generator functions em python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n

        n += 1

        if n > max:
            return


gen = generator()
for n in gen:
    print(n)
