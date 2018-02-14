import telnetlib
import re
#todo maybe implement in raw sockets would be better?
#todo this seems fine, let's use regex for our first channel.
#todo once one channel is implemented the rest should fall right into place.

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

    def __parse_txt(self, text:b''):
        #todo Maybe change this to regex.
        #todo Refactor this section.
        name = self.botName #so we can sort out or own messages?
        newbieChannelTag = b'((Newbie))'
        groupChannelTag = b'(Group)'

        if text[0:len(newbieChannelTag)] == newbieChannelTag:
            print('newbie')
        elif text[0:len(groupChannelTag)] == groupChannelTag:
            print('group')
            textTuple = text.partition(b':') #split the text up
            cleanGroup = textTuple[0].split()#split it up more.
            charName = cleanGroup[1].strip() #extract charname
            message = textTuple[-1].strip()  #extract message.
            print(charName, message)

    def format_message(self, textIn:list)->str:
        '''
        Takes the text and formats it to be readable for sending around.
        :param textIn: list[0] char, [1] channel, [2] message.
        :return:
        '''
        #todo maybe byte string? Think about this stuff.
        clean = '{0}@eotl.org::{1}:: {2}'.format(textIn[0], textIn[1], textIn[2])

handler = EOTLHandler()