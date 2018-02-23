from BogBot import BogBot
import time
from EOTLHandler import EOTLHandler



ircBot = BogBot()
eotl   = EOTLHandler()

while True:
    read = eotl.read()
    if read is not None:
        ircBot.send_txt(read)
