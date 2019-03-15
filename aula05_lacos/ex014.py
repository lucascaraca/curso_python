#########################################################################################################
'''
014. Faça um programa que lê um número n e imprima os valores entre 2 e n, que são divisores de n.
'''
#########################################################################################################

i=2
n=int(input('Digite o valor de n: '))

print('Os divisores de n entre 1 e n são: ')
print('1', end=' ')
while i<n:
    a=n%i
    if a==0:
        print(str(i), end=' ')
    i=i+1

print(str(n))

print('\n \nTHE END')