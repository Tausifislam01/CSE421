import socket

format = "utf-8"
port = 5060
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
data = 16
server_socket_address = (host_ip, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_address)
disconnected = "Disconnect message"
def msg_send(msg):

    message = msg.encode(format)  
    msg_length = len(message) 
    msg_length = str(msg_length).encode(format)  
    msg_length += b" " * (data - len(msg_length))
    client.send(msg_length)
    client.send(message)
    print(client.recv(2048).decode(format))

while True:
    inp = input("Enter Input: ")
    if inp == "End":
        msg_send(disconnected)
        break
    else: 
        msg_send(inp)