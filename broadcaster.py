
from broadcast import Transmitter

broadcaster = Transmitter(6666)

msg = raw_input("Enter message to send: ")
broadcaster.broadcast(msg)
