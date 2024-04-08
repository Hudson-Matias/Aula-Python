# Exercícios com funções

"""
Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável
"""

def multiplica(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

print(multiplica(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


"""
Crie uma função fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar
"""

def par(*args):
    for arg in args:
        if arg % 2 == 0:
            print(f'{arg} é par')
        else:
            print(f'{arg} é ímpar')

print(par(1,2,3,4,5))
