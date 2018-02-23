import telnetlib

#todo maybe implement in raw sockets would be better?

#What we're looking for:
#(Group) Helig has been invited to join the group.
#Seneo clambers onto its feet. This gives us the person to look at.
#((Newbie)) Bogbot: so where's the main idle hangout?
class EOTLHandler(telnetlib.Telnet):
    def __init__(self, botName='bogbot'):
        super().__init__('127.0.0.1', '2010')
        self.botName  = botName
        self.password = input('Password: ')
        self.__login()

    def __login(self):
        self.read_until(b'Login:')
        print('Logging in as {0}'.format(self.botName))
        self.write(self.botName.encode('utf-8')+'\n'.encode('utf-8'))
        self.read_until(b'Password:')
        print('Sending password.')
        self.write(self.password.encode('utf-8')+'\n'.encode('utf-8'))
        self.write(b'tell grouper invite\n')
        self.write(b'group accept\n')

    def read(self):
        text = self.read_until(b'\n').strip()
        if text == b'':
            pass
        elif text is None:
            pass
        else:
            return(self.__parse_txt(text))

    def __parse_txt(self, text: b''):
        # todo Refactor this section.
        name = self.botName  # so we can sort out or own messages?
        newbieChannelTag = b'((Newbie))'
        groupChannelTag = b'(Group)'

        if text[0:len(newbieChannelTag)] == newbieChannelTag:
            textTuple = text.partition(b':')  # split the text up
            cleanGroup = textTuple[0].split()  # split it up more.
            charName = cleanGroup[1].strip()  # extract charname
            message = textTuple[-1].strip()  # extract message.
            return self.format_message([charName, b'Newbie', message])

        elif text[0:len(groupChannelTag)] == groupChannelTag:
            textTuple = text.partition(b':')  # split the text up
            cleanGroup = textTuple[0].split()  # split it up more.
            charName = cleanGroup[1].strip()  # extract charname
            message = textTuple[-1].strip()  # extract message.
            return self.format_message([charName, b'Group', message])
        else:
            pass

    def format_message(self, textIn:list)->str:
        '''
        Takes the text and formats it to be readable for sending around.
        :param textIn: list[0] char, [1] channel, [2] message.
        :return:
        '''
        #todo maybe byte string? Think about this stuff.
        clean = '{0}@eotl.org*{1}* {2}'.format(textIn[0].decode(), textIn[1].decode(), textIn[2].decode())
        return clean

    def send_message(self, text):
        self.write(text.encode() + b'\n')
