import tkinter as tk

from PIL import ImageTk, Image


class IMG(tk.Label):
    def __init__(self, master, src):
        image = ImageTk.PhotoImage(Image.open(src))
        super().__init__(master, image=image)
        self.image = image

    def place(self, *args, **kwargs):
        super().place(*args, **kwargs)
        return self
