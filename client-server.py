import socket, threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message == "quit":
                break
            print(f"\nReceived message: {message}")
        except:
            print("Error receiving messages.")
            break

def send_messages(client_socket):
    while True: 
        message = input("Enter message: ")
        if message == "quit":
            client_socket.sendall(message.encode("utf-8"))
            break
        client_socket.sendall(message.encode("utf-8"))

def start_chat_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to chat server.")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    client_socket.close()

def start_chat_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print("Chat server is listening.")

    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}.")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    host = "localhost"
    port = 12345
    
    chat_mode = input("Enter chat mode (server/client): ")
    if chat_mode == "server":
        start_chat_server(host, port)
    elif chat_mode == "client":
        start_chat_client(host, port)
    else:
        print("Invalid chat mode.")
        
