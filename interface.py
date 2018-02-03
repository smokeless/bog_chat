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

        #channel list in list frame
        channels = ['Auction', 'Bitch', 'Bogleg', 'Bughouse',
                    'Food', 'Game', 'Glb', 'Gossip', 'Headlines',
                    'Info', 'Linux', 'Meetings', 'Money', 'Newbie',
                    'Radio', 'Sports', 'Tech', 'Vegas']
        listBoxWidget = tk.Listbox(channelListFrame) #create wiget, put it in list frame.
        for item in reversed(channels):  #reversed for alaphabetical.
            listBoxWidget.insert(0, item)
        listBoxWidget.pack(fill='both', expand=True)


        self.textBox = tk.Text(textEntryFrame, height = 1, bg='red')
        label   = tk.Label(textEntryFrame, text=self.user)
        label.pack(side='bottom')
        self.textBox.pack(side='bottom', fill='x', expand=True)


        chatIncoming = tk.Listbox(textEntryFrame)
        chatIncoming.pack(side='top', fill='both', expand=True)

        channelListFrame.pack(fill='both', expand=True, side='right')

        textEntryFrame.pack(expand=True, fill='both')

    def get_text_box(self):
        v = self.textBox.get('1.0', 'end')
        return v
    def clear_text_box(self):
        self.textBox.delete('1.0', 'end')



def enter_pressed(what):
    words = app.get_text_box()
    words = words.strip()
    app.clear_text_box()
    print(words)



root = tk.Tk()
root.minsize(width=640, height=480)
root.title('Bog Chatter')
root.bind('<Return>', enter_pressed)
app = App(master=root)
app.mainloop()
