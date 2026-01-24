'''Escreva um programa que crie e execute várias funções assíncronas, cada uma usando o operador await para aguardar a conclusão de outra função assíncrona.'''
import asyncio

async def async_function_1():
    print("Início async_function_1")
    await asyncio.sleep(2)
    print("Conclusão async_function_1")

async def async_function_2():
    print("Início async_function_2")
    await asyncio.sleep(1)
    print("Conclusão async_function_2")

async def main():
    print("Início main")
    task1 = asyncio.create_task(async_function_1())
    task2 = asyncio.create_task(async_function_2())
    
    await task1
    await task2
    print("Conclusão main")

asyncio.run(main())

'''Escreva um programa que utilize asyncio.gather() para executar várias tarefas assíncronas paralelamente e reunir seus resultados.'''
import asyncio

async def task1():
    await asyncio.sleep(1)
    return "Resultado da task1"

async def task2():
    await asyncio.sleep(2)
    return "Resultado da task2"

async def main():
    results = await asyncio.gather(task1(), task2())
    print(results)

asyncio.run(main())

'''Escreva um programa assíncrono que exibe "Início" na tela, faz uma pausa de 3 segundos,

exibe "Em progresso", faz uma pausa novamente de 2 segundos e exibe "Fim".
Use o método asyncio.run() para executar a coroutine principal.'''
import asyncio

async def main():
    print("Início")
    await asyncio.sleep(3)
    print("Em progresso")
    await asyncio.sleep(2)
    print("Fim")

asyncio.run(main())

'''Escreva uma função assíncrona que receba uma string e um atraso em segundos, e depois exiba a string após o atraso especificado.

Crie duas tasks, cada uma chamando essa função com strings e atrasos diferentes.

Execute-as simultaneamente usando o método asyncio.run().'''
import asyncio

async def delayed_print(text, delay):
    await asyncio.sleep(delay)
    print(text)

async def main():
    task1 = asyncio.create_task(delayed_print("Hello after 2 seconds", 2))
    task2 = asyncio.create_task(delayed_print("Hello after 5 seconds", 5))
    await task1
    await task2

asyncio.run(main())