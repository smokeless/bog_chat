import tkinter as tk


class App(tk.Frame):
    #let's lay out a basic ui.
    def __init__(self, master=None):
        super().__init__(master)
        self.user = 'Test@eotl.org'
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        textEntryFrame       = tk.Frame()
        channelListFrame     = tk.Frame()
        incomingMessageFrame = tk.Frame()

        #channel list in list frame
        channels = ['Auction', 'Bitch', 'Bogleg', 'Bughouse',
                    'Food', 'Game', 'Glb', 'Gossip', 'Headlines',
                    'Info', 'Linux', 'Meetings', 'Money', 'Newbie',
                    'Radio', 'Sports', 'Tech', 'Vegas']
        listBoxWidget = tk.Listbox(channelListFrame) #create wiget, put it in list frame.
        for item in reversed(channels):  #reversed for alaphabetical.
            listBoxWidget.insert(0, item)
        listBoxWidget.pack(fill='both', expand=True)

        textBox = tk.Text(textEntryFrame, height = 2, bg='red')
        label   = tk.Label(textEntryFrame, text='someone@eotl.org')
        label.pack(side='left')
        textBox.pack(side='left', fill='x', expand=True)

        sendButton = tk.Button(textEntryFrame, text='Send')
        sendButton.pack(side='right')


        channelListFrame.pack(fill='both', expand=True, side='right')
        incomingMessageFrame.pack(fill='both', expand=True, side='left')
        textEntryFrame.pack(side='bottom')




root = tk.Tk()
root.minsize(width=640, height=480)
root.title('Bog Chatter')
app = App(master=root)
app.mainloop()
