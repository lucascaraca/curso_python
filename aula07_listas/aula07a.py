#LISTAS

#########################################################################################################
'''
São construções de linguagem de programação que servem para armazenar diversos dados de forma simplifi-
cada.
Listas em Python são o análogo dos vetores em C.

É basicamente uma variável que armazena uma grande quantidade de dados.
Ex: se precisássemos armazenar 100 notas, deveríamos criar uma variável pra cada nota? (MUITO inviável)

Propriedades de listas:
. elas possuem índices inteiros, onde cada um armazena um dado.
. cada dado é acessado por meio do índice associado a ele.
. podemos editá-las: incluindo, removendo ou alterando dados

Declaração de uma lista:
<identificador/nome da variável>=[dado1, dado2, ..., dadoN]
'''
#########################################################################################################

#exemplos de listas

x=[-9, 7, 3, 10, -100] #de inteiros
y=['roberto', 2, 56.90, 10] #mista
z=['ana', 'beatriz', 'romoaldo', 'lessie'] #strings
w=[10,[10,900],'romoaldo'] #lista com lista dentro
q=[y, 2, 4]
r=[[x], q]

#########################################################################################################
'''
Índices e acesso de dados

Os índices de uma lista "correm" de 0 à n-1, onde n é o número de dados dessa lista.
Para acessar o dado correspondente a uma determinada posição, digitamos:

<identificador/nome da variável>[posição]

obs.: índices negativos se referem a lista da direita para a esquerda (começa em -1) 
'''
#########################################################################################################

#Exemplo de acessos

#EX01. Imprimindo um dado de uma lista
x=[10, 20, 30, 40, 50]

#imprima o dado da posição 3 da lista x
print(x[3])
#
#modificando o dado da posição 4 da lista x
x[4]=100
print(x, '\n'*2)

#EX02. Multiplicando dados da lista por uma constante
print('Multiplicando dados da lista por uma constante')
l=[1, 2, 3, 4, 5, 4]
for i in range(6):
    l[i]=5*l[i]
print(l, '\n'*2)

#EX03. Acesso com índices negativos
print('Acesso com índices negativos')
l=[1, 2, 3, 4]
print('l = ', l)
print('l[-1] = ', l[-1])
print('l[-2] = ', l[-2])
print('l[-3] = ', l[-3])
print('l[-4] = ', l[-4])
print('\n'*2)
#########################################################################################################
'''
Funções úteis

len(<lista>): retorna a dimensão/número de itens da lista. É normalmente usada em conjunto com o laço 
'for'.

<lista>.append(<dado>): insere um dado no final da lista.
ps.: o formato dessa função é diferente das usuais, pois ela vem depois de um ponto/comando; a este tipo
de função damos o nome de método. As diferenças entre métodos e funções serão explicadas numa aula poste-
rior.

<lista>.insert(<índice>, <dado>): insere um dado antes da posição indicada pelo índice.

del <lista>[<índice/posição>]: deleta o dado na posição indicada.

<lista>.remove(<dado>): remove o dado indicado da lista; importante: o dado deve existir na lista.
'''
#########################################################################################################

print('Imprimindo os elementos de l')
for i in range(len(l)):
    print(l[i], end=' ')
print('\n'*2)

print('Acrescentando um dado a l')
print('antes: ', l)
l.append(10)
print('depois: ', l)
print('\n'*2)
#podemos criar uma lista vazia e depois ir preenchendo ela com o comando append, de acordo com o número de
#dados necessários

print('Inserindo um dado na posição 1')
print('antes: ', l)
l.insert(1, 900)
print('depois: ', l)
print('\n'*2)

print('Deletando um dado da posição 2')
print('antes: ', l)
del l[2]
print('depois ', l)
print('\n'*2)

print('Deletando um valor específico (ex. 4)')
print('antes: ', l)
l.remove(4)
print('depois: ', l)
print('\n'*2)

#########################################################################################################
'''
Operações com listas

slicing: obter uma sublista composta dos elementos entre os indices i e j de uma lista; o comando é dado 
por:
<lista>[i:j] - imprime os dados do item i até o j-1

soma ou concatenação: gera uma nova lista, composta pela junção dos elementos de uma lista com os da outra.
o comando de soma é dado por:
<lista1>+<lista2>, onde o resultado é uma nova lista dos elementos da segunda lista grudados com o da pri-
meira

repetição ou multiplicação: gera uma nova lista, repetindo n vezes uma lista já criada. o comando é dado 
por:
<NovaLista>=n*<VelhaLista>, onde n é um inteiro maior que zero.
'''
#########################################################################################################

print('Criando uma sublista')
x=[1, 'cachorro', 90, 'leão', 'gamba maldito', '007', 0.93]
print('x=', x)
y=x[1:5]
print('x[1:5]=', y)
print('\n'*2)

print('Somando duas listas')
l1=[10, 20, 40, 50, 123]
l2=['robação', 'seriedade', 'compromisso', 'lazer']
print('l1=', l1)
print('l2=', l2)
l3=l1+l2
print('l1+l2=', l3)
print('\n'*2)

print('Repetição dos elementos de uma lista')
l=['hello', 'how u doin?']
print('l=', l)
l=3*l
print('3*l=', l)