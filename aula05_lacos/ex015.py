#########################################################################################################
'''
015. Faça um programa que lê um número n e que compute e imprima a "dupla".
'''
#########################################################################################################

i=1
j=1
acu=0
n=int(input('Digite o valor n de números que deseja somar: '))

while j<=n:
    while i<=j:
        acu=acu+i
        i=i+1
    j=j+1
    i=1


print(acu)
