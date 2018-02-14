import telnetlib
#todo maybe implement in raw sockets would be better?
#todo this seems fine, let's use regex for our first channel.
#todo once one channel is implemented the rest should fall right into place.

class EOTLHandler(telnetlib.Telnet):
    def __init__(self, botName='bogbot'):
        super().__init__('127.0.0.1', '2010')
        self.botName  = botName
        self.password = input('Password: ')
        self.__login()
        self.__read()

    def __login(self):
        self.read_until(b'Login:')
        print('Logging in as {0}'.format(self.botName))
        self.write(self.botName.encode('utf-8')+'\n'.encode('utf-8'))
        self.read_until(b'Password:')
        print('Sending password.')
        self.write(self.password.encode('utf-8')+'\n'.encode('utf-8'))

    def __read(self):
        print('Establishing the loop.')
        while True:
            text = self.read_eager()
            if text == b'':
                pass
            else:
                print(text)

handler = EOTLHandler()