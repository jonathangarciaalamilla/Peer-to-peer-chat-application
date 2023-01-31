# peer-to-peer chat system
import socket, threading

def receive_messages(sock):
    while True:
        data = sock.recv(1024).decode()
        if data == "quit":
            break
        if data:
            print(f"\nReceived: {data}")

def send_messages(sock):
    while True:
        message = input("Enter message: ")
        if message == "quit":
            sock.send("quit".encode())
            break
        if message:
            sock.send(message.encode())

def start_chat(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print(f"Connected to {host}:{port}")

    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(sock,))
    send_thread.start()

if __name__ == "__main__":
    host = input("Enter host IP address: ")
    port = int(input("Enter host port: "))
    start_chat(host, port)
