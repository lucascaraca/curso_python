#########################################################################################################
'''
007. Escrever um programa que lê três números e imprime o maior deles.
'''
#########################################################################################################

n1=float(input('Digite o primeiro número: '))
n2=float(input('Digite o segundo número: '))
n3=float(input('Digite o terceiro número: '))

if n1>=n2 and n1>=n3:

    print('{} é o maior número.'.format(n1))

if n2>n1 and n2>=n3:

    print('{} é o maior número'.format(n2))

if n3>n1 and n3>n1:

    print('{} é o maior número.'.format(n3))
