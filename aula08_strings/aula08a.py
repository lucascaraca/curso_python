#STRINGS

#########################################################################################################
'''
Em Python strings são listas imutáveis e que são representadas por uma sequência de caracteres entre as-
pas (simples ou dulplas).
Como são listas, podemos acessar cada um de seus caracteres, mas não podemos modificá-los.
obs.: o espaço é reconhecido como um caracter!
'''
#########################################################################################################

print('## Acesso a posição 4 de uma string ## \n')

a='ola como vai voce?'
print(a)
print('O 5o caracter de "{}" é "{}"'.format(a, a[4]))
print('OU... a[4]={}, onde a={}'.format(a[4], a))
print('\n'*2)

print('## O caracter "barra n" ## \n')
print('Ele pula uma linha! no comando print')
a='abc\nefc'
print(a)
print('\n'*2)

#########################################################################################################
'''
Operadores

soma ou concatenação: da mesma maneira que nas listas o operador + concatena duas strings.

repetição ou multiplicação: o operador * repete a string n vezes.

'''
#########################################################################################################

print('## Soma e multiplicação de strings ##')

a='abc'
b='def'
print('a={} e b={}'.format(a, b))
print('a+b={}'.format(a+b))
print('3*a={}'.format(3*a))
print('4*b={}'.format(4*b))
print('\n'*2)

#########################################################################################################
'''
Funções (e métodos) úteis

strip: retorna uma string sem os brancos e mudanças de linhas no início e final de uma string. Usamos es-
se método da seguinte maneira:
<string>.strip()

in: verifica se uma substring qualquer é parte de uma outra string, retornando verdadeiro ou falso. Usamos
da seguinte maneira:
<substring> in <string>

find: o método find retorna a posição onde a substring começa na string. Ele retorna -1 quando não ocorre
na string. Usamos da seguinte maneira.
<string>.find('substring')
'''
#########################################################################################################

print('## Método strip ##')
a='         Roberto de Nori não   \n            Roberto de Niro   '
print('a={}'.format(a))
print('a.strip={}'.format(a.strip()))
print('\n')

print('## Operador in ##')
sb='list'
st='listening'
print('sb={}\nst={}'.format(sb, st))
print('sb in st={}'.format(sb in st))

print('\n ## Método find ##')
print('st.find(sb)={}'.format(st.find(sb)))
print('st.find(a)={}'.format(st.find('a')))
print('\n'*2)
#########################################################################################################
'''
slipt(< sep >): separa uma string usando 'sep' como separador e retorna uma lista das substrings. Para usar esse método escrevemos:
< string >.split(< sep >)

slipt(): separa uma string usando espaço, \n e tab como indicadores de separação.

replace: o método replace troca todas as ocorrências de uma substring em uma string. Escrevemos:
< string >.replace(< substring >, < novasubstring >)

list: transforma uma string em uma lista, cujos elementos são strings. Para utilizá-la escrevemos:
list(< string >)

join: recebe uma lista e transforma em uma string utilizando o separador str (OQUE É ISSO?) Escrevemos:
str=< str >
str.join(< lista >)
'''
#########################################################################################################
print('## Método split ##')
print('Vamos usar o caracter "d" como indicador de separação!')
a='asdsjisd ijasjiad ijadashuda \n s'
print('a={}'.format(a))
print('a.split(d)={}'.format(a.split('d')))
print('a.split()={}'.format(a.split()))
print('Observe que no segundo, os espaços e "\ n" é que separam a string na lista.')
print('\n'*2)

print('## Método replace ##')
a='listening'
print('a={}'.format(a))
print('a.replace("list", "Neymar")={}'.format(a.replace('list', 'Neymar')))
print('\n'*2)

print('## Função list ##')
a='NEYMAR É TOP'
print('a={}'.format(a))
print('list(a)={}'.format(list(a)))
print('Note que os espaços em branco são tidos como caracteres!')
print('\n'*2)

print('## Método join ##')
a=['a', 'b', ' c', 'd',' e','f']
str=''
print('a={}'.format(a))
print('str=""')
print('str.join(a)={}'.format(str.join(a)))
str=" "
print('str=" "')
print('str.join(a)={}'.format(str.join(a)))
print('Join não ficou claro!!')

# This is Python 2
import sys

n = int(input())
if (n > 864000 or n < 0):
    print("ERRO")

else:
    dias = n / 86400
    n = n % 86400
    horas = n / 3600
    n = n % 3600
    minutos = n / 60
    n = n % 60
    segundos = n
    imp = str('%02d' % dias) + 'd' + str('%02d' % horas) + 'h' + str('%02d' % minutos) + 'm' + str(
        '%02d' % segundos) + 's'
    print(imp)

line = sys.stdin.readline()
print
line