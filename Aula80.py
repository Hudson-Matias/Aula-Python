# Manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome', 'Não existe'))

if pessoa.get('sobrenome') is None:
    print('Existe')
else:
    print(pessoa['sobrenome'])
# print('ISSO Não vai')
