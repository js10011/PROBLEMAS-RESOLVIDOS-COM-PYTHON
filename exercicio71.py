'''Escreva uma classe que gerencie sua serialização usando o método __reduce__(),
para que ao serializar e desserializar sejam mantidos apenas certos campos.'''
import pickle

class CustomSerializable:
    def __init__(self, name, age, password, hidden_info):
        self.name = name
        self.age = age
        self.password = password
        self.hidden_info = hidden_info

    def __reduce__(self):
        return self._serialize, (self.name, self.age)

    @staticmethod
    def _serialize(name, age):
        return CustomSerializable(name, age, None, None)

# Criação do objeto
obj = CustomSerializable("John Doe", 30, "supersecret", "hidden")

# Serialização
serialized_obj = pickle.dumps(obj)

# Desserialização
deserialized_obj = pickle.loads(serialized_obj)

# Verificação
print(f"Name: {deserialized_obj.name}, Age: {deserialized_obj.age}")
print(f"Password: {deserialized_obj.password}, Hidden Info: {deserialized_obj.hidden_info}")

'''Escreva uma classe que contenha campos não serializáveis, como arquivos abertos ou bancos de dados,
e implemente os métodos __getstate__() e __setstate__(),
para excluir esses campos durante a serialização e restaurá-los durante a desserialização.'''
import pickle

class MyClass:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath, 'r')
        self.data = self.file.read()
    
    def __getstate__(self):
        state = self.__dict__.copy()
        # Remove o atributo file do estado para prevenir a serialização
        del state['file']
        return state
    
    def __setstate__(self, state):
        self.__dict__.update(state)
        # Reabre o arquivo na desserialização
        self.file = open(self.filepath, 'r')
        self.data = self.file.read()
    
    def __del__(self):
        self.file.close()

# Exemplo de uso:
obj = MyClass('example.txt')
serialized_obj = pickle.dumps(obj)
deserialized_obj = pickle.loads(serialized_obj)
print(deserialized_obj.data)