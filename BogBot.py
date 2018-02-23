import socket
#todo: Implement command listening.
#todo: command for who is playing
#todo: command for gear info last seen
#todo: command chat to eotl


class BogBot():

    def __init__(self):
        self.server  = 'irc.freenode.net'
        self.channel = '##randononsense'
        self.nick    = 'BogBot'
        self.text    = ''
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()

    def connect(self):
        print('Firing up the stuff.')
        self.s.connect((self.server, 6667))
        self.s.send("USER {0} {1} {2} :Bogleg!\n".format(self.nick, self.nick, self.nick).encode('utf-8'))
        self.s.send('NICK {0} {1}'.format(self.nick, '\n').encode('utf-8'))
        self.s.send('JOIN {0} {1}'.format(self.channel, '\n').encode('utf-8'))
        print('All fired.')

    def rcv_clean_txt(self):
        text = self.s.recv(2040)
        return self.__process_txt(text)

    def __process_txt(self, txt):
        #:someguy!~someguy@127.0.0.1 PRIVMSG ##randononsense :hello
        #todo make this not some ugly nightmare in formatting txt.
        userV    = ''
        channelV = ''
        chatV    = ''
        try:
            textTuple =  txt.partition(b'!')
            userV     = textTuple[0].decode().strip('#:')
            textTuple = txt.partition(b'##')
            channelV  = textTuple[-1].decode()
            channelV  = channelV.split(':')
            chatV     = channelV[1].strip()
            channelV  = channelV[0].strip()

            return '{0}@{1}: {2}'.format(userV, channelV, chatV)
        except:
            return txt

    def send_txt(self, text:str):
        toSend = text.encode('utf-8')
        formatted = b'PRIVMSG ' + self.channel.encode('utf-8') + b' ' + b':' + toSend + b'\n'
        self.s.send(formatted)
