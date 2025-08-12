import random
from typing import Generator

global_game_state = {
    "modo_debug": True,
    "turno": 0
}

class Personagem:
    def __init__(self, nome: str, vida: int):
        self.nome = nome
        self.vida = vida
        self.inventario = ["Poção"]

    def atacar(self, inimigo):
        dano = random.randint(5, 15)
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano.")

    def usar_item(self):
        if "Poção" in self.inventario:
            self.vida += 10
            self.inventario.remove("Poção")
            print(f"{self.nome} usou uma Poção e recuperou 10 de vida.")
        else:
            print("Você não tem mais poções!")

class Inimigo(Personagem):
    pass

def batalha(jogador, inimigo):
    while True:
        global_game_state["turno"] += 1
        print(f"\n--- TURNO {global_game_state['turno']} ---")
        print(f"{jogador.nome}: {jogador.vida} HP | {inimigo.nome}: {inimigo.vida} HP")

        escolha = input("O que você quer fazer? (atacar / usar / fugir): ").lower()
        if escolha == "atacar":
            jogador.atacar(inimigo)
        elif escolha == "usar":
            jogador.usar_item()
        elif escolha == "fugir":
            print("Você fugiu covardemente.")
            break
        else:
            print("Comando inválido.")
            continue

        if inimigo.vida <= 0:
            print(f"{inimigo.nome} foi derrotado!")
            break

        inimigo.atacar(jogador)
        if jogador.vida <= 0:
            print(f"{jogador.nome} foi derrotado...")
            break

def iniciar_jogo():
    nome = input("Digite seu nome, guerreiro: ")
    jogador = Personagem(nome, 50)
    inimigo = Inimigo("Goblin", 30)

    try:
        batalha(jogador, inimigo)
    except Exception as e:
        print("Erro inesperado:", e)
    finally:
        print("Jogo encerrado.")

def keywords_demo():
    # Bora usar o resto das palavras-chave só pra cumprir o desafio
    def funcao_oculta():
        nonlocal_var = 10
        def interna():
            nonlocal nonlocal_var
            nonlocal_var += 1
        interna()
        return nonlocal_var

    def gerador() -> Generator[str, None, None]:
        yield "Você encontrou um tesouro!"
        yield "Mas era uma armadilha!"

    resultado = funcao_oculta()
    for msg in gerador():
        print(msg)

    valores = [1, 2, 3]
    for val in valores:
        if val % 2 == 0 and val > 0 or val == 3:
            assert val in valores
        else:
            pass

    def somar(a, b): return a + b  # lambda vibes
    dobro = lambda x: x * 2
    print("Lambda test:", dobro(4))

    class FakeContext:
        def __enter__(self):
            print("Entrando no contexto...")
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("Saindo do contexto...")

    with FakeContext() as ctx:
        print("Dentro do contexto")

    is_null = None
    if is_null is None:
        print("É None sim!")

    try:
        raise ValueError("Só pra usar o raise")
    except ValueError as e:
        print("Capturado:", e)

    True_var = True
    False_var = False
    if not False_var and True_var:
        print("Tudo certo com True e False")

    class Dummy:
        pass

    obj = Dummy()
    obj.atributo = "valor"
    del obj.atributo

    global global_game_state
    global_game_state["modo_debug"] = True

    return

# CHAMADA PRINCIPAL
if __name__ == "__main__":
    iniciar_jogo()
    keywords_demo()
