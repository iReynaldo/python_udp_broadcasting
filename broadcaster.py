import socket

sock_it = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Makes the socket broadcastable
sock_it.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_it.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

host = '<broadcast>'
port = 6666

while True:
    msg = raw_input("Input message to send: ")

    sock_it.sendto(msg, (host, port) )
