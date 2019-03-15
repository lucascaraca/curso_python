#########################################################################################################
'''
009. Refazer o ex008 utilizando ELIF.
'''
#########################################################################################################

n1=float(input('Digite um número: '))
n2=float(input('Digite um número: '))
n3=float(input('Digite um número: '))

if n1<=n2 and n1<=n3:

    if n2<=n3:
        print('{}, {}, {}'.format(n1, n2, n3))
    else:
        print('{}, {}, {}'.format(n1, n3, n2))

elif n2<n1 and n2<=n3:

    if n1<=n3:
        print('{}, {}, {}'.format(n2, n1, n3))
    else:
        print('{}, {}, {}'.format(n2, n3, n1))

elif n3<n1 and n3<n2:

    if n1<=n2:
        print('{}, {}, {}'.format(n3, n1, n2))
    else:
        print('{}, {}, {}'.format(n3, n2, n1))
