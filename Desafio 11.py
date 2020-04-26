"""
11. Leia a largura e altura de uma parede em metros, calcule sua area e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta pinta uma area de 2m2

"""

n1=int(input('Digite o primeiro tamanho da parede: '))
n2=int(input('Digite o segundo tamanho da parede: '))
a = n1 * n2
t = a / 2
print('A parede tem {}m de area, e para pintá-la é necessário {} litros de tinta.'.format(a, t))
