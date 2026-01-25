'''Escreva um gerenciador de contexto assíncrono que imprima mensagens ao entrar e sair do contexto.
Dentro do contexto, faça um atraso assíncrono de 2 segundos e exiba a mensagem "Dentro do contexto".'''
import asyncio

class AsyncContextManager:
    async def __aenter__(self):
        print("Entrando no contexto")
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Saindo do contexto")

    async def do_work(self):
        await asyncio.sleep(2)
        print("Dentro do contexto")

async def main():
    async with AsyncContextManager() as manager:
        await manager.do_work()

asyncio.run(main())

'''Use a biblioteca aiofiles para criar um gerenciador de contexto assíncrono,
que abrirá um arquivo, escreverá nele a string "Gravação assíncrona no arquivo" e fechará o arquivo.'''
import aiofiles
import asyncio

async def write_to_file(filename):
    async with aiofiles.open(filename, mode='w', encoding='utf-8') as file:
        await file.write("Gravação assíncrona no arquivo")

# Exemplo de uso
async def main():
    await write_to_file("example.txt")

# Executando a função assíncrona
asyncio.run(main())

'''Escreva um iterador assíncrono que retorne números de 1 a 5 com um atraso de 1 segundo entre os números.
Use este iterador em uma função assíncrona para imprimir os números na tela.'''
import asyncio

class AsyncIterator:
    def __init__(self):
        self.current = 1

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current > 5:
            raise StopAsyncIteration
        await asyncio.sleep(1)
        value = self.current
        self.current += 1
        return value

async def main():
    async for number in AsyncIterator():
        print(number)

asyncio.run(main())

'''Escreva um gerador assíncrono que gere números de 0 a 2 com um atraso de 1 segundo entre os números.
Use este gerador em uma função assíncrona para imprimir os valores na tela.'''
import asyncio

async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i

async def main():
    async for value in async_generator():
        print(value)

asyncio.run(main())