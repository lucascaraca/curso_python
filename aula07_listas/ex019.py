#########################################################################################################
'''
019. Escreva um programa que lê 10 números inteiros e os salva em uma lista. Em seguida o programa deve encon-
trar a posição do maior elemento da lista e imprimir esta posição.
'''
#########################################################################################################

#66927

print('## Qual é a posição do maior número do vetor? ##')

#criamos uma lista vazia
v=[]

#pedimos ao usuário para digitar sua dimensão
n=int(input('Dim(v)= '))

#recebemos os valores e os armazenamos em v através do método append
for i in range(n):
    v.append(float(input('v[{}]='.format(i))))

#assumimos que o maior valor se encontra na posição 0.
maior=v[0]
pos=0
for i in range(n):
    for j in range(i+1, n):
        if v[j]>v[i]:
            maior=v[j]
            pos=j
print('O maior valor é o {}, que se encontra na posição {}.'.format(maior, pos))