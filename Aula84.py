# Sets - conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# Representados graficamente pelo diagrama de Venn
# Sets em Python são imutáveis, 
# porém aceitam apenas tipos imutáveis como valor interno

# Criando um set
# set(iterável) ou {1, 2, 3}
s1 = set('Luiz')
s1 = set() # vazio
s1 = {'Luiz', 1, 2, 3} # com dados

# Sets são eficientes para remover valores duplicados de iteráveis
# - não aceitam valores mutáveis;
# - seus valores são sempre únicos;
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
s1 = {1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#     print(numero)

# Métodos úteis:
# CRUD
s1 = set()
s1.add('Luiz') # a função add para o set só aceita um valor
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4)) # ele adiciona de forma iterada, para eu passar uma frase eu mando um iterável em si
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
# print(s1)

# Operadores úteis:
# União | união (union) - Une
# Intersecção & (intersection) - Itens presentes em ambos
# Diferença - Itens presentes apenas no set da esquerda
# Diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)
