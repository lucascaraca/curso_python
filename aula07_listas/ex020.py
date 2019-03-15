#########################################################################################################
'''
020. Escreva um programa que lê 10 números ponto flutuante e os salva em uma lista. Em seguida o programa deve
calcular a média dos valores armazenados na lista e imprimir este valor
'''
#########################################################################################################
print('## Cálculo da Média ##')

#criamos uma lista vazia
v=[]

#pedimos ao usuário para digitar sua dimensão
n=int(input('Dim(v)= '))

#recebemos os valores e os armazenamos em v através do método append
for i in range(n):
    v.append(float(input('v[{}]='.format(i))))

soma=0

for i in range(n):
    soma=soma+v[i]

print('media={}'.format(soma/n))