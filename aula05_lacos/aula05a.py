#COMANDOS REPETITIVOS

#########################################################################################################

'''
Quando queremos executar uma mesma tarefa várias vezes, é interessante que tenhamos um método para fazer
isso. Por exemplo: se queremos criar um programa que imprima números de 0 à 100, não é viável que façamos
1000x o comando print para cada um dos números.

Comando 'While'
Em Python, temos um comando que realiza tarefas repetitivas - o comando 'while'. Sua estrutura é muito
parecida com a do if - com a diferença que ele repete um bloco de comandos enquanto uma condição for ver-
dadeira.

{MODELO}

...

while <expressão condicional>:

    comandos

...
'''

#########################################################################################################

#Programa que imprime números de 1 à 100.

i=1

while i<=10:
    print(i, end=' ')
    i=i+1
print('\n')
#########################################################################################################

'''
Listas (análogo de vetores em C)
Um lista em Python é uma estrutura que armazena vários dados, podendo esses serem do mesmo tipo ou não.

Uma lista é criada da seguinte maneira:
<nome da variável> = [dado1, dado2, ..., dadoN]

Cada dado ocupa uma posição, sendo que a posição varia de 0 à (N-1).

Acessa-se um dos dados da lista digitando:

<nome da variável>[<posição>]
'''

#########################################################################################################

#Imprimindo os elementos de uma lista.
a=['sol', 'lua', 'cometa']
i=0

while i<=2:
    print(a[i])
    i=i+1
print('\n')
#########################################################################################################

'''
COMANDO 'for'
Para iterar sobre os itens de uma lista ou de uma string, usamos o comando for.

{Modelo}

...

for <variável> in <lista/string>:
    
    comandos
    
...


FUNÇÃO 'range'
Como sempre estamos iterando sobre valores, numéricos, o Python oferece uma função que gera uma lista 
numérica.

O comando 'range(n)' gera uma lista com valores de 0 até n-1.
O comando 'range(x,y)' gera uma lista de números de x à (y-1).
O comando 'range(x,y,z)' gera valores de x+p até y-1.
                        (basicamente ele inicia com x, o seguinte é x+p)

'''

#########################################################################################################

#Imprimindo os elementos de uma lista com o for
i=1
for i in a:
    print(i, end=' ')
print('\n')


#Imprimindo os números de 0 até 9
for i in range(10):
    print(i, end=' ')
print('\n')


#Imprimindo números de 5 até 10:
for i in range(5,11):
    print(i, end=' ')
print('\n')


#Imprimindo com incremento
for i in range(1,13,2):
    print(i, end=' ')
print('\n')


#Imprimindo a soma de N números

n=int(input('Digite a quantidade de números que deseja somar: '))

if n>=0:
    acu=0
    print('Digite os números a serem somados: \n')
    for i in range(n):
        aux=int(input( ))
        acu=acu+aux
    print('A soma é: {}'.format(acu) )

else:
    print('Você digitou um número negativo')

print('\n'*4)

#Cálculo do fatorial

f=int(input('Digite o número que deseja calcular o fatorial: '))
acu=1
i=1
while i<=f:
    acu=acu*i
    i=i+1
print('{}! = {}'.format(f, acu))