"""

08. Escreva um programa que leia um valor em metros eo exiba convertido em  centimetros e milimetros

"""


n1 = int(input('Digite um valor em metros , para ser convertido em cm e mm: '))
cm = n1 * 100
mm = n1 * 1000
print('{}m, equivale a {}cm e {}mm  '.format(n1, cm, mm))
