import socket


address = ("localhost", 7777)
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(address)

while True:
    mystr = input("enter the string: ")
    client_sock.send(mystr.encode())
    changed_str = client_sock.recv(1024)
    print('New string: ', changed_str.decode())
client_sock.close()