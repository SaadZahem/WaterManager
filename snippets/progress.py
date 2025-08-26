import time
from tkinter import Label, Tk
from tkinter import ttk

root = Tk()
s = ttk.Style()
s.configure("TProgressbar", foreground="green", background="green", thickness=50)


def start_training_images():
    for i in range(1, 101):
        progress["value"] = i
        label_progress.config(text=str(i) + "%")
        root.update_idletasks()
        time.sleep(0.1)


ttk.Style().configure("green/white.TLabel", foreground="green", font=("Verdana", 18))
label_train = ttk.Label(
    root,
    text="Click Start for training",
    font="arial 15 bold",
    style="green/white.TLabel",
)
label_train.pack(padx=20, pady=15)

label_progress = Label(root, font="arial 12 bold")
label_progress.pack(padx=100, pady=3)

progress = ttk.Progressbar(root, style="TProgressbar", length=250, mode="determinate")
progress.pack(padx=10, pady=15)

btn_start = ttk.Button(root, text="Start", command=start_training_images)
btn_start.pack(padx=20, pady=15)

root.mainloop()
