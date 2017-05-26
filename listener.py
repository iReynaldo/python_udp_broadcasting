
from broadcast import Receiver

listener = Receiver(6666)

while True:
    msg = listener.listen()
    if msg:
        print msg
