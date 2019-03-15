#EXEMPLOS

#########################################################################################################
'''
Fazer um programa que calcule o produto interno de dois vetores de dimensão n.
'''
#########################################################################################################
print('Produto Interno entre dois vetores \n')

acu=0.0
n=int(input('Entre com a dimensão dos vetores: '))
v1=n*[0]
v2=n*[0]

print('Entre com as coordenadas do vetor1: ')

for j in range(n):
    v1[j]=float(input('v1[{}]='.format(1+j)))

print('Entre com as coordenadadas do vetor2: ')

for i in range(n):
    v2[i]=float(input('v2[{}]='.format(1+i)))

i=0
while i<n:
    acu=acu+v1[i]*v2[i]
    i=i+1

print('v1[].v2[]={}'.format(acu))
print('\n')
#OBS.: é possível fazer de outra forma, iniciando dois vetores vazios e usando o comando append para adi-
#elementos no loop for
ei=0
print('Elementos iguais')
for i in range(n):
    for j in range(n):
        if v1[i]==v2[j]:
            ei=1
            print('O elemento v1[{}] é igual ao elemento v2[{}]'.format(i, j))
if ei==0:
    print('Não há elementos iguais.')