#########################################################################################################
'''
011. Faça um programa que imprima um menu de 4 pratos na tela e uma quinta opção para sair do programa. O
programa deve imprimir o prato solicitado. O programa deve terminar quando for escolhida a quinta opção.
'''
#########################################################################################################
print('Restaurante Neymar Jr. ','\n'*2,'Escolha sua opção!')
e=0
while e!=6:
    print('1. Lanche TOP')
    print('2. Refri Rapaziada')
    print('3. Bobs Esponja')
    print('4. Pagode')
    print('5. Sair')
    e=int(input('Digite sua opção: '))
    if e==1:
        print('Você escolheu um Lanche TOP!')
        print('1. Sim \n 2. Não')
        c=int(input('Confirma?'))
        if c==1:
            print('Lanche TOP confirmado!')
        else:
            print('Lanche TOP cancelado! :(')

    elif e==2:
        print('Você escolheu um Refri Rapaziada')
        print('1. Sim \n 2. Não')
        c = int(input('Confirma?'))
        if c == 1:
            print('Refri Rapaziada confirmado!')
        else:
            print('Refri Rapaziada cancelado! :(')

    elif e == 3:
        print('Você escolheu um Bobs Esponja')
        print('1. Sim \n 2. Não')
        c = int(input('Confirma?'))
        if c == 1:
            print('Bobs Esponja confirmado!')
        else:
            print('Bobs Esponja cancelado! :(')

    elif e == 4:
        print('Você escolheu Pagode')
        print('1. Sim \n 2. Não')
        c = int(input('Confirma?'))
        if c == 1:
            print('Pagode confirmado!')
        else:
            print('Pagode cancelado! :(')

    else:
        break

print('\n'*3,'É TOISS!')