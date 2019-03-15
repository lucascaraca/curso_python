#########################################################################################################
'''
002. Faça um programa que leia e imprima o nome da pessoa com uma mensagem de boas-vindas e a data de nas-
cimento dela. Além de cálcular a soma de dois números digitados por ela.
'''
#########################################################################################################


nome=input('Qual é o seu nome? ')
print('Olá,',nome +'.','Seja bem-vindo ao mundo de Ousadia&Alegria de Python!')

dia=input('Dia: ')
mes=input('Mês: ')
ano=input('Ano: ')

print(nome+',', 'você nasceu no dia', dia, 'de', mes,'de', ano+'.')

n1=int(input('me fala aí um número: '))
n2=int(input('me fala aí outro: '))
soma = n1 + n2
print('Esses dois feras formam: ', n1+n2)

print('A soma desses malacos é: ', soma)

