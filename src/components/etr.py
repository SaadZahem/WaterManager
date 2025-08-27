from datetime import date
import tkinter as tk
from tkinter import ttk

from ..logic.etrcalc import calculate_reference_evapotranspiration as etr, j as doy


class RefETFrame(ttk.Frame):
    def __init__(self, master: tk.Misc):
        super().__init__(master)
        self.variables = {}
        self.widgets = {}
        self.mapping = {}
        self.outcome = {}

        from .styles import bold_font

        # head
        head = ttk.Frame(self, borderwidth="3")
        head.columnconfigure(tuple(range(12)), weight=1)
        dimensions = {
            "country": 3,
            "governorate": 3,
            "altitude": 2,
            "latitude": 2,
            "longitude": 2,
        }
        self.mapping.update(altitude="z", latitude="lat")
        index = 0
        for label, span in dimensions.items():
            row, column = divmod(index, 12)

            ttk.Label(head, text=label.title(), font=bold_font).grid(
                column=column,
                row=row,
                columnspan=span,
                sticky="E",
            )
            self.variables[label] = var = tk.StringVar()
            ttk.Entry(head, textvariable=var, justify="center").grid(
                column=column + span,
                row=row,
                columnspan=span,
                sticky="W",
            )
            var.trace_add("write", lambda *_: self.action())

            index += 2 * span

        head.grid(row=0, sticky="NEW")
        ttk.Separator(self, orient="horizontal").grid(row=1, pady=8, sticky="ew")

        # body
        body = ttk.Frame(self, borderwidth="3")
        inputs = {
            "Tmin (C)": "tmin",
            "Tmax (C)": "tmax",
            "Humidity (%)": "humidity",
            "Wind Speed (m/s)": "wind_speed",
            "Sun (hour)": "sun_hours",
        }
        outputs = {"ETr (mm/day)": ""}
        self.mapping.update({v: v for v in inputs.values()})
        loop = {
            "": lambda r: date(date.today().year, r, 1).strftime("%B"),
            **inputs,
            **outputs,
        }
        for row in range(13):
            for column, (key, value) in enumerate(loop.items()):
                if row == 0:
                    widget = ttk.Label(body, text=key, font=bold_font)

                elif key in inputs:
                    variable = tk.StringVar()
                    widget = ttk.Entry(
                        body,
                        justify="center",
                        validate="focusout",
                        validatecommand=(self.register(self.validate), "%P", "%W"),
                        textvariable=variable,
                    )
                    self.variables[value, row] = variable
                    self.widgets[str(widget)] = row

                elif column == 0:
                    widget = ttk.Label(
                        body, text=value(row), style="Const.TLabel", anchor="center"
                    )
                else:
                    variable = tk.StringVar()
                    widget = ttk.Label(
                        body,
                        text=value,
                        style="Output.TLabel",
                        textvariable=variable,
                        anchor="center",
                    )
                    self.outcome[row] = variable

                widget.grid(row=row, column=column, sticky="NEWS", ipadx=5)

        body.grid(row=2, sticky="SEW")

    def validate(self, newvalue: str, widgetname: str) -> bool:
        valid = self.validate_float(newvalue)

        if valid:
            self.action(self.widgets[widgetname])

        return valid

    @staticmethod
    def validate_float(value: str) -> bool:
        try:
            float(value)
        except ValueError:
            return False
        else:
            return True

    def action(self, row: int | None = None):
        if row is None:
            iterable = range(1, 13)
        else:
            iterable = (row,)

        for row in iterable:
            args = {}
            for key, param in self.mapping.items():
                if key in self.variables:
                    var = self.variables[key]
                    valid = self.validate_float(var.get())
                else:
                    var = self.variables[key, row]
                    valid = self.validate_float(var.get())

                if valid:
                    args[param] = float(var.get())
                else:
                    break
            else:
                set = self.outcome[row].set
                try:
                    value = etr(doy(row), **args)
                except ValueError:
                    set("")
                else:
                    set(format(value, ".4f"))


if __name__ == "__main__":
    root = tk.Tk()
    RefETFrame(root).grid(padx=8, pady=8, sticky="NEWS")
    root.mainloop()
