'''Escreva um programa que cria um objeto Future e define um resultado para ele após 3 segundos.
Use o método set_result para definir o resultado e imprima o resultado do objeto Future após sua conclusão.'''
import asyncio

async def set_future_result(fut):
    await asyncio.sleep(3)
    fut.set_result('Hello, Future!')

async def main():
    fut = asyncio.Future()
    await asyncio.gather(set_future_result(fut))
    print(fut.result())

asyncio.run(main())

'''Escreva um programa que cria um objeto Future e configura uma exceção para ele após 2 segundos.
Use o método set_exception para configurar a exceção e trate essa exceção após sua ocorrência.'''
import asyncio

async def set_future_exception(future):
    await asyncio.sleep(2)
    future.set_exception(Exception("An error has occurred"))

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    
    asyncio.create_task(set_future_exception(future))

    try:
        await future
    except Exception as e:
        print(f"Exception occurred: {e}")

asyncio.run(main())