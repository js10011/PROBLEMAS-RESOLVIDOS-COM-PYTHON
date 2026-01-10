'''Crie um módulo geometry.py que contenha as funções circle_area(radius) e rectangle_area(length, width).
Em seguida, importe apenas a função circle_area e use-a em outro arquivo.'''
from geometry import circle_area

radius = 5
area = circle_area(radius)
print(f"A área do círculo com raio {radius} é {area}")

'''Escreva um programa que solicita ao usuário o nome de um módulo para importar

e o nome de uma função para chamar desse módulo.

O programa deve importar dinamicamente o módulo e chamar a função especificada com qualquer argumento.

Para obter um elemento filho do módulo, use a função getattr.'''
module_name = input("Digite o nome do módulo: ")
function_name = input("Digite o nome da função: ")

module = __import__(module_name)
function = getattr(module, function_name)

function(1)