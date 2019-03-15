#########################################################################################################
'''
012. Faça um programa que lê dois números inteiros positivos a e b. Utilizando laços, o seu programa deve cal-
cular e imprimir o valor a b .
'''
#########################################################################################################

a=int(input('Digite o número da base: '))
b=int(input('Digite o número da potência: '))
acu=1
i=1

while i<=b:
    acu=acu*a
    i=i+1

print('{}^{}={}'.format(a, b, acu))
