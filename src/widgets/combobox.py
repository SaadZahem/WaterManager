import tkinter as tk
from tkinter import ttk

qw = tk.Tk()
qw.geometry("500x500")

st = tk.StringVar()
c = ttk.Combobox(qw, width=5, values=["1", "Egypt"], textvariable=st, font=("tajawal"))
c.place(x=90, y=120)


def dd(*args):
    for w in qw.grid_slaves(1):
        w.grid_remove()
    if st.get() == "Egypt":
        Options = [
            "",
            "Alexandria",
            "Assuit",
            "Aswan",
            "Beni Suef",
            "Cairo",
            "Damietta",
            "Elalyoubia",
            "Elbehira",
            "Eldakahlia",
            "Elfayoum",
            "Elgharbia",
            "Elgiza",
            "Elismailia",
            "Elkalubia",
            "Elminofia",
            "Elminia",
            "Elsharkia",
            "Elsuez",
            "Elwadi Elgidid",
            "Kafr Elsheikh",
            "Luxor",
            "Matoruh",
            "North Sinai",
            "Port Said",
            "Qena",
            "Red Sea",
            "Sohag",
            "South Sinai",
        ]
        st1 = tk.StringVar()
        c = ttk.Combobox(
            qw, width=15, values=Options, textvariable=st1, font=("tajawal")
        )
        c.place(x=120, y=150)

        def ww(*args):
            nonlocal st1

            for m in qw.grid_slaves(1):
                m.grid_remove()
            if st1.get() == "Alexandria":
                Options = [
                    "",
                    "1",
                    "2",
                    "2",
                    "3",
                    "4",
                    "Damietta",
                    "Elalyoubia",
                    "Elbehira",
                    "Eldakahlia",
                    "Elfayoum",
                    "Elgharbia",
                    "Elgiza",
                    "Elismailia",
                    "Elkalubia",
                    "Elminofia",
                    "Elminia",
                    "Elsharkia",
                    "Elsuez",
                    "Elwadi Elgidid",
                    "Kafr Elsheikh",
                    "Luxor",
                    "Matoruh",
                    "North Sinai",
                    "Port Said",
                    "Qena",
                    "Red Sea",
                    "Sohag",
                    "South Sinai",
                ]
                st1 = tk.StringVar()
                c1 = ttk.Combobox(
                    qw, width=15, values=Options, textvariable=st1, font=("tajawal")
                )
                c1.place(x=120, y=200)

            elif st1.get() == "Assuit":
                Options = [""]
                st2 = tk.StringVar()
                c1 = ttk.Combobox(
                    qw, width=15, values=Options, textvariable=st2, font=("tajawal")
                )
                c1.place(x=120, y=200)

        st1.trace("m", ww)

    elif st.get() == "1":
        Options = ["", ""]
        st2 = tk.StringVar()
        c = ttk.Combobox(
            qw, width=15, values=Options, textvariable=st2, font=("tajawal")
        )
        c.place(x=120, y=150)


st.trace_add("write", dd)
# st.trace('m',ww)
qw.mainloop()
