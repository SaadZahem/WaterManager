from tkinter import *
from widgets.paragraph import Paragraph

path = "g:\\New folder\\Egyptian Development Bank\\icon\\"

class Colors:
    blue = '#0B2F3A'

class Window(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(True,True)
        self.state('zoomed')
        self.configure(background= Colors.blue)
        
        self.screen = self.start()
        self.screen.pack()
    
    def start(self):
        f = Frame(self)
        b = Button(f, text= 'Start', command= self.next)
        b.pack()
        return f
    
    def next(self):
        self.screen.destroy()
        self.screen = self.home()
        self.screen.pack()
    
    def home(self):
        f = Frame(self, bg= Colors.blue)
        return f

if __name__ == '__main__':
    Window().mainloop()