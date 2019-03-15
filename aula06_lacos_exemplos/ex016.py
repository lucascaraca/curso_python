#########################################################################################################
'''
016. Faça um programa que leia um número n e imprima n linhas na tela
com o seguinte formato (exemplo se n = 6):
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
'''
#########################################################################################################

n=int(input('Digite um número inteiro: '))

for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print('\n')