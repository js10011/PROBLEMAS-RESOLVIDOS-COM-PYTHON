'''Escreva um programa que serializa um objeto Python que contém data e hora em uma string JSON
usando um codificador personalizado para converter objetos datetime para formato de string ISO.'''

import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {
    'name': 'John Doe',
    'timestamp': datetime.now()
}

json_str = json.dumps(data, cls=DateTimeEncoder)
print(json_str)

'''Escreva um programa que desserializa uma string JSON em um objeto Python usando
um decoder personalizado para converter strings ISO em objetos datetime.'''
import json
from datetime import datetime

def iso_to_datetime(iso_str):
    return datetime.fromisoformat(iso_str)

def custom_decoder(dct):
    for key, value in dct.items():
        if isinstance(value, str):
            try:
                dct[key] = iso_to_datetime(value)
            except ValueError:
                pass
    return dct

json_str = '{"name": "John", "birthdate": "1990-01-01T12:00:00"}'
result = json.loads(json_str, object_hook=custom_decoder)
print(result)