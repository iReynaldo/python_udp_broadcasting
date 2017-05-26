"""
Thanks to Matt Studiey

http://code.activestate.com/recipes/577278-receive-udp-broadcasts/

Super Thanks!
"""

import select
import socket

port = 6666
buffer_size = 1024
do_not_block = 0

sock_it = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_it.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # My modification to allow the bind address to be shared
sock_it.bind( ('<broadcast>', port) )
sock_it.setblocking(do_not_block)

read_list = 0  #rlist
index_of_our_socket = 0

while True:
    result = select.select([sock_it], [], [])  # When this returns it means our sock_it has something to read
    msg = result[read_list][index_of_our_socket].recv(buffer_size)
    print msg
