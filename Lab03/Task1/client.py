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

sent_msg = f"Client's IP address is {host_ip} and client's name is {hostname}"
msg_send(sent_msg)
msg_send(disconnected)