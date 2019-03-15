#########################################################################################################
'''
017. Faça um programa que imprima uma matriz quadrada de ordem n, onde os elementos das diagonais são '+'
e os demais '*'.
'''
#########################################################################################################
n=int(input('Digite a ordem da matriz: '))

for i in range(1, n+1):
    for j in range(1, n+1):

        if i!=j:
            print('*', end='  ')

        else:
            print('+', end='  ')
    print('\n')