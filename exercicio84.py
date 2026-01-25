'''Escreva um programa assíncrono que cria duas tarefas.
A primeira tarefa deve imprimir "Primeira tarefa" e esperar 2 segundos,
a segunda tarefa deve imprimir "Segunda tarefa" e esperar 3 segundos.
Use asyncio.create_task() para criar as tarefas e execute-as simultaneamente, esperando a conclusão de ambas.'''
import asyncio

async def task_one():
    print("Primeira tarefa")
    await asyncio.sleep(2)

async def task_two():
    print("Segunda tarefa")
    await asyncio.sleep(3)

async def main():
    task1 = asyncio.create_task(task_one())
    task2 = asyncio.create_task(task_two())

    await asyncio.gather(task1, task2)

# Iniciando o loop de eventos principal
asyncio.run(main())

'''Escreva um programa assíncrono que cria uma tarefa que espera por 5 segundos.

Execute-a, espere 1 segundo, depois cancele a tarefa e exiba uma mensagem sobre o cancelamento.
Trate a exceção CancelledError.'''
import asyncio

async def long_running_task():
    try:
        print("Task started, will sleep for 5 seconds...")
        await asyncio.sleep(5)
        print("Task completed!")
    except asyncio.CancelledError:
        print("Task was cancelled.")

async def main():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Caught task cancellation.")

asyncio.run(main())