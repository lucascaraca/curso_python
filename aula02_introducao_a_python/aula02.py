# TIPOS PRIMITIVOS & SAÍDA DE DADOS

#Serão criadas duas variáveis: n1 e n2. Cada uma delas receberá um valor digitado pelo usuário pela função "input".
n1=input('Me fala aí um número: ')
n2=input('fala aí outro: ')

#aqui haverá a junção de n1 e n2, pois não foram definidos os tipos de variáveis de n1 e n2 - o programa as interpretará como strings.
s1=n1+n2

#haverá a impressão de s1
print('A soma vale: ', s1)

#Aqui o mesmo acontecerá, porém está estabelecido o tipo de variável - no caso, números inteiros.
n3=int(input('Me fala aí um número: '))
n4=int(input('agora fala aí outro: '))

#Como se tratam de números inteiros, a expressão abaixo somará esses números.
s2=n3+n4

#haverá a impressão de s2.
print('A soma vale:',s2)


#########################################################################################################################################
#TIPOS DE VARIÁVEIS

#O tipo primitivo de uma variável deve ser especificado. Caso contrário, ela será interpretada como string.

'''int = números inteiros (-7, 4, 0, 2);
#float = números reais (4.5, 5.7891, pi, 6.0);
#bool (booleando)= um ou outro - assume dois valores: True ou False;
#str (string) = palavras, sempre entre aspas ('Olá', '7.5', '').
'''
##########################################################################################################################################

#NOVA FORMA DE IMPRIMIR A SOMA:
print('A soma vale: {}'.format(s2))

#UTILIDADE DA FORMA

#Se quiséssemos, por exemplo imprimir a seguinte mensagem: A soma entre n2 e n3 é s2, no modelo antigo faríamos:
print('A soma entre',n3, 'e', n4, 'é:', s2)

#Já na nova fazemos:
print('A soma entre {} e {} vale: {}'.format(n3, n4, s2))


#Criação de uma nova variável, atribuindo a ela um valor digitado pelo usuário.
n5=input('Digite um valor: ')

#impressão do tipo de uma variável
print(type(n5))
#impressão de 'string'/'str', já que a variável não teve seu tipo especificado

#Corrigindo
n6=int(input('Digite outro valor: '))
print(type(n6))

#IMPRESSÃO DE UM NÚMERO INTEIRO NO FORMATO DE FLOAT
n7=float(input('Fala aí um número inteiro pra ver o que acontece: '))
print(n7)

#TESTE MAROTO
n8=int(input('OQ: '))
#Neste caso, como declaramos um número inteiro, se digitarmos um float, dará erro.
print(n8)

#VERIFICANDO SE O QUE FOI DIGITADO É NÚMERO, ALFABETO, ETC.
n10=input('Digita qqr coisa: ')

#Verifica se o que foi digitado é alfabético
print('O valor digitado é alfabético? ', n10.isalpha())
#Verifica se o que foi digitado é número
print('O valor digitado é numérico? ', n10.isalnum())

#ETC...