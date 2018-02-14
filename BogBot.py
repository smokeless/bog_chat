import socket
import re

class BogBot():

    def __init__(self):
        self.server  = 'irc.freenode.net'
        self.channel = '##randononsense'
        self.nick    = 'BogBot'
        self.text    = ''
        #self.connect()

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Firing up the stuff.')
        self.s.connect((self.server, 6667))
        self.s.send("USER {0} {1} {2} :Bogleg!\n".format(self.nick, self.nick, self.nick).encode('utf-8'))
        self.s.send('NICK {0} {1}'.format(self.nick, '\n').encode('utf-8'))
        self.s.send('JOIN {0} {1}'.format(self.channel, '\n').encode('utf-8'))

    def rcv_clean_txt(self):
        #text = self.s.recv(2040)
        text = b'#:smokeless!~smokeless@c-24-23-128-114.hsd1.ca.comcast.net PRIVMSG ##randononsense :hello'
        #Need to parse this out.
        #Currently looks like: #randononsense :I've got my network code working.
        #Should look like: #nick@channel: I've got my network code working.
        #moved to process txt function
        clean = self.__process_txt(text)
        return clean

    def __process_txt(self, txt):
        #:smokeless!~smokeless@c-24-23-128-114.hsd1.ca.comcast.net PRIVMSG ##randononsense :hello
        #todo make this not some ugly nightmare in formatting txt.
        textTuple =  txt.partition(b'!')
        userV     = textTuple[0].decode().strip('#:')
        textTuple = txt.partition(b'##')
        channelV  = textTuple[-1].decode()
        channelV  = channelV.split(':')
        channelV  = channelV[0]
        print(textTuple)
        print(userV)
        print(channelV)

bot = BogBot()
bot.rcv_clean_txt()