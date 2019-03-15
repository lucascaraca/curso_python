#########################################################################################################
'''
Quando ações são vendidas ou compradas por meio de um corretor, a comissão do corretor é muitas vezes
calculada usando uma escala que depende do valor das ações negociadas. Escreva um programa que calcule
o valor da comissão a partir do valor da transação informado pelo usuário, sabendo-se que o corretor
cobra os valores indicados abaixo e que a comissão mínima é de R$ 39,00:

Até R$ 2.500,00, comissão de R$30+1,7%
R$2.500,01 até R$6.250,00, comissão de R$56 + 0,66%
R$6.250,01 até R$20.000,00, comissão de R$76 + 0,34%
R$20.000,01 até R$50.000,00, comissão de R$100 + 0,22%
R$50.000,01 até R$500.000,00, comissão de R$155 + 0,11%
Mais que R$ 500.000,00, comissão de R$255 + 0,09%
'''
#########################################################################################################

v=float(input('Entre com o valor em reais das ações negociadas: R$ '))

if (v<=529.41):
    print('O valor da comissão é de R$ 39.00')

elif (v>529.41 and v<=2500):
    v=0.017*v
    print('O valor da comissão é de R$ {}'.format(v + 30))

elif (v>2500 and v<=6250):
    v=0.0066*v+56
    print('O valor da comissão é de R$ {}'.format(v))

elif (v>6250 and v<=20000):
    v=0.0034*v+76
    print('O valor da comissão é de R$ {}'.format(v))

elif (v>20000 and v<=50000):
    v=0.0022*v+100
    print('O valor da comissão é de R$ {}'.format(v))

elif (v>50000 and v<=500000):
    v=0.0011*v+155
    print('O valor da comissão é de R$ {}'.format(v))

else:
    v=0.0009*v+255
    print('O valor da comissão é de R$ {}'.format(v))

