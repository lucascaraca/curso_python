#COMANDOS CONDICIONAIS

#########################################################################################################

'''
Um comando condicional é aquele que permite decitir, a partir do resultado de uma operação relacional ou
lógica se um determinado bloco de comandos deve ou não ser executado.

Lembrando que um bloco de comandos é um conjunto de instruções agrupadas.
Em Python, um bloco de comandos é identado dentro de um comando anterior
seguido de dois pontos.
Por padrão a identação é feita com 2 espaços em branco antes de cada comando que deve estar no bloco.

Em python, os principais comandos são

if : se (verifica se uma senteça é verdadeira e se for, realiza os comandos do bloco).
else: se não / caso contrário (caso as condições anteriores não sejam satisfeitas, executa os comandos do
      seu bloco.

{MODELO}

if <expressão relacional ou lógica> :


    comandos executados se a expressão é verdadeira.


else :


    comandos executados se a expressão é falsa.


'''

#########################################################################################################


#Programa que identifica se um número é par ou ímpar
n=int(input('Digite um número inteiro: '))

if n%2==0:

    print('{} é um número par.'.format(n))

else:

    print('{} é um número ímpar'.format(n))

#O comando abaixo é executado em qqr um dos casos.
print('==FIM==')

#O mesmo programa resumido PORÉM LIXO D+
m=int(input('Digite outro inteiro: '))
print('{} é par.' if m%2==0 else'{} é impar'.format(m,m))

