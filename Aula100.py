# Introdução às Generator functions em Python
# Generator  = (n for n in range(10000))

def generator(n=0, maximun=10):
    while True:
        yield n
        n += 1

        if n >= maximun:
            return

gen = generator(maximun=10000)
for n in gen:
    print(n)
