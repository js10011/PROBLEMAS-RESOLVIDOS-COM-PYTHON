'''Escreva um programa que usa a classe Timer para executar uma função com atraso
e demonstre o cancelamento do timer antes que ele dispare.'''
import threading
import time

class Timer:
    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.thread = None

    def start(self):
        self.thread = threading.Timer(self.interval, self.function, self.args, self.kwargs)
        self.thread.start()

    def cancel(self):
        if self.thread:
            self.thread.cancel()

def my_function():
    print("O timer disparou!")

# Cria uma instância do Timer com intervalo de 5 segundos
t = Timer(5, my_function)

# Inicia o timer
print("Iniciando o timer")
t.start()

# Espera 2 segundos e então cancela o timer
time.sleep(2)
print("Cancelando o timer")
t.cancel()

'''Escreva um programa que utilize a classe ThreadLocal para armazenar dados únicos para cada thread'''
import threading

# Criando um objeto ThreadLocal
thread_local_data = threading.local()

# Função que trabalha com dados ThreadLocal
def process_data():
    thread_local_data.value = threading.current_thread().name
    print(f"Hello from {thread_local_data.value}")

# Função para a thread
def thread_function():
    process_data()

# Criando várias threads
threads = []
for i in range(5):
    thread = threading.Thread(target=thread_function, name=f"Thread-{i}")
    threads.append(thread)
    thread.start()

# Esperando a conclusão de todas as threads
for thread in threads:
    thread.join()