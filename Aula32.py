"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

try:
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print('Número é par')
    else:
        print('Número ímpar')
except:
    print('O número não é inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_digitada = input('Digite a hora: ')

try:
    hora_digitada_inteiro = int(hora_digitada)

    if hora_digitada_inteiro >= 0 and hora_digitada_inteiro <= 11:
        print('Bom dia')
    elif hora_digitada_inteiro >= 12 and hora_digitada_inteiro <= 17:
        print('Boa tarde')
    elif hora_digitada_inteiro >=18 and hora_digitada_inteiro <=23:
        print('Boa noite')
    else:
        print('Essa hora não existe')
        
except:
    print('Digite um número inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal";  maior que 6 escreva "Seu nome é muito grande".
"""
nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >=5 and len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')