"""
Classes for Transmitting and Receiving Broadcasts over UPD
"""

import socket

class Transmitter:

    def __init__(self, port):
        self.sock_it = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Mkae Socket Broadcastable
        self.sock_it.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock_it.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.host = '<broadcast>'
        self.port = port

    def broadcast(self, msg):
        self.sock_it.sendto(msg, (self.host, self.port) )


class Receiver:

    def __init__(self, port, buffer_size=1024):
        self.sock_it = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Set socket up for receiving (and make the port sharable)
        self.sock_it.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # My modification to allow the bind address to be shared
        self.sock_it.bind( ('<broadcast>', port) )
        self.sock_it.setblocking(0)  # 0 means "do not block"

        self.port = port
        self.buffer_size = buffer_size  # bytes

    def listen(self, timeout=None):
        """ Listens until timeout, which is float in seconds """
        if timeout:
            self.sock_it.settimeout(timeout)
        try:
            msg = self.sock_it.recv(self.buffer_size)
            return msg if msg else None
        except socket.timeout as err:
            return None
