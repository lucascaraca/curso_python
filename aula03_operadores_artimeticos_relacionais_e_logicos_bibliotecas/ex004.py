#########################################################################################################
'''
004. Faça um programa que sorteie um entre 4 alunos.
'''
#########################################################################################################

#Sorteio entre 4 alunos

import random

n1=input('Primeiro aluno: ')
n2=input('Segundo aluno: ')
n3=input('Terceiro aluno: ')
n4=input('Quarto aluno: ')

lista=[n1, n2, n3, n4]

e = random.choice(lista)

print('O escolhido foi: {}'.format(e))