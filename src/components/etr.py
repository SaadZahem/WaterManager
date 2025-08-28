from datetime import date
import tkinter as tk
from tkinter import ttk

from ..logic.etrcalc import calculate_reference_evapotranspiration as etr, j as doy


class RefETFrame(ttk.Frame):
    def __init__(self, master: tk.Misc):
        """Creates the UI and links"""
        super().__init__(master)

        self.columnconfigure(0, weight=1)

        # links
        self.variables = {}  # str -> head var, (str, row) -> body var
        self.widgets = {}  # widget name -> row
        self.argsmap = {}  # required key -> valid param
        self.outcome = {}  # row -> output label var

        # styles
        #
        # note that this can't be moved to the top as the Tk widget must be
        # initialized before using fonts
        from .styles import bold_font

        # head
        head = ttk.Frame(self)
        head.columnconfigure(tuple(range(12)), weight=1)
        dimensions = {
            "country": 3,
            "governorate": 3,
            "altitude": 2,
            "latitude": 2,
            "longitude": 2,
        }
        self.argsmap.update(altitude="z", latitude="lat")
        index = 0
        for label, span in dimensions.items():
            row, column = divmod(index, 12)
            self.variables[label] = var = tk.StringVar()

            ttk.Label(head, text=label.title(), font=bold_font).grid(
                column=column,
                row=row,
                columnspan=span,
                sticky="E",
            )
            ttk.Entry(head, textvariable=var, justify="center").grid(
                column=column + span,
                row=row,
                columnspan=span,
                sticky="W",
            )

            var.trace_add("write", lambda *_: self.action())
            index += 2 * span

        head.grid(row=0, sticky="NEW")

        # separator
        ttk.Separator(self, orient="horizontal").grid(row=1, pady=8, sticky="WE")

        # body
        body = ttk.Frame(self)
        inputs = {
            "Tmin (C)": "tmin",
            "Tmax (C)": "tmax",
            "Humidity (%)": "humidity",
            "Wind Speed (m/s)": "wind_speed",
            "Sun (hour)": "sun_hours",
        }
        outputs = {"ETr (mm/day)": ""}
        self.argsmap.update({v: v for v in inputs.values()})
        loop = {
            "": lambda r: date(date.today().year, r, 1).strftime("%B"),
            **inputs,
            **outputs,
        }
        for row in range(13):
            # body.rowconfigure(row, weight=1)
            for column, (key, value) in enumerate(loop.items()):
                body.columnconfigure(column, weight=1)

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
        """Validate command for entries."""
        valid = self.validate_float(newvalue)
        row = self.widgets[widgetname]

        if valid:
            self.action(row)
        else:
            self.outcome[row].set("")

        return valid

    @staticmethod
    def validate_float(value: str) -> bool:
        """Return true if the value is convertable to float."""
        try:
            float(value)
        except ValueError:
            return False
        else:
            return True

    def action(self, row: int | None = None):
        """Validate all rows in the table, calculate the result, and update the corresponding label."""

        if row is None:
            iterable = range(1, 13)
        else:
            iterable = (row,)

        for row in iterable:
            args = {}
            value = ""

            for key, param in self.argsmap.items():
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
                try:
                    result = etr(doy(row), **args)
                    value = format(result, ".5f")
                except ValueError:
                    pass

            self.outcome[row].set(value)


if __name__ == "__main__":
    root = tk.Tk()
    RefETFrame(root).pack(fill="both", expand=1)
    root.mainloop()
