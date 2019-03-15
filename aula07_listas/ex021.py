#########################################################################################################
'''
021. Escreva um programa que lê 10 números inteiros e os salva em uma lista. Em seguida o programa deve ler um
outro número inteiro C . O programa deve então encontrar dois números de posições distintas da lista cuja
multiplicação seja C e imprimı́-los. Caso não existam tais números, o programa deve informar isto.
'''
#########################################################################################################

print('## Múltiplos de C ##')

#mesmos comentários dos exercícios anteriores
v=[]
n=int(input('Dim(v)='))

for i in range(n):
    v.append(float(input('v[{}]='.format(i))))

c=int(input('C='))
t=0
#o loop abaixo pegara cada um dos elementos i do vetor e irá testá-los com os elementos nas posições j>i
#a fim de verificar se multiplicados resultam em c
for i in range(n):
    for j in range(i, n):
        #caso resulte em c, o programa irá imprimir os valores e mudará o valor de t (indicadora) para 1
        if v[i]*v[j]==c:
            print('Os números que multiplicados resultam em {} são: {} e {}'.format(c,v[i],v[j]))
            t=1
#se após o loop acima t continuar valendo 0 (sendo falso), o programa imprime que não há multiplos de c
if t==0:
    print('Não há tais números na lista')