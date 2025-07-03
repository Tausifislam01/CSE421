import socket

data = 16
port_num = 5060
format = "utf-8"
hostname = socket.gethostname()
host_ip_add = socket.gethostbyname(hostname)
disconnected = "Disconnect message"

server_socket_address = (host_ip_add, port_num)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)
server.listen()
print("Server is listening on port:", port_num)

while True:
    connection, address = server.accept()
    print("Connected to: ", address)

    connected = True
    while connected:
        initial = connection.recv(data).decode(format)
        print("Length of the message :", initial)

        if initial:
            message_length = int(initial)
            msg = connection.recv(message_length).decode(format)
            if msg == disconnected:
                connection.send("Goodbye. It was nice to serve you.".encode(format))
                print("Terminating the connection with:", address)
                connected = False
            else:
                vowels = "AEIOUaeiou" 
                count = 0
                for i in msg:
                    if i in vowels:
                        count += 1
                if count == 0:
                    connection.send("Not enough vowels.".encode(format))
                elif count <= 2:
                    connection.send("Enough vowels I guess.".encode(format))
                else:
                    connection.send("Too many vowels".encode(format))
    connection.close()
