#Operadores Relacionais

#########################################################################################################

'''
Expressões relacionais são aquelas que realizam uma comparação entre duas expressões e retornam se é o
resultado é verdadeiro ou falso.

Em Python, alguns dos operadores relacionais que temos são:
== : verifica igualdade*;
!= : verifica diferença;
> : verifica se um número é maior que o outro;
< : verifica se um número é menor que o outro;
>= : verifica se um número é maior ou igual que o outro;
<= : verifica se um número é menor ou igual que o outro.

* lembrar que um sinal apenas de igual atribui um valor a uma variável!

A saída de uma comparação é sempre True ou False
'''

#########################################################################################################


#Imprimindo uma comparação de valores.

print(8<9)
print(8>9)
print(8!=9)
print(8==9)
print(8>=9)
print(8<=9)
print('\n'*3)

#Operadores Lógicos
#########################################################################################################

'''
Expressões lógicas são aquelas que realizam uma operação lógica (ou, e, não, etc.) e retornam verdadeiro
ou falso.

Em Python são operadores lógicos:
and : operador E
or: operador OU
not: operador NÃO

sobre o not: ele retorna verdadeiro se a expressão é falsa e falso se é verdadeira.

'''

#########################################################################################################

a=0
b=0

print(a==0 and b==0)
print(a==1 or b==0)
print(a==1 or b==2)
print(not(a!=b))
print(not(a==b))

# fonte: aula04 - MC102 - 2s2018