# Uncomment this to pass the first stage
import socket
import threading

BUFSIZE = 4096

def response(client):
    while input := client.recv(BUFSIZE):
        client.send(b"+PONG\r\n")


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    
    while True:
        client, address = server_socket.accept() # wait for client
        t = threading.Thread(target=response, args=(client,)) 
        t.start()

if __name__ == "__main__":
    main()
