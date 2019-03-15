#AULA 3: OPERADORES & MALANDRAGENS DO PRINT ()

#Operadores Aritiméticos

'''
+ == soma ou junção de caractéres;
- == subtração;
* == multiplicação ou repetição de caractéres;
/ == divisão (float como resultado);
** == exponenciação;
// == divisão inteira (número inteiro como resultado);
% == resto da divisão.

a exp também pode ser feita da seguinte maneira:
Sejám a e b dois números quaisquer, então:
pwr(a,b) == a**b

#ORDEM DE PRECEDÊNCIA
1st - ()
2nd - **
3rd - *, /, //, % - faz quem aparece primeiro
4th - +, -

'''

n1=float(input('Diga um número: '))
n2=float(input('Diz aí outro: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
r=n1%n2
print('A soma entre eles é {}, a multiplicação é {}, a divisão é {}'.format(s, m, d))
print('A divisão inteira é {}. E o resto da divisão é {}'.format(di, r))


#Algumas malandragens com o print


#Juntando os dois prints acima em uma única linha
#Acrescentamos ", end=' ' - o final da primeira impressão será um espaço em branco.
print('A soma entre eles é {}, a multiplicação é {}, a divisão é {}'.format(s, m, d), end=' ')
print('A divisão inteira é {}. E o resto da divisão é {}'.format(di, r))

#Pulando linha dentro de um print
#Basta acrescentar \n no local onde se deseja pular a linha
print('A soma entre eles é {}, a multiplicação é {}, a divisão é {} \n'
      'A divisão inteira é {}. E o resto da divisão é {}'.format(s, m, d, di, r))

#Aplicação dos operadores com strings
nome=input('Digite um string: ')
nome2=input('Digite outro string: ')
n=int(input('Digite um número: '))

#Juntando dois strings
print('A junção dos strings é: ', nome+nome2)

#Imprimindo um string n vezes
print('A impressão de {} vezes o string {} é: '.format(n, nome), nome*n)

#ESTUDAR MELHOR ESSA FITA AQUI EMBAIXO

#Separando uma pontuação
print('Separando a string {} em 10 espaços do pinto final: {:10}.'.format(nome, nome))

#Alinhando a direita
print('Alinhando a string {} em 10 espaços a direita: {:>10}.'.format(nome, nome))

#Alinhando a esquerda
print('Alinhando a string {} em 10 espaços a esquerda: {:<10}.'.format(nome, nome))

#Centralizando
print(('Centralizando a string {} em 10 espaços:{:^10}.'.format(nome, nome)))

#Colocando iguais ou asteriscos em volta
print(('Olha que loco: {:=^20}'.format(nome)))