from dataclasses import dataclass, field
from datetime import date
from functools import partial
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import ttk
from typing import Callable

from ..widgets.datatable import DataTable


@dataclass
class InputItem:
    validate: Callable = str
    factory: Callable = str
    choices: list[str] | None = None
    var: tk.StringVar = field(default_factory=tk.StringVar)
    valid = False


class GIRFrame(ttk.Frame):
    CROP_TYPES = [
        "Wheat",
        "Rice",
    ]

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self["padding"] = (0, 4, 8, 4)

        # links
        self.dates: list[DateEntry] = []

        # styles
        from .styles import bold_font

        # head
        head = ttk.Frame(self, padding=8)
        self.head_details = {
            "Crop": InputItem(choices=self.CROP_TYPES),
            "Plant Date": InputItem(factory=date),
            "Harvest Date": InputItem(factory=date),
            "errmsg": ttk.Label(
                head, anchor="center", foreground="red", font=bold_font
            ),
            "sep": ttk.Separator(head, orient="horizontal"),
        }
        self.required = {
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
        self.head_details.update(self.required)
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
                widget = ttk.Entry(
                    head,
                    justify="center",
                    textvariable=item.var,
                    validate="focusout",
                    validatecommand=(
                        self.register(partial(self._validate, item=item)),
                        "%P",
                        "%W",
                    ),
                )

            widget.grid(row=row, column=1, sticky="W", columnspan=2)

        head.grid(row=0, column=0, sticky="NWS")

        # separator
        ttk.Separator(self, orient="vertical").grid(
            row=0, column=1, padx=8, sticky="ns"
        )

        # body
        headers = [
            "TAW",
            "RAW",
            "ETa (mm/day)",
            "Precipitation (mm/day)",
            "Di",
            "LR",
            "R (on/off)",
            "F",
            "Dg",
            "GIR",
        ]
        self.table = DataTable(self, headers, callback=self.verify_all, output_count=3)
        self.table.grid(row=0, column=2, sticky="NEWS")
        self.table.scrollbar.grid(row=0, column=3, sticky="NS")

        # Ensure all elements are visible at once
        self.update_idletasks()
        self.table.configure(width=self.table.frame.winfo_reqwidth())

    def _validate(self, newvalue: str, widgetname: str, *, item: InputItem) -> bool:
        entry = self.nametowidget(widgetname)

        try:
            item.validate(newvalue)
        except ValueError:
            item.valid = not newvalue
            entry.configure(style="Invalid.TEntry")
        else:
            item.valid = True
            entry.configure(style="TEntry")

        return item.valid

    def verify_dates(self, _event: tk.Event) -> None:
        plant, harvest = self.dates
        start = plant.get_date()
        end = harvest.get_date()

        if start < end:
            self.table.populate(start, end)
            self.table.configure(width=self.table.frame.winfo_reqwidth())
            self.winfo_toplevel().geometry("")  # ignore user selected size
            msg = ""
        else:
            msg = "Error:\nharvest date must be after plant date"

        self.head_details["errmsg"].configure(text=msg)

    def verify_all(
        self, doy: int, values: list[float], setv: Callable[[int, str], None]
    ) -> None:
        for item in self.required.values():
            if item.valid:
                values.insert(0, float(item.var.get()))  # type: ignore
            else:
                value = ""
                break
        else:
            # compute the result
            value = str(doy + sum(values))

        # all the outputs are the same
        for i in range(3):
            setv(i, value)


if __name__ == "__main__":
    root = tk.Tk()
    GIRFrame(root).pack(fill="both", expand=1)
    root.mainloop()
