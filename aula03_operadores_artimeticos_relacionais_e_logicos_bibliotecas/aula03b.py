#IMPORTAÇÃO DE BIBLIOTECAS#

#####################################################################################################################
'''
Uma biblioteca em programação é um conjunto de algumas funções que podem ser úteis para a criação de programas.
Para obtermos uma biblioteca, utilizamos o comando "import + <biblioteca>".
Caso queiramos obtermos apenas uma das funções de uma biblioteca digitamos:
"from <biblioteca> import <função>".

Um exemplo de biblioteca muito útil é a math, que possui uma série de funções úteis - como as funções condicionais,
por exemplo.

Para vermos as funções disponíveis numa biblioteca, digitamos "<biblioteca>." e o pycharm informará as funções dela.
Para usarmos as funções diponíveis devemos digitar "<biblioteca>.<função>"

Para vermos bibliotecas disponíveis digitamos "import" e segurando ctrl apertando espaço
'''
#####################################################################################################################

import math
import random

num=int(input('Digite um número: '))
r=math.sqrt(num)
print("A raiz quadrada de {} é: {}".format(num, r))

#Assim não funciona!!
#r=sqrt(num)
#print("A raiz quadrada de {} é: {}".format(num, r))


#####################################################################################################################
'''
O que fazem algumas das funções de math
ceil: arredonda um número pra cima
floor: arredonda um número pra baixo
trunc: elimina casas decimais
pow: potência
sqrt: raiz quadrada
factorial: cálculo de fatorial
'''

#####################################################################################################################


#Usando as funções acima

print("A raiz quadrada arredondada pra cima de {} é: {}.".format(num, math.ceil(r)))

print("A raiz quadrada arredondada pra baixo de {} é: {}.".format(num, math.floor(r)))

print("A raiz quadrada truncada de {} é: {}.".format(num,math.trunc(r)))

x=float(input('Digite o número da base: '))
y=float(input('Digite o expoente: '))
p=math.pow(x,y)
print('{} elevado a {} é igual a: {}'.format(x,y,p))

#####################################################################################################################

'''
Como obter bibliotecas que não venham acompanhadas do python?
Acessando o site do Python! 
Lá há uma série de bibliotecas e as funcionalidades de suas funções.

Há também um espaço "PyPi", onde estão disponibilizadas bibliotecas criadas por outras pessoas.

Para instalá-las basta digitar "import <biblioteca>" e clicar na lampadinha vermelha que aparecer.
'''
#PRECISO ARRUMAR O INSTALADOR DE PACOTES/BIBLIOTECAS
#####################################################################################################################


n1=random.randint(1,100)
print(n1)