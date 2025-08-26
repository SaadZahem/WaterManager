from tkinter import Frame


class Paragraph(Frame):
    def __init__(self, texts):
        super().__init__()
        for text in texts:
            self.make_label(text)

    def make_label(self, text):
        pass
