from tkinter import ttk, font


bold_font = font.Font(family='Helvetica', size=8, weight='bold')
s = ttk.Style()
s.theme_use("classic")  #<-- executes automatically on import
s.configure("Thick.TSeparator", background="gray", borderwidth=5)
s.configure("Const.TLabel", background="peru", relief="raised", font=bold_font)
s.configure("Output.TLabel", background="grey50", borderwidth=5, relief="sunken")