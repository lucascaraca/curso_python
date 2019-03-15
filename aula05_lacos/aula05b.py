#COMANDOS REPETITIVOS (CONT.)

#########################################################################################################

'''
Comandos 'break' e 'continue'
O comando 'break' faz com que a execução de um laço seja terminada, passando  execução pro próximo coman-
do após o laço.

Já o comando 'continue' faz com que a execução de uma laço seja alterada para o final do laço. Ele é usado
em situações onde comandos dentro do laço são executados caso alguma condição seja satisfeita.
'''

#########################################################################################################

#Imprimindo numeros de 0 à 5.
for i in range(1,11):
    if(i>5):
        break
    print(i, end=' ')
print('\n')

#Imprimindo números de 0 à 10 menos o 5.
i=1
while i<=10:
    if(i==5):
        i=i+1
        continue
    print(i, end=' ')
    i=i+1
print('\n')

#########################################################################################################

'''
Variável indicadora

Usamos uma variável indicadora quando queremos testar uma propriedade de um (conjunto de) objeto(s).
Para isso assumimos que o objeto possui essa propriedade e a testamos a fim de validar nossa hipótese 
inicial. 
'''

#########################################################################################################

#Programa que lê n números e verifica se eles estão em ordem crescente

n=int(input('Digite o número de números que irá digitar: '))
ant=float(input('Digite os números: '))
i=1
ord=1

while i<n:
    atual=float(input())
    if (atual<ant):
        ord=0#
    i=i+1
    ant=atual

if ord==0:
    print('ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRROU!')
elif ord==1:
    print('TÁ PEGANO FOGO BIXO!')

#########################################################################################################

'''
Variável contadora

Usamos uma variável contadora para contar o número de vezes que um objeto satisfaz uma determinada proprie-
dade.
'''

#########################################################################################################

#Programa que diz se um número é primo ou não

#um número é primo se seus únicos divisores são ele mesmo e 1.

n=int(input('Digite um número inteiro qualquer: '))

#criação de uma variável que irá dividir o número digitado
d=2

#variável contadora: inicia em 0 porque até então, nenhum número foi testado
div=0

while d<(n-1):
    if n%d==0:
        div=div+1
    d=d+1

if div==0:
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))
