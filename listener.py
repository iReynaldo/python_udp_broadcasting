
from broadcast import Receiver

listener = Receiver(6666)

while True:
    msg = listener.listen(5.0)
    if msg:
        print msg
    else:
        print "Timed out"
