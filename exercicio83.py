'''Escreva um programa assíncrono que cria duas tarefas.

A primeira tarefa deve esperar 1 segundo e imprimir "Primeira tarefa concluída",
a segunda tarefa deve esperar 2 segundos e imprimir "Segunda tarefa concluída".
Use asyncio.create_task() para criar as tarefas e asyncio.run() para executá-las.'''
import asyncio

async def first_task():
    await asyncio.sleep(1)
    print("Primeira tarefa concluída")

async def second_task():
    await asyncio.sleep(2)
    print("Segunda tarefa concluída")

async def main():
    task1 = asyncio.create_task(first_task())
    task2 = asyncio.create_task(second_task())
    await task1
    await task2

asyncio.run(main())

'''Escreva uma função assíncrona que receba um objeto Future

e defina o resultado para ele após um atraso de 1 segundo.

Crie um loop de eventos, um objeto Future e use a função para definir o resultado.

Em seguida, exiba o resultado do Future na tela.'''
import asyncio

async def set_future_result(future):
    await asyncio.sleep(1)
    future.set_result('Result after 1 second')

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    
    await set_future_result(future)
    print(future.result())

asyncio.run(main())

'''Escreva um programa que cria um novo loop de eventos, define-o como o atual e o imprime.
Em seguida, crie outro novo loop de eventos e defina-o novamente como o atual.
Certifique-se de que está trocando corretamente os loops de eventos.'''
import asyncio

# Criamos o primeiro loop de eventos
first_event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(first_event_loop)
print("First event loop:", first_event_loop)

# Criamos o segundo loop de eventos
second_event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(second_event_loop)
print("Second event loop:", second_event_loop)

'''Escreva um programa que inicie um loop de eventos em modo infinito.
Agende a parada do loop após 3 segundos, utilizando o método call_later.
Exiba o status do funcionamento do loop antes da chamada do método stop().'''
import asyncio

def stop_loop():
    print(f"Status do loop antes de stop: {loop.is_running()}")
    loop.stop()
    print(f"Status do loop depois de stop: {loop.is_running()}")

async def main():
    loop.call_later(3, stop_loop)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()