#########################################################################################################
'''
022. A) Escreva um programa que lê uma string e imprime “Palindromo” caso a string seja um palindromo e
“Nao Palindromo”caso contrário, assumindo que a entrada é dada sem acentos e com letras minúsculas.

B) faça o mesmo para quando o usuario usa letras maiúsculas e minusculas
'''
#########################################################################################################
print('##PALÍNDROMO A## ')
st=input('Digite uma string em letras minúsculas e sem acentos: ')
print(st)

'''Para a letra B, basta adicionar a linha abaixo ao programa. Ele transformara a string toda em letras
minusculas'''
#st=st.lower()

st=st.replace(' ', '')
print(st)
invSt=''

#enquanto i estiver entre o tamanho de st - 1 (posição do último elemento da string) e -1
#diminua 1 no valor de i e armazene esses valores numa nova string
for i in range(len(st)-1, -1, -1):
    invSt=invSt + st[i]

print (invSt)

if invSt==st:
    print('Palindromo')
else:
    print('Nao Palindromo')