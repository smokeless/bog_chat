from BogBot import BogBot
import time
from EOTLHandler import EOTLHandler



ircBot = BogBot()
eotl   = EOTLHandler()

incoming = []

while len(incoming) <= 0 and not len(incoming) > 10 :
    read = eotl.read()
    if read is not None:
        ircBot.send_txt(read)
