primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if (primeiro_valor > segundo_valor):
    print(f'O primeiro valor é "{primeiro_valor}" maior que o segundo valor "{segundo_valor}"')
elif(primeiro_valor < segundo_valor):
    print(f'O segundo valor é "{segundo_valor}" maior que o primeiro valor "{primeiro_valor}"')
else:
    print('Os valores são iguais')