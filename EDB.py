from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb

from typing import NamedTuple

from unicodedata import name
from urllib import response
import sys
from PIL import ImageTk, Image
import sqlite3
from data_table import DataTable
from tkcalendar import DateEntry

# *************************************************************************************************************
p = "icon/"
fo = ("tajawal", 16, "bold")
d = "fg+'gold',bg='#0B2F3A',font=fo"

# country, governorate and city comboboxes options
options = {
    "Egypt": {
        "": [],
        "Alexandria": [
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
        ],
        "Assuit": [],
        "Aswan": [],
        "Beni Suef": [],
        "Cairo": [],
        "Damietta": [],
        "Elalyoubia": [],
        "Elbehira": [],
        "Eldakahlia": [],
        "Elfayoum": [],
        "Elgharbia": [],
        "Elgiza": [],
        "Elismailia": [],
        "Elkalubia": [],
        "Elminofia": [],
        "Elminia": [],
        "Elsharkia": [],
        "Elsuez": [],
        "Elwadi Elgidid": [],
        "Kafr Elsheikh": [],
        "Luxor": [],
        "Matoruh": [],
        "North Sinai": [],
        "Port Said": [],
        "Qena": [],
        "Red Sea": [],
        "Sohag": [],
        "South Sinai": [],
    },
}


class IMG(Label):
    def __init__(self, master, src):
        image = ImageTk.PhotoImage(Image.open(src))
        super().__init__(master, image=image)
        self.image = image

    def place(self, *args, **kwargs):
        super().place(*args, **kwargs)
        return self


class DataRow(NamedTuple):
    name: str
    gender: str


# *************************************************************************************************************
class Window(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(True, True)
        self.state("zoomed")
        self.configure(background="black")  # تغير الخلفية
        self.w = self.winfo_screenwidth()
        self.h = self.winfo_screenheight()
        self.state("zoomed")
        self.geometry(
            "{w}x{h}+0+0".format(w=self.w, h=self.h)
        )  # self.pro.geometry ('1366x705+0+0')  # f"{self.w}x{self.h}+0+0"
        self.title("Egyptian Development Bank")
        self.iconbitmap(p + "1.ico")

        self.screen = self.start()
        self.screen.pack(fill="both", expand=1)

    def start(self):
        f = Frame(self, bg="#0B2F3A")

        t1 = Label(
            f,
            text="UTILIZATION OF GIS AND REMOTE SENSING TECHNOLOGY ON",
            fg="gold",
            bg="#0B2F3A",
            font=fo,
        )
        t1.place(x=400, y=90)
        t2 = Label(
            f,
            text="IRRIGATION WATER MANAGEMENT IN THE NORTH DLTA",
            fg="gold",
            bg="#0B2F3A",
            font=fo,
        )
        t2.place(x=440, y=120)
        t3 = Label(
            f,
            text="OF EGYPT AS A CASE STUDY",
            fg="gold",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )
        t3.place(x=540, y=150)
        t4 = Label(
            f,
            text='"Egyptian Development Bank" (EDB) Model',
            fg="red",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )
        t4.place(x=470, y=200)

        t5 = Label(
            f,
            text="Developed by",
            fg="white",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )
        t5.place(x=615, y=270)
        t6 = Label(
            f,
            text="Nader Elsayed Saad Rizq Zahem",
            fg="gold",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )
        t6.place(x=530, y=320)
        t7 = Label(
            f,
            text="B.Sc.,Agric. Engineering, Al-Azhar University, Egypt",
            fg="white",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )
        t7.place(x=450, y=350)

        t8 = Label(
            f, text="Supervisor", fg="white", bg="#0B2F3A", font=("tajawal", 16, "bold")
        )
        t8.place(x=620, y=400)

        t9 = Label(
            f, text="Prof.Dr.", fg="white", bg="#0B2F3A", font=("tajawal", 16, "bold")
        )
        t9.place(x=230, y=450)
        t10 = Label(
            f,
            text="Mohamed Maher Ibrahim",
            fg="gold",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )  # Abd Elal
        t10.place(x=150, y=480)
        t11 = Label(
            f,
            text="Assistant Professor at Irrigation and drainage Agricultural ",
            fg="white",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )
        t11.place(x=5, y=510)
        t12 = Label(
            f,
            text="Engineering Department, Faculty of Agriculture,",
            fg="white",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )
        t12.place(x=60, y=540)
        t13 = Label(
            f,
            text="Mansoura University, Egypt",
            fg="white",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )
        t13.place(x=140, y=570)

        t14 = Label(
            f, text="Prof.Dr.", fg="White", bg="#0B2F3A", font=("tajawal", 16, "bold")
        )
        t14.place(x=1050, y=450)
        t15 = Label(
            f,
            text="Nadia Gamal Abd Elfattah Daoud",
            fg="gold",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )
        t15.place(x=930, y=480)
        t16 = Label(
            f,
            text="Lecturer at Irrigation and drainage of Agricultural",
            fg="white",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )
        t16.place(x=850, y=510)
        t17 = Label(
            f,
            text="Engineering Department, Faculty of Agriculture,",
            fg="white",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )
        t17.place(x=860, y=540)
        t18 = Label(
            f,
            text="Mansoura University, Egypt",
            fg="white",
            bg="#0B2F3A",
            font=("tajawal", 16, "bold"),
        )
        t18.place(x=960, y=570)

        t19 = Label(
            f, text="Version 1.0", fg="white", bg="#0B2F3A", font=("tajawal", 14)
        )
        t19.place(x=625, y=630)
        t20 = Label(f, text="2022", fg="white", bg="#0B2F3A", font=("tajawal", 14))
        t20.place(x=640, y=660)

        i1 = IMG(f, p + "2.png").place(x=-4, y=0, width=200, height=220)
        i2 = IMG(f, p + "0.png").place(x=1176, y=0, width=190, height=230)

        b = Button(
            f,
            text="Start",
            font=("tajawal", 17, "bold"),
            width=10,
            bd=5,
            height=1,
            fg="black",
            bg="red",
            command=self.next,
        )
        b.place(x=1020, y=625)
        b1 = Button(
            f,
            text="Exit",
            font=("tajawal", 17, "bold"),
            width=10,
            bd=5,
            height=1,
            fg="black",
            bg="red",
            command=self.sd,
        )
        b1.place(x=200, y=625)

        return f

    def sd(self):
        messagebox.askyesno("quit", "Are your sure sir !")
        if response == 1:
            self.screen.destroy()
        # else:
        # self.start

    def next(self):
        self.screen.destroy()
        self.screen = self.home()
        self.screen.pack(fill=BOTH, expand=True)

    def home(self):
        f = Frame(self, bg="#0B2F3A", borderwidth=1)
        f1 = Frame(
            f, bd=2, width=300, height=300, bg="gold"
        )  # bd 2d/3dنوع البرورد       وممكن لاتحدد الطول والعرض أوتضيفة على على السطر التالى
        f1.place(x=530, y=200)

        t1 = Label(
            f1, text="EDB system login", fg="black", bg="gold", font=("tajawal", 14)
        )
        t1.place(x=70, y=0)
        t2 = Label(f1, text="User Name :", fg="black", bg="gold", font=("tajawal", 14))
        t2.place(x=0, y=30)
        t3 = Label(f1, text="Password   :", fg="black", bg="gold", font=("tajawal", 14))
        t3.place(x=0, y=60)

        e1 = Entry(f1, width=30, bd=3)
        e1.place(x=110, y=35)
        e2 = Entry(
            f1, width=30, bd=3, justify="center"
        )  # justify='right',height=1  /textvarible=  /
        e2.place(x=110, y=65)

        b2 = Button(
            f1,
            text="Exit",
            font=("tajawal", 17, "bold"),
            width=6,
            bd=3,
            height=1,
            fg="black",
            bg="red",
            command=self.page1(self.start),
        )  # destroy /quit
        b2.place(x=50, y=130)
        b1 = Button(
            f1,
            text="Sign In",
            font=("tajawal", 17, "bold"),
            width=6,
            bd=3,
            fg="black",
            bg="red",
            command=self.page1(self.page2),
        )
        b1.place(x=150, y=130)

        return f

    def page1(self, func):
        def f():
            self.screen.destroy()
            self.screen = func()
            self.screen.pack(fill=BOTH, expand=True)

        return f

    def page2(self):
        f = Frame(self, bg="#0B2F3A", borderwidth=1)
        f1 = Frame(
            f, bd=2, width=100, height=self.h, bg="gold"
        )  # bd 2d/3dنوع البرورد       وممكن لاتحدد الطول والعرض أوتضيفة على على السطر التالى
        f1.place(x=0, y=0)

        b5 = Button(
            f1,
            text="Add land",
            font=("tajawal"),
            width=11,
            bd=3,
            fg="black",
            bg="red",
            command=self.Add_land,
        )
        b5.pack()
        b2 = Button(
            f1,
            text="Add data",
            font=("tajawal"),
            width=11,
            bd=3,
            fg="black",
            bg="red",
            command=self.Add_data1,
        )
        b2.pack(pady=0)
        b1 = Button(
            f1,
            text="Feedback Data",
            font=("tajawal"),
            width=11,
            bd=3,
            fg="black",
            bg="red",
            command=self.feedback_Data,
        )  # ,height=1
        b1.pack()  # pady=20
        b4 = Button(
            f1, text="RAC", font=("tajawal"), width=11, bd=3, fg="black", bg="red"
        )
        b4.pack(pady=0)
        b4 = Button(
            f1,
            text="Crop selection",
            font=("tajawal"),
            width=11,
            bd=3,
            fg="black",
            bg="red",
        )
        b4.pack()
        b4 = Button(
            f1,
            text="incoming mail",
            font=("tajawal"),
            width=11,
            bd=3,
            fg="black",
            bg="red",
        )
        b4.pack(pady=0)
        b3 = Button(
            f1,
            text="Search",
            font=("tajawal"),
            width=11,
            bd=3,
            fg="black",
            bg="red",
            command=self.say_hello,
        )  # ,command= self.play
        b3.pack()
        b4 = Button(
            f1,
            text="Settings",
            font=("tajawal"),
            width=11,
            bd=3,
            fg="black",
            bg="red",
            command=self.Settings,
        )
        b4.pack(pady=0)
        b6 = Button(
            f1,
            text="Help",
            font=("tajawal"),
            width=11,
            bd=3,
            fg="black",
            bg="red",
            command=self.Help,
        )
        b6.pack()
        b7 = Button(
            f1,
            text="Exit",
            font=("tajawal"),
            width=11,
            bd=3,
            fg="black",
            bg="red",
            command=self.page1(self.start),
        )  #   .grid(row=0, column=2) ,command= self.start
        b7.pack(pady=0)

        return f

    # ***********************************************************
    def save_data(self, data):
        wb = Workbook("data.xlsx")
        ws = wb.add_worksheet()
        ws.write("B2", data.name)
        ws.write("C2", data.gender)
        wb.close()

    # ***********************************************************
    def Add_land(self):  # static scope
        f = Frame(
            self, bd=2, width=self.w, height=self.h, bg="white"
        )  # bd 2d/3dنوع البرورد       وممكن لاتحدد الطول والعرض أوتضيفة على على السطر التالى   ,width=1247, height=704
        f.place(x=117, y=0)
        f1 = Frame(self, bd=2, width=300, height=self.h, bg="gold")
        f1.place(x=117, y=0)
        f2 = Frame(self, bd=2, width=300, height=self.h, bg="gold")
        f2.place(x=418, y=0)

        # *****************************الاطار الاول*****************************************
        t = Label(f1, text="Person data", fg="red", bg="gold", font=("tajawal", 14))
        t.place(x=90, y=0)
        t = Label(f1, text="National ID :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=25)
        t = Label(f1, text="Full name :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=55)
        t = Label(f1, text="Home Adress", fg="red", bg="gold", font=("tajawal", 14))
        t.place(x=90, y=85)
        t = Label(f1, text="Country :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=115)
        t = Label(f1, text="Governorate :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=145)
        t = Label(f1, text="City :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=175)

        t = Label(
            f1, text="Telephone number :", fg="black", bg="gold", font=("tajawal", 14)
        )
        t.place(x=0, y=205)
        t = Label(f1, text="Emil Adress :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=235)
        t = Label(f1, text="Birth date :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=265)
        t = Label(f1, text="Enter data", fg="red", bg="gold", font=("tajawal", 14))
        t.place(x=90, y=295)
        t = Label(f1, text="Enter Email :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=325)
        t = Label(f1, text="Password :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=355)

        e0 = Entry(f1, width=32, bd=3, fg="black", justify="center")  # name
        e0.place(x=95, y=30)
        e1 = Entry(
            f1, width=32, bd=3, fg="black", justify="center"
        )  # justify='right',height=1
        e1.place(x=106, y=60)
        e2 = Entry(
            f1, width=15, bd=3, fg="black", justify="center"
        )  # justify='right',height=1
        e2.place(x=180, y=210)
        e3 = Entry(
            f1, width=30, bd=3, fg="black", justify="center"
        )  # justify='right',height=1
        e3.place(x=106, y=240)
        e4 = Entry(
            f1, width=30, bd=3, fg="black", justify="center"
        )  # justify='right',height=1
        e4.place(x=106, y=330)
        e5 = Entry(
            f1, width=30, bd=3, fg="black", justify="center"
        )  # justify='right',height=1
        e5.place(x=106, y=360)

        def save_data():
            data = DataRow(e1.get(), gender)
            self.save_data(data)

        b7 = Button(
            f1,
            text="Exit",
            font=("tajawal"),
            width=11,
            bd=3,
            fg="black",
            bg="red",
            command=save_data,
        )  #   .grid(row=0, column=2) ,command= self.start
        b7.place(x=106, y=450)

        gender = None

        def set_male():
            nonlocal gender
            gender = "male"

        def set_female():
            nonlocal gender
            gender = "female"

        b0 = ttk.Radiobutton(f1, text="male", command=set_male, value=1)
        b0.place(x=150, y=122)

        b1 = ttk.Radiobutton(f1, text="female", command=set_female, value=2)
        b1.place(x=202, y=122)

        cal = DateEntry(f1, selectmode="day", year=2021, month=7, day=16)
        cal.place(x=100, y=270)

        def country_changed(*args):
            self.gov = StringVar()
            values = list(options[self.country.get()].keys())
            c = ttk.Combobox(
                f1, width=11, values=values, textvariable=self.gov, font="tajawal"
            )
            c.place(x=120, y=150)
            self.gov.trace("w", gov_changed)

        self.country = StringVar()
        c = ttk.Combobox(
            f1,
            width=5,
            values=list(options.keys()),
            textvariable=self.country,
            font="tajawal",
        )
        c.place(x=79, y=120)
        self.country.trace("w", country_changed)

        def gov_changed(*args):
            self.city = StringVar()
            values = options[self.country.get()][self.gov.get()]
            c = ttk.Combobox(
                f1, width=5, values=values, textvariable=self.city, font="tajawal"
            )
            c.place(x=50, y=180)
            # self.city.trace('w', self.gov_changed)

        # *****************************الاطار الثانى*****************************************
        t = Label(f2, text="Fild data", fg="red", bg="gold", font=("tajawal", 14))
        t.place(x=90, y=0)
        t = Label(f2, text="field ID :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=25)
        t = Label(f2, text="Basin :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=205)

        def listbox_selected(event):
            f1 = Frame(self, bd=2, width=210, height=self.h, bg="gold")
            f1.place(x=719, y=0)

            t = Label(
                f1, text="Meteorology ", fg="red", bg="gold", font=("tajawal", 14)
            )
            t.place(x=55, y=0)
            t2 = Label(
                f1, text="R\u2099:", fg="black", bg="gold", font=("tajawal", 14)
            )  # Rn
            t2.place(x=0, y=20)
            t3 = Label(f1, text="G :", fg="black", bg="gold", font=("tajawal", 14))
            t3.place(x=0, y=46)
            t4 = Label(
                f1, text="\u0394 :", fg="black", bg="gold", font=("tajawal", 14)
            )  # dlta
            t4.place(x=0, y=72)
            t5 = Label(
                f1, text="U\u2082:", fg="black", bg="gold", font=("tajawal", 14)
            )  # u2
            t5.place(x=0, y=98)
            t6 = Label(
                f1, text="e\u209b:", fg="black", bg="gold", font=("tajawal", 14)
            )  # es
            t6.place(x=0, y=124)
            t7 = Label(
                f1, text="e\u2090:", fg="black", bg="gold", font=("tajawal", 14)
            )  # ea
            t7.place(x=0, y=150)
            t8 = Label(f1, text="T :", fg="black", bg="gold", font=("tajawal", 14))
            t8.place(x=0, y=176)
            t9 = Label(
                f1, text="\u0194 :", fg="black", bg="gold", font=("tajawal", 14)
            )  # gama
            t9.place(x=0, y=202)
            t9 = Label(
                f1, text="ET\u2092", fg="red", bg="gold", font=("tajawal", 14)
            )  # ETo
            t9.place(x=0, y=227)

            t11 = Label(
                f1, text="Crop type:", fg="black", bg="gold", font=("tajawal", 14)
            )
            t11.place(x=0, y=249)
            t12 = Label(
                f1, text="Kc ini. :", fg="black", bg="gold", font=("tajawal", 14)
            )
            t12.place(x=0, y=276)
            t12 = Label(f1, text="ETc ini.", fg="red", bg="gold", font=("tajawal", 14))
            t12.place(x=0, y=302)
            t14 = Label(
                f1, text="Kc mid. :", fg="black", bg="gold", font=("tajawal", 14)
            )
            t14.place(x=0, y=328)
            t12 = Label(f1, text="ETc mid.", fg="red", bg="gold", font=("tajawal", 14))
            t12.place(x=0, y=354)
            t16 = Label(
                f1, text="Kc end. :", fg="black", bg="gold", font=("tajawal", 14)
            )
            t16.place(x=0, y=380)
            t12 = Label(f1, text="ETc end.", fg="red", bg="gold", font=("tajawal", 14))
            t12.place(x=0, y=406)
            t12 = Label(
                f1,
                text="Readily available water",
                fg="red",
                bg="gold",
                font=("tajawal", 14),
            )  # ETc
            t12.place(x=0, y=427)

            t18 = Label(f1, text="AW :", fg="black", bg="gold", font=("tajawal", 14))
            t18.place(x=0, y=450)
            t19 = Label(
                f1, text="Z\u1d63  :", fg="black", bg="gold", font=("tajawal", 14)
            )  # zr
            t19.place(x=0, y=476)
            t20 = Label(f1, text="P   :", fg="black", bg="gold", font=("tajawal", 14))
            t20.place(x=0, y=502)
            t20 = Label(f1, text="RAW", fg="red", bg="gold", font=("tajawal", 14))
            t20.place(x=0, y=528)

            t21 = Label(
                f1,
                text="Leaching Requirements",
                fg="red",
                bg="gold",
                font=("tajawal", 14),
            )
            t21.place(x=0, y=548)
            t22 = Label(
                f1, text="Soil type :", fg="black", bg="gold", font=("tajawal", 14)
            )
            t22.place(x=0, y=573)
            t23 = Label(f1, text="ECw :", fg="black", bg="gold", font=("tajawal", 14))
            t23.place(x=0, y=599)
            t24 = Label(
                f1, text="EC\u2091 :", fg="black", bg="gold", font=("tajawal", 14)
            )
            t24.place(x=0, y=624)
            t24 = Label(f1, text="LR :", fg="red", bg="gold", font=("tajawal", 14))
            t24.place(x=0, y=651)

            e1 = Entry(
                f1, width=9, bd=3, fg="red", justify="center"
            )  # justify='right',height=1
            e1.place(x=39, y=23)
            e2 = Entry(
                f1, width=9, bd=3, justify="center"
            )  # justify='right',height=1  /textvarible=  /
            e2.place(x=39, y=49)
            e3 = Entry(
                f1, width=9, bd=3, justify="center"
            )  #  ,textvariable=name استدعاء المتغير -----+ name=stringvar()
            e3.place(x=39, y=75)
            e4 = Entry(f1, width=9, bd=3, justify="center")
            e4.place(x=39, y=101)
            e5 = Entry(f1, width=9, bd=3, justify="center")
            e5.place(x=39, y=127)
            e6 = Entry(f1, width=9, bd=3, justify="center")
            e6.place(x=39, y=153)
            e7 = Entry(f1, width=9, bd=3, justify="center")
            e7.place(x=39, y=179)
            e8 = Entry(f1, width=9, bd=3, justify="center")
            e8.place(x=39, y=205)
            e9 = Entry(
                f1,
                width=9,
                bd=3,
                justify="center",
                relief=SUNKEN,
                textvariable=sys.displayhook,
            )
            e9.place(x=39, y=231)

            e10 = Entry(f1, width=7, bd=3, justify="center")
            e10.place(x=85, y=279)
            e11 = Entry(f1, width=7, bd=3, justify="center")
            e11.place(x=85, y=305)
            e12 = Entry(f1, width=7, bd=3, justify="center")
            e12.place(x=85, y=331)
            e13 = Entry(f1, width=7, bd=3, justify="center")
            e13.place(x=85, y=357)
            e14 = Entry(f1, width=7, bd=3, justify="center")
            e14.place(x=85, y=383)
            e15 = Entry(f1, width=7, bd=3, justify="center")
            e15.place(x=85, y=409)

            e16 = Entry(f1, width=7, bd=3, justify="center")
            e16.place(x=60, y=453)
            e17 = Entry(f1, width=7, bd=3, justify="center")
            e17.place(x=60, y=479)
            e18 = Entry(f1, width=7, bd=3, justify="center")
            e18.place(x=60, y=505)
            e19 = Entry(f1, width=7, bd=3, justify="center")
            e19.place(x=60, y=531)

            e20 = Entry(f1, width=9, bd=3, fg="red", justify="center")
            e20.place(x=55, y=601)
            e21 = Entry(
                f1, width=9, bd=3, justify="center"
            )  # justify='right',height=1  /textvarible=  / ,fg='red'
            e21.place(x=55, y=627)
            e22 = Entry(f1, width=9, bd=3, justify="center")
            e22.place(x=55, y=653)

            t2s.place(x=100, y=25)
            t3s = Label(
                f1, text="MJ.m\u00b2/day", fg="black", bg="gold", font=("tajawal", 14)
            )
            t3s.place(x=100, y=49)
            t4s = Label(f1, text="m/s", fg="black", bg="gold", font=("tajawal", 14))
            t4s.place(x=100, y=75)
            t5s = Label(f1, text="m/s", fg="black", bg="gold", font=("tajawal", 14))
            t5s.place(x=100, y=101)
            t6s = Label(
                f1, text="KP\u2090", fg="black", bg="gold", font=("tajawal", 14)
            )
            t6s.place(x=100, y=127)
            t7s = Label(
                f1, text="KP\u2090", fg="black", bg="gold", font=("tajawal", 14)
            )
            t7s.place(x=100, y=153)
            t8s = Label(f1, text="\u00b0c", fg="black", bg="gold", font=("tajawal", 14))
            t8s.place(x=100, y=179)
            t9s = Label(
                f1, text="KP\u2090/\u00b0c", fg="black", bg="gold", font=("tajawal", 14)
            )
            t9s.place(x=100, y=203)
            t10s = Label(f1, text="mm/day", fg="black", bg="gold", font=("tajawal", 14))
            t10s.place(x=100, y=225)

            t11s = Label(f1, text="mm/day", fg="black", bg="gold", font=("tajawal", 14))
            t11s.place(x=135, y=299)
            t12s = Label(f1, text="mm/day", fg="black", bg="gold", font=("tajawal", 14))
            t12s.place(x=135, y=351)
            t13s = Label(f1, text="mm/day", fg="black", bg="gold", font=("tajawal", 14))
            t13s.place(x=135, y=403)

            t13s = Label(f1, text="mm/m", fg="black", bg="gold", font=("tajawal", 14))
            t13s.place(x=115, y=453)
            t13s = Label(f1, text="%", fg="black", bg="gold", font=("tajawal", 14))
            t13s.place(x=115, y=479)

            t20s = Label(f1, text="dS/m", fg="black", bg="gold", font=("tajawal", 14))
            t20s.place(x=120, y=596)
            t21s = Label(f1, text="dS/m", fg="black", bg="gold", font=("tajawal", 14))
            t21s.place(x=120, y=621)

        listbox = Listbox(
            f2,
            width=30,
            height=5,
            fg="red",
            bd=0,
        )
        listbox.bind("<<ListboxSelect>>", listbox_selected)
        listbox.place(x=0, y=100)

        def add():
            n = name.get()
            if not n:
                return
            listbox.insert(END, n)
            name.set("")

        def delete():
            listbox.delete(ANCHOR)

        b6 = tk.Button(
            f2, text="Add", font=("tajawal"), bd=3, fg="black", bg="red", command=add
        ).place(x=0, y=60)
        b6 = tk.Button(
            f2,
            text="Delete",
            font=("tajawal"),
            bd=3,
            fg="black",
            bg="red",
            command=delete,
        ).place(x=50, y=60)

        name = tk.StringVar()

        tk.Entry(
            f2, width=20, bd=3, fg="black", justify="center", textvariable=name
        ).place(x=75, y=30)

        scrollbar = tk.Scrollbar(f2, orient="vertical", command=listbox.yview)
        listbox["yscrollcommand"] = scrollbar.set
        # scrollbar.pack()
        scrollbar.place(x=182, y=100, height=82)

    # class kj(Label):
    # def

    def add(self):
        li = Listbox(self, width=30, height=5)
        li.insert(END, n)
        li.place(x=0, y=300)
        e1 = tk.Entry(
            self, width=32, bd=3, fg="black", justify="center", textvariable=name
        )  # justify='right',height=1
        e1.place(x=95, y=30)
        n = name.get()

        name = tk.StringVar()

        # li.insert(ANCHOR)

    # *********************************************
    # *********************************************
    def Add_data1(self):
        f = Frame(
            self, bd=2, width=self.w, height=self.h, bg="white"
        )  # bd 2d/3dنوع البرورد       وممكن لاتحدد الطول والعرض أوتضيفة على على السطر التالى   ,width=1247, height=704
        f.place(x=117, y=0)
        f1 = Frame(self, bd=2, width=300, height=self.h, bg="gold")
        f1.place(x=117, y=0)

        t = Label(
            f1, text="Select Country :", fg="black", bg="gold", font=("tajawal", 14)
        )
        t.place(x=0, y=0)
        t = Label(
            f1,
            text="Select Witch your data will see?",
            fg="red",
            bg="gold",
            font=("tajawal", 14),
        )
        t.place(x=0, y=25)
        t = Label(f1, text="Governorate :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=85)
        t = Label(f1, text="City :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=115)
        t = Label(f1, text="Basin :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=145)
        t = Label(f1, text="field ID :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=175)
        t = Label(f1, text="Full name :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=205)
        t = Label(f1, text="National ID :", fg="black", bg="gold", font=("tajawal", 14))
        t.place(x=0, y=235)

        e1 = Entry(
            f1, width=32, bd=3, fg="black", justify="center"
        )  # justify='right',height=1
        e1.place(x=95, y=180)
        e1 = Entry(
            f1, width=32, bd=3, fg="black", justify="center"
        )  # justify='right',height=1
        e1.place(x=95, y=210)
        e1 = Entry(
            f1, width=32, bd=3, fg="black", justify="center"
        )  # justify='right',height=1
        e1.place(x=95, y=240)

        b = Button(
            f1,
            text="Enter",
            font=("tajawal", 17, "bold"),
            bd=5,
            fg="black",
            bg="red",
            command=self.next,
        )
        b.place(x=50, y=500)

        # *******************************************select****************************************************************
        Options = ["", "Egypt"]
        clicked = StringVar()
        clicked.set(Options[0])

        c = ttk.Combobox(f1, width=5, values=Options)
        c.current(0)
        c.bind(
            "<<ComboboxSelected>>"
        )  # ,comboclick / def comboclick(event): / m= label(root, text= c.get()).pack()
        c.place(x=140, y=5)

        Options = [
            "",
            "Governorate",
            "City",
            "Basin",
            "field ID",
            "Full name",
            "National ID",
        ]
        clicked = StringVar()
        clicked.set(Options[0])

        c = ttk.Combobox(f1, width=10, values=Options)
        c.current(0)
        c.bind(
            "<<ComboboxSelected>>"
        )  # ,comboclick / def comboclick(event): / m= label(root, text= c.get()).pack()
        c.place(x=120, y=60)

        Options = [
            "",
            "Alexandria",
            "Assuit",
            "Aswan",
            "Beni Sweif",
            "Cairo",
            "Damietta",
            "Eldakahlia",
            "Kafr Elsheik",
            "Elbehira",
            "Elgharbia",
            "Elminofia",
            "Elsharkia",
            "Elkalubia",
            "Elgiza",
            "Elfayoum",
            "Elminia",
            "Sohag",
            "Qena",
            "",
            "",
            "",
        ]
        clicked = StringVar()
        clicked.set(Options[0])

        c = ttk.Combobox(f1, width=10, values=Options)
        c.current(0)
        c.bind(
            "<<ComboboxSelected>>"
        )  # ,comboclick / def comboclick(event): / m= label(root, text= c.get()).pack()
        c.place(x=120, y=90)

        Options = [
            "",
            "Elgamalia",
            "Elmansura",
            "City",
            "Basin",
            "ID Land",
            "Name",
            "ID",
        ]
        clicked = StringVar()
        clicked.set(Options[0])

        c = ttk.Combobox(f1, width=10, values=Options)
        c.current(0)
        c.bind(
            "<<ComboboxSelected>>"
        )  # ,comboclick / def comboclick(event): / m= label(root, text= c.get()).pack()
        c.place(x=80, y=120)

        Options = ["", "Elzawahem", "Elpostan"]
        clicked = StringVar()
        clicked.set(Options[0])

        c = ttk.Combobox(f1, width=10, values=Options)
        c.current(0)
        c.bind(
            "<<ComboboxSelected>>"
        )  # ,comboclick / def comboclick(event): / m= label(root, text= c.get()).pack()
        c.place(x=80, y=150)

    def feedback_Data(self):
        table = DataTable(
            self, bd=2, width=self.w, height=self.h, bg="white"
        )  # bd 2d/3dنوع البرورد       وممكن لاتحدد الطول والعرض أوتضيفة على على السطر التالى

        table.place(x=117, y=0, width=1000, height=800)
        table.set_headings()

    def Settings(self):
        f = Frame(
            self, bd=2, width=self.w, height=self.h, bg="white"
        )  # bd 2d/3dنوع البرورد       وممكن لاتحدد الطول والعرض أوتضيفة على على السطر التالى   ,width=1247, height=704
        f.place(x=117, y=0)

    def Help(self):
        f = Frame(
            self, bd=2, width=self.w, height=self.h, bg="white"
        )  # bd 2d/3dنوع البرورد       وممكن لاتحدد الطول والعرض أوتضيفة على على السطر التالى   ,width=1247, height=704
        f.place(x=117, y=0)

        # **************************sound**********************
        # pygame.mixer.init()
        # def play(self):
        # pygame.mixer.music.load("E:\\New folder\\Egyptian Development Bank\\audiosounds\\sounds.res")
        # pygame.mixer.music.play(loops=0)

        # sw = self.winfo_screenwidth() - 19
        # print(f'sw =', sw)
        # sh=self.h-19
        # scroll_y=Scrollbar(f2,orient=VERTICAL)
        # scroll_y.pack(side=LEFT, fill=Y, expand=1)  #side=LEFT , anchor=N
        # scroll_x=Scrollbar(f2,orient=HORIZONTAL)
        # scroll_x.pack(side=BOTTOM, fill=X, expand=1)#side=TOP/BOTTOM
        # scroll_x.place(x=16,y=686,width=1230)
        # scroll_y.place(x=0,y=0,height=703)

        # textarea = ttk.Treeview(f2, columns= ( 'name', 'telephone', 'National ID','Home Address','field ID','areaa','irrigation periud','irrigation period','name','name'), yscrollcommand=scroll_y.set,xscrollcommand =scroll_x.set)
        # textarea.place(x=16,y=0,width=1214, height=650)#x=1,y=1,width=130, height=600
        # textarea.pack(fill=BOTH,expand=1)

        # scroll_x.config(command=textarea.xview) #عند وجود مشكلة فى الظهور
        # scroll_y.config(command=textarea.yview)

        # textarea['show']='headings'
        # textarea.heading('name',text='الاسم',width=130)
        # textarea.heading('telephone',text='التليفون')
        # textarea.heading('National ID',text='الرقم القومى')
        # textarea.heading('Home Address',text='عنوان المنزل')
        # textarea.heading('field ID',text='field ID')
        # textarea.heading('areaa',text='areaa')
        # textarea.heading('irrigation period',text='فترة الرى')
        # textarea.heading('name',text='الاسم')
        # textarea.heading('name',text='الاسم')
        # textarea.heading('name',text='الاسم')

        name_var = StringVar()
        telephon_var = StringVar()
        National_ID_var = StringVar()
        Home_Address_var = StringVar()
        field_ID_var = StringVar()
        areaa_var = StringVar()
        irrigation_period_var = StringVar()

        # *************************************************************************************************************************

        self.line_numbers = tk.Text(self, bg="grey", fg="white")
        first_100_numbers = [str(n + 1) for n in range(100)]

        menu = tk.Menu(self, bg="lightgrey", fg="black")
        sub_menu_items = ["file", "edit", "tools", "help"]
        self.generate_sub_menus(sub_menu_items)
        self.configure(menu=self.menu)

    def generate_sub_menus(self, sub_menu_items):
        window_methods = [
            method_name
            for method_name in dir(self)
            if callable(getattr(self, method_name))
        ]
        tkinter_methods = [
            method_name
            for method_name in dir(tk.Tk)
            if callable(getattr(tk.Tk, method_name))
        ]
        my_methods = [method for method in set(window_methods) - set(tkinter_methods)]
        my_methods = sorted(my_methods)
        for item in sub_menu_items:
            sub_menu = tk.Menu(Menu, tearoff=0, bg="lightgrey", fg="black")
            matching_methods = []
            for method in my_methods:
                if method.startswith(item):
                    matching_methods.append(method)
                    for match in matching_methods:
                        actual_method = getattr(self, match)
                        method_shortcut = actual_method.__doc__.strip()
                        friendly_name = " ".join(match.split("_")[1:])
                        sub_menu.add_command(
                            label=friendly_name.title(),
                            command=actual_method,
                            accelerator=method_shortcut,
                        )
                        self.menu.add_cascade(label=item.title(), menu=sub_menu)

        self.right_click_menu = Menu(self, bg="lightgrey", fg="black", tearoff=0)
        self.right_click_menu.add_command(label="Cut", command=self.edit_cut)
        self.right_click_menu.add_command(label="Copy", command=self.edit_copy)
        self.right_click_menu.add_command(label="Paste", command=self.edit_paste)

    def cut(self, event=None):
        self.event_generate("<<Cut>>")

    def copy(self, event=None):
        self.event_generate("<<Copy>>")

    def paste(self, event=None):
        self.event_generate("<<Paste>>")

    # self.bind('<Control-a>', self.select_all)
    # self.bind('<Control-c>', self.copy)
    # self.bind('<Control-v>', self.paste)
    # self.bind('<Control-x>', self.cut)

    def edit_copy(self, event=None):
        """
        Ctrl+C
        """
        self.textarea.event_generate("<Control-c>")

    def edit_cut(self, event=None):
        """
        Ctrl+X
        """
        self.textarea.event_generate("<Control-x>")
        self.line_numbers.force_update()

    def edit_paste(self, event=None):
        """
        Ctrl+V
        """
        self.textarea.event_generate("<Control-v>")
        self.line_numbers.force_update()
        self.highlighter.force_highlight()

    def force_highlight(self):
        self.highlight()

    # class LineNumbers(tk.Text):
    def force_update(self):
        self.on_key_press()

    # ****************************************************************************************************************************************************
    def shose_crops(self):
        f = Frame(
            self, bd=2, width=self.w, height=self.h, bg="white"
        )  # bd 2d/3dنوع البرورد       وممكن لاتحدد الطول والعرض أوتضيفة على على السطر التالى   ,width=1247, height=704
        f.place(x=117, y=0)
        f1 = Frame(self, bd=2, width=210, height=self.h, bg="gold")
        f1.place(x=117, y=0)
        f2 = Frame(self, bd=2, width=210, height=self.h, bg="gold")
        f2.place(x=328, y=0)
        f3 = Frame(self, bd=2, width=210, height=self.h, bg="gold")
        f3.place(x=539, y=0)

        # *****************************الاطار الاول*****************************************
        t = Label(f1, text="Meteorology ", fg="red", bg="gold", font=("tajawal", 14))
        t.place(x=55, y=0)
        t2 = Label(
            f1, text="R\u2099:", fg="black", bg="gold", font=("tajawal", 14)
        )  # Rn
        t2.place(x=0, y=20)
        t3 = Label(f1, text="G :", fg="black", bg="gold", font=("tajawal", 14))
        t3.place(x=0, y=46)
        t4 = Label(f1, text="\u0394 :", fg="black", bg="gold", font=("tajawal", 14))
        t4.place(x=0, y=72)
        t5 = Label(
            f1, text="U\u2082:", fg="black", bg="gold", font=("tajawal", 14)
        )  # u2
        t5.place(x=0, y=98)
        t6 = Label(
            f1, text="e\u209b:", fg="black", bg="gold", font=("tajawal", 14)
        )  # es
        t6.place(x=0, y=124)
        t7 = Label(
            f1, text="e\u2090:", fg="black", bg="gold", font=("tajawal", 14)
        )  # ea
        t7.place(x=0, y=150)
        t8 = Label(f1, text="T :", fg="black", bg="gold", font=("tajawal", 14))  # dlta
        t8.place(x=0, y=176)
        t9 = Label(
            f1, text="\u0194 :", fg="black", bg="gold", font=("tajawal", 14)
        )  # gama
        t9.place(x=0, y=202)
        t9 = Label(
            f1, text="ET\u2092", fg="red", bg="gold", font=("tajawal", 14)
        )  # ETo
        t9.place(x=0, y=227)

        t11 = Label(f1, text="Crop type:", fg="black", bg="gold", font=("tajawal", 14))
        t11.place(x=0, y=249)
        t12 = Label(f1, text="Kc ini. :", fg="black", bg="gold", font=("tajawal", 14))
        t12.place(x=0, y=276)
        t12 = Label(f1, text="ETc ini.", fg="red", bg="gold", font=("tajawal", 14))
        t12.place(x=0, y=302)
        t14 = Label(f1, text="Kc mid. :", fg="black", bg="gold", font=("tajawal", 14))
        t14.place(x=0, y=328)
        t12 = Label(f1, text="ETc mid.", fg="red", bg="gold", font=("tajawal", 14))
        t12.place(x=0, y=354)
        t16 = Label(f1, text="Kc end. :", fg="black", bg="gold", font=("tajawal", 14))
        t16.place(x=0, y=380)
        t12 = Label(f1, text="ETc end.", fg="red", bg="gold", font=("tajawal", 14))
        t12.place(x=0, y=406)
        t12 = Label(
            f1,
            text="Readily available water",
            fg="red",
            bg="gold",
            font=("tajawal", 14),
        )  # ETc
        t12.place(x=0, y=427)

        t18 = Label(f1, text="AW :", fg="black", bg="gold", font=("tajawal", 14))
        t18.place(x=0, y=450)
        t19 = Label(
            f1, text="Z\u1d63  :", fg="black", bg="gold", font=("tajawal", 14)
        )  # zr
        t19.place(x=0, y=476)
        t20 = Label(f1, text="P   :", fg="black", bg="gold", font=("tajawal", 14))
        t20.place(x=0, y=502)
        t20 = Label(f1, text="RAW", fg="red", bg="gold", font=("tajawal", 14))
        t20.place(x=0, y=528)

        t21 = Label(
            f1, text="Leaching Requirements", fg="red", bg="gold", font=("tajawal", 14)
        )
        t21.place(x=0, y=548)
        t22 = Label(f1, text="Soil type :", fg="black", bg="gold", font=("tajawal", 14))
        t22.place(x=0, y=573)
        t23 = Label(f1, text="ECw :", fg="black", bg="gold", font=("tajawal", 14))
        t23.place(x=0, y=599)
        t24 = Label(f1, text="EC\u2091 :", fg="black", bg="gold", font=("tajawal", 14))
        t24.place(x=0, y=624)
        t24 = Label(f1, text="LR :", fg="red", bg="gold", font=("tajawal", 14))
        t24.place(x=0, y=651)

        e1 = Entry(
            f1, width=9, bd=3, fg="red", justify="center"
        )  # justify='right',height=1
        e1.place(x=39, y=23)
        e2 = Entry(
            f1, width=9, bd=3, justify="center"
        )  # justify='right',height=1  /textvarible=  /
        e2.place(x=39, y=49)
        e3 = Entry(
            f1, width=9, bd=3, justify="center"
        )  #  ,textvariable=name استدعاء المتغير -----+ name=stringvar()
        e3.place(x=39, y=75)
        e4 = Entry(f1, width=9, bd=3, justify="center")
        e4.place(x=39, y=101)
        e5 = Entry(f1, width=9, bd=3, justify="center")
        e5.place(x=39, y=127)
        e6 = Entry(f1, width=9, bd=3, justify="center")
        e6.place(x=39, y=153)
        e7 = Entry(f1, width=9, bd=3, justify="center")
        e7.place(x=39, y=179)
        e8 = Entry(f1, width=9, bd=3, justify="center")
        e8.place(x=39, y=205)
        e9 = Entry(
            f1,
            width=9,
            bd=3,
            justify="center",
            relief=SUNKEN,
            textvariable=sys.displayhook,
        )
        e9.place(x=39, y=231)

        e10 = Entry(f1, width=7, bd=3, justify="center")
        e10.place(x=85, y=279)
        e11 = Entry(f1, width=7, bd=3, justify="center")
        e11.place(x=85, y=305)
        e12 = Entry(f1, width=7, bd=3, justify="center")
        e12.place(x=85, y=331)
        e13 = Entry(f1, width=7, bd=3, justify="center")
        e13.place(x=85, y=357)
        e14 = Entry(f1, width=7, bd=3, justify="center")
        e14.place(x=85, y=383)
        e15 = Entry(f1, width=7, bd=3, justify="center")
        e15.place(x=85, y=409)

        e16 = Entry(f1, width=7, bd=3, justify="center")
        e16.place(x=60, y=453)
        e17 = Entry(f1, width=7, bd=3, justify="center")
        e17.place(x=60, y=479)
        e18 = Entry(f1, width=7, bd=3, justify="center")
        e18.place(x=60, y=505)
        e19 = Entry(f1, width=7, bd=3, justify="center")
        e19.place(x=60, y=531)

        e20 = Entry(f1, width=9, bd=3, fg="red", justify="center")
        e20.place(x=55, y=601)
        e21 = Entry(
            f1, width=9, bd=3, justify="center"
        )  # justify='right',height=1  /textvarible=  / ,fg='red'
        e21.place(x=55, y=627)
        e22 = Entry(f1, width=9, bd=3, justify="center")
        e22.place(x=55, y=653)

        t2s = Label(
            f1, text="MJ.m\u00b2/day", fg="black", bg="gold", font=("tajawal", 14)
        )
        t2s.place(x=100, y=25)
        t3s = Label(
            f1, text="MJ.m\u00b2/day", fg="black", bg="gold", font=("tajawal", 14)
        )
        t3s.place(x=100, y=49)
        t4s = Label(f1, text="m/s", fg="black", bg="gold", font=("tajawal", 14))
        t4s.place(x=100, y=75)
        t5s = Label(f1, text="m/s", fg="black", bg="gold", font=("tajawal", 14))
        t5s.place(x=100, y=101)
        t6s = Label(f1, text="KP\u2090", fg="black", bg="gold", font=("tajawal", 14))
        t6s.place(x=100, y=127)
        t7s = Label(f1, text="KP\u2090", fg="black", bg="gold", font=("tajawal", 14))
        t7s.place(x=100, y=153)
        t8s = Label(f1, text="\u00b0c", fg="black", bg="gold", font=("tajawal", 14))
        t8s.place(x=100, y=179)
        t9s = Label(
            f1, text="KP\u2090/\u00b0c", fg="black", bg="gold", font=("tajawal", 14)
        )
        t9s.place(x=100, y=203)
        t10s = Label(f1, text="mm/day", fg="black", bg="gold", font=("tajawal", 14))
        t10s.place(x=100, y=225)

        t11s = Label(f1, text="mm/day", fg="black", bg="gold", font=("tajawal", 14))
        t11s.place(x=135, y=299)
        t12s = Label(f1, text="mm/day", fg="black", bg="gold", font=("tajawal", 14))
        t12s.place(x=135, y=351)
        t13s = Label(f1, text="mm/day", fg="black", bg="gold", font=("tajawal", 14))
        t13s.place(x=135, y=403)

        t13s = Label(f1, text="mm/m", fg="black", bg="gold", font=("tajawal", 14))
        t13s.place(x=115, y=453)
        t13s = Label(f1, text="%", fg="black", bg="gold", font=("tajawal", 14))
        t13s.place(x=115, y=479)

        t20s = Label(f1, text="dS/m", fg="black", bg="gold", font=("tajawal", 14))
        t20s.place(x=120, y=596)
        t21s = Label(f1, text="dS/m", fg="black", bg="gold", font=("tajawal", 14))
        t21s.place(x=120, y=621)

        Options = [
            "",
            "rice",
            "sugar beet",
            "potato",
            "wheat",
            "tomato",
            "cotton",
            "cucumber",
        ]
        clicked = StringVar()
        clicked.set(Options[0])

        c = ttk.Combobox(f1, width=10, values=Options)
        c.current(0)
        c.bind(
            "<<ComboboxSelected>>"
        )  # ,comboclick / def comboclick(event): / m= label(root, text= c.get()).pack()
        c.place(x=94, y=256)

        Options2 = ["", "sand", "gly", ""]
        clicked2 = StringVar()
        clicked2.set(Options2[0])

        c2 = ttk.Combobox(f1, width=10, values=Options)
        c2.current(0)
        c2.bind(
            "<<ComboboxSelected>>"
        )  # ,comboclick / def comboclick(event): / m= label(root, text= c.get()).pack()
        c2.place(x=90, y=577)

        # *****************************الاطار الثانى*****************************************
        t25 = Label(
            f2, text="Soil water depletion", fg="red", bg="gold", font=("tajawal", 14)
        )
        t25.place(x=15, y=0)
        t26 = Label(f2, text="D\u1d62-1 :", fg="black", bg="gold", font=("tajawal", 14))
        t26.place(x=0, y=23)
        t27 = Label(f2, text="R :", fg="black", bg="gold", font=("tajawal", 14))
        t27.place(x=0, y=46)
        t27 = Label(f2, text="D\u1d62 =", fg="black", bg="gold", font=("tajawal", 14))
        t27.place(x=0, y=72)
        t28 = Label(f2, text="E\u2090 :", fg="black", bg="gold", font=("tajawal", 14))
        t28.place(x=0, y=98)
        t27 = Label(f2, text="Dg =", fg="red", bg="gold", font=("tajawal", 14))
        t27.place(x=0, y=120)

        t29 = Label(
            f2, text="If selected rice", fg="red", bg="gold", font=("tajawal", 14)
        )
        t29.place(x=0, y=145)
        t30 = Label(f2, text="PERC", fg="black", bg="gold", font=("tajawal", 14))
        t30.place(x=0, y=166)
        t31 = Label(
            f2, text="Regular irrigation :", fg="black", bg="gold", font=("tajawal", 14)
        )
        t31.place(x=0, y=187)
        t31 = Label(
            f2, text="D\u1d63\u1d62 :", fg="black", bg="gold", font=("tajawal", 14)
        )
        t31.place(x=0, y=212)
        t27 = Label(f2, text="Dg =", fg="red", bg="gold", font=("tajawal", 14))
        t27.place(x=0, y=233)
        t32 = Label(
            f2, text="Sat irrigation :", fg="black", bg="gold", font=("tajawal", 14)
        )
        t32.place(x=0, y=258)
        t32 = Label(f2, text="SAT :", fg="black", bg="gold", font=("tajawal", 14))
        t32.place(x=0, y=281)
        t27 = Label(f2, text="Dg =", fg="red", bg="gold", font=("tajawal", 14))
        t27.place(x=0, y=304)
        t33 = Label(
            f2,
            text="1st irrigation in midstage",
            fg="black",
            bg="gold",
            font=("tajawal", 14),
        )
        t33.place(x=0, y=329)
        t33 = Label(f2, text="WL :", fg="black", bg="gold", font=("tajawal", 14))
        t33.place(x=0, y=352)
        t27 = Label(f2, text="Dg =", fg="red", bg="gold", font=("tajawal", 14))
        t27.place(x=0, y=375)

        t33 = Label(
            f2,
            text="Canal`s available water",
            fg="red",
            bg="gold",
            font=("tajawal", 14),
        )
        t33.place(x=0, y=400)
        t33 = Label(f2, text="Qf", fg="black", bg="gold", font=("tajawal", 14))
        t33.place(x=0, y=423)
        t33 = Label(f2, text="Af", fg="black", bg="gold", font=("tajawal", 14))
        t33.place(x=0, y=446)
        t33 = Label(
            f2, text="L\u2092\u2099 :", fg="black", bg="gold", font=("tajawal", 14)
        )
        t33.place(x=0, y=472)
        t33 = Label(f2, text="CAW", fg="red", bg="gold", font=("tajawal", 14))
        t33.place(x=0, y=498)
        t33 = Label(f2, text="Ac :", fg="black", bg="gold", font=("tajawal", 14))
        t33.place(x=0, y=524)
        t33 = Label(f2, text="GIR =", fg="red", bg="gold", font=("tajawal", 14))
        t33.place(x=0, y=549)
        t33 = Label(
            f2, text="If selected rice :", fg="red", bg="gold", font=("tajawal", 14)
        )
        t33.place(x=0, y=570)
        t33 = Label(
            f2,
            text="1st irrigation in midstage",
            fg="black",
            bg="gold",
            font=("tajawal", 14),
        )
        t33.place(x=0, y=591)
        t33 = Label(f2, text="GIR =", fg="red", bg="gold", font=("tajawal", 14))
        t33.place(x=0, y=616)
        t33 = Label(
            f2, text="Regular irrigation :", fg="black", bg="gold", font=("tajawal", 14)
        )
        t33.place(x=0, y=637)
        t33 = Label(f2, text="GIR =", fg="red", bg="gold", font=("tajawal", 14))
        t33.place(x=0, y=662)

        e23 = Entry(f2, width=9, bd=3, justify="center")
        e23.place(x=55, y=23)
        e24 = Entry(f2, width=9, bd=3, justify="center")
        e24.place(x=55, y=49)
        e25 = Entry(f2, width=9, bd=3, justify="center")
        e25.place(x=55, y=75)
        e26 = Entry(f2, width=9, bd=3, justify="center")
        e26.place(x=55, y=101)
        e27 = Entry(f2, width=9, bd=3, justify="center")
        e27.place(x=55, y=127)

        e28 = Entry(f2, width=9, bd=3, justify="center")
        e28.place(x=60, y=168)
        e29 = Entry(f2, width=9, bd=3, justify="center")
        e29.place(x=60, y=213)
        e30 = Entry(f2, width=9, bd=3, justify="center")
        e30.place(x=60, y=239)

        e30 = Entry(f2, width=9, bd=3, justify="center")
        e30.place(x=60, y=284)
        e31 = Entry(f2, width=9, bd=3, justify="center")
        e31.place(x=60, y=310)
        e31 = Entry(f2, width=9, bd=3, justify="center")
        e31.place(x=60, y=355)
        e31 = Entry(f2, width=9, bd=3, justify="center")
        e31.place(x=60, y=381)

        e20 = Entry(f2, width=9, bd=3, fg="red", justify="center")
        e20.place(x=30, y=423)
        e20 = Entry(f2, width=9, bd=3, fg="red", justify="center")
        e20.place(x=30, y=449)
        e20 = Entry(f2, width=9, bd=3, fg="red", justify="center")
        e20.place(x=55, y=475)
        e20 = Entry(f2, width=9, bd=3, fg="red", justify="center")
        e20.place(x=60, y=501)
        e20 = Entry(f2, width=9, bd=3, fg="red", justify="center")
        e20.place(x=60, y=527)
        e20 = Entry(f2, width=9, bd=3, fg="red", justify="center")
        e20.place(x=60, y=553)

        e20 = Entry(f2, width=9, bd=3, fg="red", justify="center")
        e20.place(x=60, y=617)
        e20 = Entry(f2, width=9, bd=3, fg="red", justify="center")
        e20.place(x=60, y=665)

        t22s = Label(f2, text="mm/day", fg="black", bg="gold", font=("tajawal", 14))
        t22s.place(x=120, y=25)
        t23s = Label(f2, text="mm", fg="black", bg="gold", font=("tajawal", 14))
        t23s.place(x=120, y=47)
        t24s = Label(f2, text="mm/day", fg="black", bg="gold", font=("tajawal", 14))
        t24s.place(x=120, y=69)
        t25s = Label(f2, text="%", fg="black", bg="gold", font=("tajawal", 14))
        t25s.place(x=120, y=95)
        t26s = Label(f2, text="mm", fg="black", bg="gold", font=("tajawal", 14))
        t26s.place(x=120, y=121)

        t26s = Label(f2, text="mm", fg="black", bg="gold", font=("tajawal", 14))
        t26s.place(x=125, y=168)
        t27s = Label(f2, text="mm", fg="black", bg="gold", font=("tajawal", 14))
        t27s.place(x=125, y=213)
        t28s = Label(f2, text="mm", fg="black", bg="gold", font=("tajawal", 14))
        t28s.place(x=125, y=239)
        t28s = Label(f2, text="mm", fg="black", bg="gold", font=("tajawal", 14))
        t28s.place(x=125, y=284)
        t29s = Label(f2, text="mm", fg="black", bg="gold", font=("tajawal", 14))
        t29s.place(x=125, y=310)
        t29s = Label(f2, text="mm", fg="black", bg="gold", font=("tajawal", 14))
        t29s.place(x=125, y=355)
        t29s = Label(f2, text="mm", fg="black", bg="gold", font=("tajawal", 14))
        t29s.place(x=125, y=381)

        t20s = Label(
            f2, text="m\u00b3/feed.day", fg="black", bg="gold", font=("tajawal", 14)
        )
        t20s.place(x=92, y=422)
        t20s = Label(f2, text="feed", fg="black", bg="gold", font=("tajawal", 14))
        t20s.place(x=92, y=447)
        t20s = Label(f2, text="m", fg="black", bg="gold", font=("tajawal", 14))
        t20s.place(x=120, y=475)
        t20s = Label(f2, text="m\u00b3", fg="black", bg="gold", font=("tajawal", 14))
        t20s.place(x=120, y=501)
        t20s = Label(f2, text="m\u00b2", fg="black", bg="gold", font=("tajawal", 14))
        t20s.place(x=120, y=527)
        t20s = Label(f2, text="m\u00b3", fg="black", bg="gold", font=("tajawal", 14))
        t20s.place(x=120, y=553)

        t20s = Label(f2, text="m\u00b3", fg="black", bg="gold", font=("tajawal", 14))
        t20s.place(x=120, y=617)
        t20s = Label(f2, text="m\u00b3", fg="black", bg="gold", font=("tajawal", 14))
        t20s.place(x=120, y=665)

        # ******************************************** الاطار رقم 3 ***************************************************
        t33 = Label(
            f3, text="Sat irrigation :", fg="black", bg="gold", font=("tajawal", 14)
        )
        t33.place(x=0, y=0)
        t33 = Label(f3, text="GIR =", fg="red", bg="gold", font=("tajawal", 14))
        t33.place(x=0, y=23)
        t33 = Label(f3, text="GIR =", fg="red", bg="gold", font=("tajawal", 14))
        t33.place(x=0, y=23)
        t33 = Label(f3, text="Hydro", fg="red", bg="gold", font=("tajawal", 14))
        t33.place(x=0, y=23)

        e20 = Entry(f3, width=9, bd=3, fg="red", justify="center")
        e20.place(x=60, y=26)

        t20s = Label(f3, text="m\u00b3", fg="black", bg="gold", font=("tajawal", 14))
        t20s.place(x=120, y=26)

        # drop=OptionMenu(f1,clicked,*Options) # ,command=selected  / def selected(event): / m= label(root, text= clicked.get()).pack()  /  if clicked.get() == 'friday': /  m= label(root, text= "Yay its friday ".pack() / else: /  m= label(root, text= clicked.get()).pack()
        # drop.place(x=100,y=340)

    # \u209b --s  /

    # x=time.strftime('%d/%m/%y',time.localtime(time.time()))

    def say_hello(self):
        messagebox.showinfo("Hello", "Hello World!")

        # **********************************************************************************************************

        # def EDB_App(self):
        # con=sqlite3.connector(host='localhost',user='root',password='',database='EDB_App')
        # cur=con.cursor()
        # cur.execute("insert into EDB values($s,$s,$s,$s,$s,$s,$s)",(name_var.get(),telephon_var.get(),National_ID_var.get() ))
        # con.commit()
        # con.close()
        # def fetch_all(self):
        # con = sqlite3.connector(host='localhost',user='root',password='',database='EDB_App')
        # cur = con.execute('select * from EDB_App')
        # rows=
        table.bind("ButtonRelease,show")

    def add(self):
        con = sqlite3.connector(
            host="localhost", user="root", password="", database="EDB_App"
        )
        cur = con.cursor()
        if (
            len(name_var.get()) == 0
            or len(telephon_var.get()) == 0
            or len(National_ID_var.get()) == 0
        ):
            mb.showerror("error", "all data should be required")
        else:
            cur.execute(
                "insert into EDB values($s,$s,$s,$s,$s,$s,$s)",
                (name_var.get(), telephon_var.get(), National_ID_var.get()),
            )
            con.commit()
            con.close()
            mb.showinfo("successfully added , data inserted successfuly")
            name_var.delet(0, "end")
            telephon_var.delet(0, "end")
            National_ID_var.delet(0, "end")
            # read.()

    def read(self):
        con = sqlite3.connector(
            host="localhost", user="root", password="", database="EDB_App"
        )
        cur = con.cursor()
        cur.execute("select * from student")
        myresults = cur.fetchall()
        Table.delete(*table.get_children())
        for res in myresults:
            Table.insert("", "end", Values=res)
        con.close()

    def show(self, ev):
        data = table.focus()
        alldata = table.item(data)
        val = alldata["values"]
        name.set(val[1])
        last.set(val[2])
        cin.set(val[3])
        emall.set(val[4])

    def close(self):
        self.screen.destroy()


class TextArea(tk.Text):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)
        master = master
        self.config(wrap=tk.WORD)
        screen = self.start()
        screen.pack(fill=BOTH, expand=True)


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        text_area = TextArea(self, bg="white", fg="black", undo=True)
        scrollbar = ttk.Scrollbar(orient="vertical", command=self.scroll_text)
        text_area.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # self.screen = closing()
        # self.screen.pack(fill=BOTH, expand=True)
        # print(BOTH)

        # padx : makes padding horizontally
        # pady: makes padding vertically between widgets
        # *************************************************
        # quiz_frame = pro.frame(pro)
        # work_frame = pro.frame(pro)

        # logo_quiz=pro.Label(quiz_frame,image=pro.photoimage(fill='logo.png'))
        # logo_quiz.pack(pady=20)
        # heading_quiz=pro.Label(quiz_frame,text='This is quiz frame',font=16)
        # heading_quiz.pack(pady=20)

        # quiz_frame.pack(fill='both',expand=1)

        # work_frame.pack(fill='both',expand=1)
        # quiz_frame.pack(fill='both',expand=1)
        # work_frame.forget()

        # *******************************************************

        # def open1 ():
        # webbrowser.open_new()

        # **************** جدول محتويات ****************
        # scroll_y=Scrollbar(f1,orient=VERTICAL)
        # scroll_x=Scrollbar(f1,orient=HORIZONTAL)

        # self.tables=f2.Treeview(f3,columns=("t1","t2",'',''), scrollcommand= scroll_x.set, scrollcommand=scroll_y.set) #لكتابة العناوين
        # self.tables.place(x=1,y=1,width=1130, height=600)
        # scroll_x.pack(side=BOTTON,fill=X)
        # scroll_y.pack(side=LEFT,fill=Y,expand=1)

        # scroll_x.config(command=self.tables.xview) #عند وجود مشكلة فى الظهور
        # scroll_y.config(command=self.tables.yview)
        # self.tables['show']=''

        # scroll_y.config(command= textarea.yview)

        # textarea= Text (f1,yscrollcommand =scroll_y.set)

        # ===========bill======
        # ti=Label(f1,text='bill',fg='white',bg='#0B2F3A',font=('tajawal',16,'bold'))
        # ti.place(x=1020,y=630)
        # f2= Frame(self.pro,bd=2,width=2000, height=1000, bg='#0B2F3A')#bd 2d/3dنوع البرورد
        # f1.place(x=0,y=0)
        # scroll_y=Scrollbar(f2,orient=VERTICAL)
        # self.textarea= Text (f2,yscrollcommand =scroll_y.set)
        # scroll_y.pack(side=LEFT,fill=Y)
        # scroll_y.config(command= textarea.yview)
        # self.textarea.pack(fill=BOTH,expand=1)


if __name__ == "__main__":
    Window().mainloop()
