# dir, hasattr e gatattr em Python

string = 'Luiz'
metodo = 'lower' # Mas somente aqueles que não precisam passar parâmetro

if hasattr(string, metodo):
    print('Existe Upper')
    print(getattr(string, metodo)())
else:
    print(f'Não existe o método a seguir {metodo=}')