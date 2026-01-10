
'''Escreva a classe SimpleIterator, que irá iterar sobre a sequência de números de start até end.

Implemente os métodos __iter__ e __next__.'''

class SimpleIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

'''Escreva a classe CollectionIterator, que irá iterar sobre uma coleção arbitrária (lista, string, etc.).
Implemente os métodos __iter__ e __next__.'''
class CollectionIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.collection):
            item = self.collection[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

# Exemplos de uso:
# Para lista
ci_list = CollectionIterator([1, 2, 3, 4])
for item in ci_list:
    print(item)

# Para string
ci_string = CollectionIterator("hello")
for char in ci_string:
    print(char)