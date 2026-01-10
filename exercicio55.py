'''Escreva uma função check_positive que recebe um número e verifica se ele é positivo.
Se o número for negativo ou igual a zero, a função deve lançar uma exceção ValueError com a mensagem "Number must be positive".'''
def check_positive(number):
    if number <= 0:
        raise ValueError("Number must be positive")
    return True

    '''Escreva uma função validate_input que aceita uma string e verifica se ela não está vazia e se seu comprimento não excede 10 caracteres.
Se a string estiver vazia, lance um ValueError com a mensagem "Input cannot be empty".
Se a string for muito longa, lance um ValueError com a mensagem "Input is too long".
Em seguida, capture essa exceção e reembale-a em uma exceção personalizada InputValidationError, preservando a exceção original como a causa.'''
class InputValidationError(Exception):
    def __init__(self, message, original_exception):
        super().__init__(message)
        self.original_exception = original_exception

def validate_input(input_str):
    try:
        if not input_str:
            raise ValueError("Input cannot be empty")
        if len(input_str) > 10:
            raise ValueError("Input is too long")
    except ValueError as e:
        raise InputValidationError("Validation error occurred", e)

# Exemplo de uso:
try:
    validate_input("")
except InputValidationError as e:
    print(f"Caught custom exception: {e}")
    print(f"Original exception: {e.original_exception}")

'''Crie uma exceção personalizada InvalidAgeError, que será chamada na função check_age,
se a idade for menor que 0 ou maior que 150. Trate essa exceção no bloco try-except.'''
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(f"Invalid age: {age}")

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer for age.")

'''Crie uma classe base de exceções chamada ApplicationError e duas subclasses NegativeValueError e ValueTooLargeError.
Implemente a função check_number, que irá lançar a exceção correspondente se o número for negativo ou muito grande.
Trate as exceções no bloco try-except.'''
class ApplicationError(Exception):
    pass

class NegativeValueError(ApplicationError):
    pass

class ValueTooLargeError(ApplicationError):
    pass

def check_number(number):
    if number < 0:
        raise NegativeValueError("The value is negative.")
    elif number > 100:
        raise ValueTooLargeError("The value is too large.")
    else:
        return "The value is acceptable."

try:
    num = int(input("Enter a number: "))
    result = check_number(num)
    print(result)
except NegativeValueError as e:
    print(f"Error: {e}")
except ValueTooLargeError as e:
    print(f"Error: {e}")
except ApplicationError as e:
    print(f"An application error occurred: {e}")