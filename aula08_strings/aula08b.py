#EXEMPLOS

#########################################################################################################
'''
EX01. Faça um programa que leia um texto e:
a) conte o número de palavras nele;
b) faça a busca de todas as ocorrências de uma palavra no texto.
'''
#########################################################################################################
#criamos uma variável para armazenar o texto da pessoa
st=str(input('Digite um texto: '))
#criamos um vetor com todos os sinais de pontuação
pontuacao=['.', ',', ':', ';', '!', '?']

print('Antes do método replace!')
print(st)
#agora percorreremos o vetor pontuacao e utilizaremos a função replace, para substituir todos seus compo-
#nentes por um espaço em branco

for pont in pontuacao:
    st=st.replace(pont, '')

print('Depois do método replace!')
print(st)

#usamos agora o método split() que transforma uma string num vetor, onde cada elemento é delimitado pelos
#espaços da string e também a função len() que devolve o tamanho do vetor em questão.

numPal=len(st.split())
print('O número de palavras digitadas é: {}'.format(numPal))


#########################################################################################################
'''
EX02. Faça um programa que encontre a posição de todas as ocorrências de uma string.  
'''
#########################################################################################################

