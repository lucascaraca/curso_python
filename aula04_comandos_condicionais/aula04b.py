#IF-ELSE && IF-ELSE-IF
#########################################################################################################

'''
Como o Python executa os comandos por linhas, ao utilizarmos uma série de "ifs", como no ex008, mesmo a 
primeira opção sendo verdadeira, o programa executará e verificará as outras linhas.

Quando dois times empatam no Brasileirão, há criterios de desempate que seguem uma certa ordenação:
o número de vitórias, saldo de gols, gols feitos, etc. Se um desses critérios é satisfeito, os outros não
precisam ser analisdos.

Suponha por exemplo que o time 1 e o time 2 estejam empatados. O time 1 tem mais vitórias que o time 2,
mas o saldo de gols do time 2 é maior que o do time 1.
Caso fizéssemos um programa somente com ifs, na verificação da primeira condição (vitórias ele daria a
vitória para o time 1, mas, ao verificar a segunda condição, ele daria a vitória ao time 2.

'''

#########################################################################################################


#REFAZENDO O EX008 COM ELSE

n1=float(input('Digite um número: '))
n2=float(input('Digite um número: '))
n3=float(input('Digite um número: '))

if n1<=n2 and n1<=n3:

    if n2<=n3:
        print('{}, {}, {}'.format(n1, n2, n3))
    else:
        print('{}, {}, {}'.format(n1, n3, n2))

else:
    if n2<n1 and n2<=n3:

        if n1<=n3:
            print('{}, {}, {}'.format(n2, n1, n3))
        else:
            print('{}, {}, {}'.format(n2, n3, n1))

    else:
        if n3<n1 and n3<n2:

            if n1<=n2:
                print('{}, {}, {}'.format(n3, n1, n2))
            else:
                print('{}, {}, {}'.format(n3, n2, n1))


#########################################################################################################

'''
Ao invés de digitarmos:

...
else:
    if <condição>:
    ...

Podemos digitar:

...

elif <condição>:

    ...

...

elif <condição>:

    ...
        
else:
#ESTE ULTIMO ELSE PARA UMA CONDIÇÃO QUE NÃO SEJA RESPEITADA POR NENHUMA DAS ANTERIORES.
'''

#########################################################################################################
