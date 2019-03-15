#EXEMPLOS COM LAÇOS

#########################################################################################################
'''
EX01 - MENU DE ESCOLHAS
'''
#########################################################################################################

print('####### MENU DE ESCOLHAS #######', '\n'*2)

opcao=5

while opcao != 4:
    print('1. Cadastre um produto.')
    print('2. Buscar um produto')
    print('3. Remover um produto')
    print('4. Sair')

    opcao=int(input('\nEntre com a opção desejada: '))

    if opcao==1:
        print('Cadastrando... \n')

    elif opcao==2:
        print('Buscando... \n')

    elif opcao==3:
        print('Removendo... \n')

    elif opcao==4:
        print('Seu programa será encerrado \n')

    else:
        print('Opção inválida!\n')


#########################################################################################################
'''
LAÇOS ENCAIXADOS

EX02: Impressão dos índices de uma matriz 11x6
'''
#########################################################################################################
print('\n'*2, '###### IMPRESSÃO DOS INDICES MATRICIAIS ######', '\n'*2)
for i in range(1,11):
    for j in range(1,6):
        print (i, j)

#########################################################################################################
'''
EX03: Determinar as soluções inteiras de um sistema linear do tipo:
                x1+x2=C
'''
#########################################################################################################
print('\n'*2, '###### SOLUÇÕES LINEARES INTEIRAS ######', '\n'*2)

C=int(input('Digite o valor da constante C: '))
print('\n As soluções inteiras de x1 + x2 = {} são: \n'.format(C))
for x1 in range(0, C+1):
    for x2 in range (0, C+1):
        if (x1+x2==C):
            print(x1, "+", x2, "=", C)
