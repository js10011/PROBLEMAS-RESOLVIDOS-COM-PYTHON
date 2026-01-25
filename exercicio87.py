'''Escreva um programa que cria 4 processos paralelos.

Cada processo deve imprimir seu próprio nome e o identificador atual do processo.
Use o módulo multiprocessing.'''
import multiprocessing
import os

def worker(name):
    print(f'Process name: {name}, PID: {os.getpid()}')


processes = []
for i in range(4):
    process_name = f'Process-{i+1}'
    p = multiprocessing.Process(target=worker, args=(process_name,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

'''Escreva um programa assíncrono que execute 30 tarefas em paralelo.

Cada tarefa deve esperar 2 segundos e, em seguida, exibir sua mensagem "Task n done", onde n é o número da tarefa.

Use o módulo asyncio.'''
import asyncio

async def task(n):
    await asyncio.sleep(2)
    print(f"Task {n} done")

async def main():
    tasks = [task(i) for i in range(1, 31)]
    await asyncio.gather(*tasks)

asyncio.run(main())