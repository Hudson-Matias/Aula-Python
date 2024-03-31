"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = '     Olha só que    ,     coisa interessante        '
lista_palavras = frase.split()
lista_frases_crua = frase.split(',') # ele corta na vírgula
lista_frases_sem_espaço = frase.split(', ') # e se eu quiser posso colocar o espaço também

lista_frases = []
for i, frase in enumerate(lista_frases_crua):
    lista_frases.append(lista_frases_crua[i].strip())

# for i, frase in enumerate(lista_frases):
#     print(lista_frases[i].strip())

# .strip() -> corta os espaços
# .rstrip() -> corta os espaços da direita
# .lstrip() -> corta os espaços da esquerda

# print(frase)
# print(lista_palavras)
# print(lista_frases_crua)
# print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
