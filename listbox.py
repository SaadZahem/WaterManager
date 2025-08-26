from ast import Delete
import tkinter as tk
from tkinter import *
from turtle import color

qw = tk.Tk()
qw.geometry("500x500")

listbox = Listbox(
    qw,
    width=30,
    height=5,
    fg="red",
    bd=0,
)


def add():
    n = name.get()
    listbox.insert(END, n)
    name.set("")


def delete():
    listbox.delete(ANCHOR)


# listbox.place(x=0,y=300)
listbox.grid(column=0, row=0, sticky="nwes")
b6 = tk.Button(
    qw, text="add", font=("tajawal"), bd=3, fg="black", bg="red", command=add
).place(x=0, y=260)

b6 = tk.Button(
    qw, text="delete", font=("tajawal"), bd=3, fg="black", bg="red", command=delete
).place(x=50, y=260)

name = tk.StringVar()

e1 = tk.Entry(qw, width=32, bd=3, fg="black", justify="center", textvariable=name)
e1.place(x=250, y=30)

scrollbar = tk.Scrollbar(qw, orient="vertical", command=listbox.yview)
listbox["yscrollcommand"] = scrollbar.set
# scrollbar.pack()
scrollbar.grid(column=1, row=0, sticky="ns")


qw.mainloop()
