"""
Dissecando uma variável

Usando métodos.

"""

a= input('Digite algo: ')
print('O tipo primito desse valor é: ', type(a))
print('Só tem espaços? ',a.isspace())
print('É um número? ' , a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanúmerico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minusculuas? ', a.islower())
print('Está capitalizado? ', a.istitle())
