from tkinter import ttk, font


bold_font = font.Font(family="Helvetica", size=8, weight="bold")

style = ttk.Style()
style.theme_use("clam")

style.configure("Thick.TSeparator", background="gray", borderwidth=5)
style.configure("Heading.TLabel", background="grey80", font=bold_font)
style.configure("Const.TLabel", background="peru", relief="raised", font=bold_font)
style.configure("Output.TLabel", background="grey50", borderwidth=5, relief="sunken")
style.configure("Blank.TLabel", borderwidth=5, relief="sunken", width=8)
style.configure("Invalid.TEntry", foreground="white", fieldbackground="red")

style.map(
    "Invalid.TEntry",
    foreground=[("focus", "red")],
    fieldbackground=[("focus", "white")],  # use fieldbackground, not background
)
