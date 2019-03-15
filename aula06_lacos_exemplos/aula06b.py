#########################################################################################################
'''
LAÇOS ENCAIXADOS (Continuação)

EX01. Impressão dos números primos de 0 a n. Testando apenas os números ímpares, com excessão do 2.
E imprimindo o número total de primos.
'''
#########################################################################################################

print('#### IMPRIMINDO PRIMOS ####\n')

n=int(input('Digite o número n: \n'))

print('Os números primos de {} à {} são os seguintes: '.format(0, n))

if(n>0):
    #imprime o 2, como o primeiro primo.
    print(2)
    #com a impressão do 2, a variável que conta o número de primos se inicia com 1.
    PI=1
    #atribuimos então o primeiro candidato a primo
    c=3
    while c<=n:
        #criamos a varíavel para o divisor a fim de ele ser testado!
        div=3
        #assumimos que o número é primo
        eprimo=1
        #loop que vai testar se o número é primo ou não, através de sua divisão pelos divisores.
        while(div<=c/2) and eprimo==1:
            if(c%div==0):
                eprimo=0
            #como o candidato  é impar ele não é divisivel por 2 nem por seus múltiplos,
            #por isso só testamos divisores impares também!

            div=div+2

        #se mesmo após sair do loop e primo continuar valendo 1
        if(eprimo==1):
            #imprimiremos o número primo
            print(c)
            #e o número de primos é adicionado em 1
            PI=PI+1
        c=c+2
    print('O número de primos entre {} e {} é: {}'.format(0, n, PI))

else:
    print('Você digitou um número não inteiro maior que zero, OTARIO! \nTHAU')