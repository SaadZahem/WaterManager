from tkinter import *
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(True,True)
        self.state('zoomed')
        self.configure(background='red')#تغير الخلفية
        self.w = self.winfo_screenwidth()
        self.h = self.winfo_screenheight()
        self.state('zoomed')
        self.geometry ("{w}x{h}+0+0".format(w=self.w,h=self.h))#self.pro.geometry ('1366x705+0+0')  # f"{self.w}x{self.h}+0+0" 
        
        self.screen = self.start()
        self.screen.pack(fill='both', expand=1)
        
    def start(self):
        f = Frame(self, bg= '#0B2F3A')
        b = Button(f, text= 'Start',font=('tajawal',17,'bold'),width=10,bd=5,height=1, fg='black',bg='red',command= self.next)
        b.place(x=1020,y=625)
        return f
    def next(self): 
        self.screen.destroy()
        self.screen = self.home()
        self.screen.pack(fill=BOTH, expand=True)
        print(BOTH)
    
    def home(self):
        f = Frame(self, bg='#0B2F3A', borderwidth=1)
        f1 = Frame(f,bd=2,width=100, height=self.h, bg='gold')#bd 2d/3dنوع البرورد       وممكن لاتحدد الطول والعرض أوتضيفة على على السطر التالى
        f1.place(x=0,y=0)
        
        b1 = Button(f1, text= 'Feedback Data', font=('tajawal'), width=11,bd=3, fg='black', bg='red', command= self.feedback_Data)#,height=1
        b1.pack()#pady=20
        return f

    def feedback_Data (self):
        f = Frame(self, bg='#0B2F3A', borderwidth=1)
        f1 = Frame(f,bd=2,width=self.w, height=self.h, bg='gold')#bd 2d/3dنوع البرورد       وممكن لاتحدد الطول والعرض أوتضيفة على على السطر التالى
        f1.place(x=100,y=0)
        tree = ttk.Treeview(f1, columns = ('1','2','3','4','5','6','7','8','9','10'), show='headings', height=100)#, width=100
        tree.pack(side=LEFT)

        xscroll = Scrollbar(f1, orient=HORIZONTAL)
        yscroll = Scrollbar(f1, orient=VERTICAL)
        
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=LEFT, fill=Y)

        #tree.pack(fill=BOTH, expand=True)

        tree.config(xscrollcommand= xscroll.set, yscrollcommand= yscroll.set,)

        xscroll.config(command= tree.xview)
        yscroll.config(command= tree.yview)

        tree.heading('1', text='الاسم', width=130)
        tree.heading('2', text='التليفون')
        tree.heading('3', text='الرقم القومى')
        tree.heading('4', text='عنوان المنزل')
        tree.heading('5', text='field ID')
        tree.heading('6', text='areaa')
        tree.heading('7', text='فترة الرى')
        tree.heading('8', text='الاسم')
        tree.heading('9', text='الاسم')
        tree.heading('10', text='الاسم')
        #return f
if __name__ == '__main__':
    
    Window().mainloop()