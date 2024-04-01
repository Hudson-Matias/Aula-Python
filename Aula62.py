# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

print(*salas, sep='\n')

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

# for nome in lista:
#     print(nome, end=' ')

# p, b, *_, ap, u = lista
# print(p, ap, u)
