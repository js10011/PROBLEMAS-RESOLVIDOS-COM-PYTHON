'''
Escreva uma função que armazene informações sobre um carro
 em um dicionário. A função sempre deve receber o nome de um fabricante e um
 modelo. Um número arbitrário de argumentos nomeados então deverá ser
 aceito. Chame a função com as informações necessárias e dois outros pares
 nome-valor, por exemplo, uma cor ou um opcional. Sua função deve ser
 apropriada para uma chamada como esta: car = make_car(‘subaru’, ‘outback’,
 color=’blue’, tow_package=True) Mostre o dicionário devolvido para garantir
 que todas as informações foram armazenadas corretamente
'''
#meu codigo de bosta
def carros():
    automo ={
        'jeep':2015, 'cor' : 'verde', 'vendido':not True,
        
    }
    print(automo)
carros()

#ai
def make_car(fabricante, modelo, **info_extra):
    
    carro = {"fabricante": fabricante, "modelo": modelo}
    carro.update(info_extra)  
    return carro

car = make_car("subaru", "outback", color="blue", tow_package=True)

print(car)
