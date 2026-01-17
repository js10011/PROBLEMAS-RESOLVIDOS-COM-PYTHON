'''Escreva um programa que cria um servidor socket, aceita conexões de clientes que chegam e responde a eles "Hello, client!".'''
import socket

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                conn.sendall(b"Hello, client!")

start_server()
'''Escreva um programa que cria um socket cliente, conecta-se a um socket servidor, envia uma mensagem para ele e recebe uma resposta'''

import socket

def main():
    # Parâmetros do servidor
    server_host = '127.0.0.1'  # Endereço do servidor (localhost)
    server_port = 12345        # Porta do servidor

    # Criação do socket cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conexão com o servidor
        client_socket.connect((server_host, server_port))
        print(f'Conectado ao servidor {server_host}:{server_port}')

        # Mensagem a ser enviada ao servidor
        message = 'Olá, servidor!'
        client_socket.sendall(message.encode('utf-8'))
        print(f'Mensagem enviada: {message}')

        # Recebendo resposta do servidor
        response = client_socket.recv(1024).decode('utf-8')
        print(f'Resposta do servidor: {response}')

    except socket.error as e:
        print(f'Erro no socket: {e}')

    finally:
        # Fechando o socket
        client_socket.close()
        print('Conexão encerrada')

main()