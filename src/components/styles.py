from tkinter import ttk, font


bold_font = font.Font(family="Helvetica", size=8, weight="bold")

style = ttk.Style()
style.theme_use("clam")

style.configure("Thick.TSeparator", background="gray", borderwidth=5)
style.configure("Const.TLabel", background="peru", relief="raised", font=bold_font)
style.configure("Output.TLabel", background="grey50", borderwidth=5, relief="sunken")
style.configure("Invalid.TEntry", foreground="white", fieldbackground="red")

# style.map(
#     "TEntry",
#     foreground=[("invalid", "blue")],
#     fieldbackground=[("invalid", "red")],  # use fieldbackground, not background
# )
