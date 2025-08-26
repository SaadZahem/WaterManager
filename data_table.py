
from tkinter import ttk, Frame, Scrollbar, HORIZONTAL, VERTICAL, BOTTOM, LEFT, BOTH, X, Y


class DataTable(Frame):
    columns = (
            'name',
            'telephone',
            'National ID',
            'Home Address',
            'field ID',
            'areaa',
            'irrigation periud',
            'irrigation period',
            'name',
            'name',
    )

    def __init__(self, *args, **kws):
        super().__init__(*args, **kws)
        
        self.tree = ttk.Treeview(self, columns= DataTable.columns)
        self.xscroll = Scrollbar(self, orient=HORIZONTAL)
        self.yscroll = Scrollbar(self, orient=VERTICAL)
        
        self.xscroll.pack(side=BOTTOM, fill=X)
        self.yscroll.pack(side=LEFT, fill=Y)
        self.tree.pack(fill=BOTH, expand=True)

        self.tree.config(
            xscrollcommand= self.xscroll.set,
            yscrollcommand= self.yscroll.set,
        )
        self.xscroll.config(command= self.tree.xview)
        self.yscroll.config(command= self.tree.yview)
    
    def set_headings(self):
        textarea = self.tree
        textarea['show']='headings'
        textarea.heading('name',text='الاسم',width=130)
        textarea.heading('telephone',text='التليفون')
        textarea.heading('National ID',text='الرقم القومى')
        textarea.heading('Home Address',text='عنوان المنزل')
        textarea.heading('field ID',text='field ID')
        textarea.heading('areaa',text='areaa')
        textarea.heading('irrigation period',text='فترة الرى')
        textarea.heading('name',text='الاسم')
        textarea.heading('name',text='الاسم')
        textarea.heading('name',text='الاسم')


