"""
06. Crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada.

"""

n1 =int(input('Digite um número, que mostraremos o dobro,triplo e raiz: '))
dobro = n1 * 2
triplo = n1 * 3
raiz= n1 ** 0.5
print('O número digita é {}, seu dobro é {}, seu triplo é {}, sua raiz quadrada é {:.2f}'.format(n1, dobro, triplo, raiz))
