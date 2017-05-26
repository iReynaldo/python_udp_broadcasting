
from broadcast import Transmitter

broadcaster = Transmitter(6666)

while True:
    msg = raw_input("Enter message to send: ")
    broadcaster.broadcast(msg)
