#AULA 007

"""
Operadores Aritméticos
+ Adição
- Subtração
* Multiplicação
/ Divisão
** Potencia
// Divisão Inteira
% Resto da Divisão

"""

#Desafio
"""
print('Faremos uma divisão entre dois numeros inteiros')
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('segundo numero: '))
di = int(n1/n2)

resto = (n1%n2)
print("A divisão entre {} e {} é:{}".format (n1,n2,di))
print('O resto da divisão é: {}'.format(resto))
"""

"""
nome=input('Qual seu nome? ')
#print('Prazer em te conhecer {:20}!'.format(nome))
#print('Prazer em te conhecer {:>20}!'.format(nome))
#print('Prazer em te conhecer {:<20}!'.format(nome))
#print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

"""

n1= int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d= n1 / n2
di= n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {}, e a divisão é {:.2f}'.format(s, m, d), end=" ")
print('A divisão inteira é {}, a potencia é {}'.format(di, e))



