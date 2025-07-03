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
                msg = int(msg)
                if msg <= 40:
                    salary = msg * 200
                    connection.send(f"Total Salary: {salary}".encode(format))
                else:
                    salary = 8000 + ((msg-40) * 300)
                    connection.send(f"Total Salary: {salary}".encode(format))
    connection.close()
