
#criando class
class Carro:
    

    def __init__(self, fabricante, modelo, cor):
       
        self.fabricante = fabricante
        self.modelo = modelo
        self.cor = cor
    
    def descrever(self):
        """Exibe as informações do carro."""
        return f"{self.fabricante} {self.modelo} - Cor: {self.cor}"


# Criando dois objetos da classe Carro
meu_carro = Carro("Toyota", "Corolla", "Prata")
carro_amigo = Carro("Honda", "Civic", "Preto")

# Exibindo as descrições dos carros
print(meu_carro.descrever())   # Saída: Toyota Corolla - Cor: Prata
print(carro_amigo.descrever()) # Saída: Honda Civic - Cor: Preto



class Carro:
    def __init__(self, fabricante, modelo, cor):
        self.fabricante = fabricante
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0  # Novo atributo

    def acelerar(self):
        """Aumenta a velocidade."""
        self.velocidade += 10
        return f"{self.modelo} agora está a {self.velocidade} km/h."

# Criando um carro e acelerando
meu_carro = Carro("Ford", "Mustang", "Vermelho")
print(meu_carro.acelerar())  # Saída: Mustang agora está a 10 km/h.

#---------------------------------------------------------------------------------

class ContaBancaria:
    """Classe que representa uma conta bancária."""

    def __init__(self, titular, saldo_inicial=0):
        """Inicializa a conta com um titular e um saldo opcional."""
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        """Adiciona dinheiro à conta."""
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso!"
        return "O valor do depósito deve ser positivo."

    def sacar(self, valor):
        """Retira dinheiro da conta, se houver saldo suficiente."""
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado!"
        return "Saldo insuficiente ou valor inválido."

    def consultar_saldo(self):
        """Retorna o saldo atual da conta."""
        return f"Saldo atual de {self.titular}: R${self.saldo:.2f}"

# Criando uma conta bancária
conta = ContaBancaria("Maria", 500)

# Realizando operações
print(conta.consultar_saldo())  # Saída: Saldo atual de Maria: R$500.00
print(conta.depositar(200))      # Saída: Depósito de R$200.00 realizado com sucesso!
print(conta.consultar_saldo())  # Saída: Saldo atual de Maria: R$700.00
print(conta.sacar(100))         # Saída: Saque de R$100.00 realizado!
print(conta.consultar_saldo())  # Saída: Saldo atual de Maria: R$600.00
