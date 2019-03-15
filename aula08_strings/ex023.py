#########################################################################################################
'''
023. A)O usuário entra cinco números separados por brancos. Imprima a média deles.
B) O usuário entra com vários números separados por branco ou virgula, por exemplo “3,4 5 6, 9” . Imprima
a média deles.
'''
#########################################################################################################

print('## A) Média ##\n')

st=input('Digite os números que deseja calcular a média separados por espaços: ')
print('Os números digitados foram: {}'.format(st))

st=st.split()
print('A conversão da string digitada em lista é: {}'.format(st))
soma=0

for i in range(len(st)):
    soma=soma+float(st[i])

print('A média dos números digitados é: {}'.format(soma/len(st)))




print('## B) Média 2 ## \n')

st1=input('Digite os números que deseja calcular a média separados por vírgulas ou espaços: ')

print('A string digitada foi st1={}'.format(st1))
st1=st1.replace(',', ' ')

print('Substituindo todas as vírgulas de st1 por espaços em branco, temos st1={}'.format(st1))

st1=st1.split()
print('Transformando st1 em lista, utilizando espaços em branco como separação temos: {}'.format(st1))

soma=0
for i in range(len(st1)):
    soma=soma+float(st1[i])

print('A média dos números digitados é: {}'.format(soma/len(st1)))


