#########################################################################################################
'''
013. Faça um programa que lê um número n e que compute e imprima a soma de 1 à n.
'''
#########################################################################################################

i=1
j=1
acu=0
n=int(input('Digite o valor n de números que deseja somar: '))

while i<=n:
    acu=acu+i
    i=i+1

print('A soma de 1 à {} é: {}'.format(n, acu))
