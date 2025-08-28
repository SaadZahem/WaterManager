from datetime import date, timedelta
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import ttk
from typing import NamedTuple, Callable

from ..widgets.scrollable import Scrollable


class InputItem[T](NamedTuple):
    validate: Callable = str
    factory: Callable = str
    choices: list[T] | None = None


class GIRFrame(ttk.Frame):
    CROP_TYPES = [
        "Wheat",
        "Rice",
    ]

    def __init__(self, master: tk.Misc):
        super().__init__(master)

        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # links
        self.dates: list[DateEntry] = []

        # styles
        from .styles import bold_font

        # head
        head = ttk.Frame(self, padding=8)
        self.head_details = {
            "Crop": InputItem[str](choices=self.CROP_TYPES),
            "Plant Date": InputItem(factory=date),
            "Harvest Date": InputItem(factory=date),
            "errmsg": ttk.Label(
                head, anchor="center", foreground="red", font=bold_font
            ),
            "sep": ttk.Separator(head, orient="horizontal"),
            "Area (m²)": InputItem(float),
            "AW": InputItem(float),
            "Ece": InputItem(float),
            "Ecw": InputItem(float),
            "MAP": InputItem(float),
            "Zn": InputItem(float),
            "Zo": InputItem(float),
            "Zx": InputItem(float),
            "to": InputItem(float),
            "tx": InputItem(float),
            "h": InputItem(float),
        }
        for row, (label, item) in enumerate(self.head_details.items()):
            head.grid_rowconfigure(row, weight=1, pad=4)

            if isinstance(item, ttk.Widget):
                item.grid(row=row, column=0, columnspan=3, sticky="WE", pady=8)
                continue

            ttk.Label(head, text=label, font=bold_font).grid(column=0, row=row)

            if item.choices:
                widget = ttk.Combobox(head, values=item.choices)

            elif item.factory is date:
                # current issue: calendar dropdown is self-destroyed when the widget is originally focused
                widget = DateEntry(head, date_pattern="y-mm-dd")
                widget.bind("<<DateEntrySelected>>", self.verify_dates)
                self.dates.append(widget)
            else:
                widget = ttk.Entry(head, justify="center")

            widget.grid(row=row, column=1, sticky="W", columnspan=2)

        head.grid(row=0, column=0, sticky="NWS")

        # separator
        ttk.Separator(self, orient="vertical").grid(
            row=0, column=1, padx=8, sticky="ns"
        )

        # body
        scroll = Scrollable(self)
        scroll.grid(row=0, column=2, sticky="NEWS")
        scroll.scrollbar.grid(row=0, column=3, sticky="NS")

        body = scroll.frame
        inputs = {
            "Zr": "",
            "TAW": "",
            "RAW": "",
            "ETa (mm/day)": "",
            "Precipitation (mm/day)": "",
            "Di": "",
            "LR": "",
            "R (on/off)": False,
        }
        outputs = {
            "F": "",
            "Dg": "",
            "GIR": "",
        }
        loop = {
            "": lambda r: current + timedelta(days=~-r),
            **inputs,
            **outputs,
        }
        current = date.today()
        for row in range(61):
            for column, (key, value) in enumerate(loop.items(), start=2):
                if row == 0:
                    widgets = [ttk.Label(body, text=key, font=bold_font)]

                elif key in inputs:
                    variable = tk.StringVar()
                    widgets = [
                        ttk.Entry(
                            body,
                            justify="center",
                            validate="focusout",
                            # validatecommand=(self.register(self.validate), "%P", "%W"),
                            textvariable=variable,
                            width=8,
                        )
                    ]
                    # self.variables[value, row] = variable
                    # self.widgets[str(widget)] = row

                elif column == 2:
                    widgets = [
                        ttk.Label(
                            body,
                            text=value(row).strftime("%a"),
                            style="Const.TLabel",
                            anchor="center",
                        ),
                        ttk.Label(
                            body,
                            text=value(row).strftime("%j"),
                            style="Const.TLabel",
                            anchor="center",
                        ),
                        ttk.Label(
                            body, text=value(row), style="Const.TLabel", anchor="center"
                        ),
                    ]
                    column = 0
                else:
                    variable = tk.StringVar()
                    widgets = [
                        ttk.Label(
                            body,
                            text=value,
                            style="Output.TLabel",
                            textvariable=variable,
                            anchor="center",
                        )
                    ]
                    # self.outcome[row] = variable

                for i, widget in enumerate(widgets, column):
                    widget.grid(row=row, column=i, sticky="NEWS", ipadx=5)

        # Ensure all elements are visible at once
        self.update()
        scroll.configure(width=body.winfo_reqwidth())

    def verify_dates(self, event):
        plant, harvest = self.dates

        if plant.get_date() < harvest.get_date():
            msg = ""
        else:
            msg = "Error:\nharvest date must be after plant date"

        self.head_details["errmsg"].configure(text=msg)


if __name__ == "__main__":
    root = tk.Tk()
    GIRFrame(root).pack(fill="both", expand=1)
    root.mainloop()
