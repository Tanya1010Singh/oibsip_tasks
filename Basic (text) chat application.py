#Server side code
import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(1)
    print("[*] Listening on 0.0.0.0:5555")

    client, addr = server.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    while True:
        message = client.recv(1024).decode('utf-8')
        print(f"Received: {message}")

        response = input("Reply: ")
        client.send(response.encode('utf-8'))

if __name__ == "__main__":
    main()

#client side code

import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    while True:
        message = input("Your message: ")
        client.send(message.encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        print(f"Server: {response}")

if __name__ == "__main__":
    main()
