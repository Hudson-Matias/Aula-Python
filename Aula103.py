# Try, except, else e finally

try:
    print('ABRIR O ARQUIVO')
    # 8/0
except ZeroDivisionError:
    print('Dividiu por zero')
except IndexError as error:
    print(error.__class__.__name__)
    print(error)
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')
