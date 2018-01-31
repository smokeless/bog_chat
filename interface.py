import tkinter as tk


class App(tk.Frame):
    #let's lay out a basic ui.
    def __init__(self, master=None):
        super().__init__(master)
        self.user = 'Test@eotl.org'
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        chatFrame = tk.Frame(self, relief='ridge', borderwidth=2)
        listFrame = tk.Frame(self, relief='ridge', borderwidth=2)
        incomingTextFrame = tk.Frame(self, relief='ridge', borderwidth=2)

        #channel list in list frame
        channels = ['Auction', 'Bitch', 'Bogleg', 'Bughouse',
                    'Food', 'Game', 'Glb', 'Gossip', 'Headlines',
                    'Info', 'Linux', 'Meetings', 'Money', 'Newbie',
                    'Radio', 'Sports', 'Tech', 'Vegas']
        listBoxWidget = tk.Listbox(listFrame) #create wiget, put it in root
        for item in reversed(channels):  #reversed for alaphabetical.
            listBoxWidget.insert(0, item)
        listBoxWidget.pack(expand = True, fill='y', side='right')


        chatBoxWidget = tk.Label(incomingTextFrame, text='text')
        chatBoxWidget.pack(expand = True, side='top')

        userLabelWidget = tk.Label(chatFrame, text=self.user)
        userLabelWidget.pack(side='left')

        textEntryWidget = tk.Text(chatFrame, height = 2)
        textEntryWidget.focus_set()
        textEntryWidget.config(highlightbackground='RED')
        textEntryWidget.pack(expand = True, fill='x', side='bottom')
        chatFrame.pack(expand = True, fill='x', side='bottom')
        listFrame.pack(expand = True, fill='y', side='right')
        incomingTextFrame.pack(expand = True, fill='both', side='top')


        # frame1 = tk.Frame(self, relief='ridge', borderwidth=1)
        # frame1.pack(fill='both', expand=True)
        #
        # self.pack(fill='both', expand=True)
        #
        # closeButton = tk.Button(self, text="Close")
        # closeButton.pack(side='right', padx=5, pady=5)
        # okButton = tk.Button(self, text="OK")
        # okButton.pack(side='right')

root = tk.Tk()
root.minsize(width=640, height=480)
root.title('Bog Chatter')
app = App(master=root)
app.mainloop()
