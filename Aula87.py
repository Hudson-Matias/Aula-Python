# Função Lambda em Python
# A função Lambda é uma função como qualquer outra em python. Porém, são funções
# anônimas que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de
# uma única expressão.
# lista = [
#     {'Nome': 'Luiz', 'Sobrenome': 'Miranda'},
#     {'Nome': 'Maria', 'Sobrenome': 'Oliveira'},
#     {'Nome': 'Daniel', 'Sobrenome': 'Silva'},
#     {'Nome': 'Eduardo', 'Sobrenome': 'Moreira'},
#     {'Nome': 'Aline', 'Sobrenome': 'Souza'},
# ]

# lista = [4, 32, 1, 34, 5, 6, 6, 21,]
# lista.sort(reverse=True)
# sorted(lista)

lista = [
    {'Nome': 'Luiz', 'Sobrenome': 'Miranda'},
    {'Nome': 'Maria', 'Sobrenome': 'Oliveira'},
    {'Nome': 'Daniel', 'Sobrenome': 'Silva'},
    {'Nome': 'Eduardo', 'Sobrenome': 'Moreira'},
    {'Nome': 'Aline', 'Sobrenome': 'Souza'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['Nome'])
l2 = sorted(lista, key=lambda item: item['Sobrenome'])

exibir(l1)
exibir(l2)