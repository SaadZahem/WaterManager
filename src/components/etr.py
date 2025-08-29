from datetime import date
import tkinter as tk
from tkinter import ttk

from ..logic.etrcalc import (
    calculate_reference_evapotranspiration as etr,
    calculate_day_of_year as doy,
)


class RefETFrame(ttk.Frame):
    def __init__(self, master: tk.Misc):
        """Creates the UI and links"""
        super().__init__(master)

        self.columnconfigure(0, weight=1)

        # links
        self.link_keyrow2inputvar = {}  # str -> head var, (str, row) -> body var
        "Maps key (str) to head StringVar and tuple[key, row (int)] to body StringVar."

        self.link_wname2row = {}  # widget name -> row
        "Maps widget internal name to row number."

        self.link_key2param = {}  # required key -> valid param
        "Maps key (str) to the parameter used by the function"

        self.link_row2outputvar = {}  # row -> output label var
        "Maps row (int) to StringVar of the output label"

        # styles
        #
        # note that this can't be moved to the top as the Tk widget must be
        # initialized before using fonts
        from .styles import bold_font

        # BEGIN head
        #
        # This has predefined number of columns (12)
        head = ttk.Frame(self)
        head["padding"] = (0, 8, 0, 0)  # padding top of 8

        # follow a 12 column layout as 12 is divisible by 1,2,3,4,6,12
        columns_count = 12
        head.columnconfigure(tuple(range(columns_count)), weight=1, pad=8)

        # foreach: key(label.text) value(columnspan) -> label & entry pair
        dimensions = {
            "country": 3,  # label span 3 & entry span 3
            "governorate": 3,  # completed the first row
            "altitude": 2,
            "latitude": 2,
            "longitude": 2,  # completed the second row
        }
        self.link_key2param.update(altitude="z", latitude="lat")

        # Generates label and entry pairs from a dictionary
        index = 0
        for label, span in dimensions.items():
            row, column = divmod(index, columns_count)
            self.link_keyrow2inputvar[label] = var = tk.StringVar()

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
        # END head

        # separator
        ttk.Separator(self, orient="horizontal").grid(row=1, pady=8, sticky="WE")

        # BEGIN body
        body = ttk.Frame(self)
        inputs = {
            "Tmin (C)": "tmin",
            "Tmax (C)": "tmax",
            "Humidity (%)": "humidity",
            "Wind Speed (m/s)": "wind_speed",
            "Sun (hour)": "sun_hours",
        }
        outputs = {"ETr (mm/day)": ""}
        self.link_key2param.update({v: v for v in inputs.values()})
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
                    self.link_keyrow2inputvar[value, row] = variable
                    self.link_wname2row[str(widget)] = row

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
                    self.link_row2outputvar[row] = variable

                widget.grid(row=row, column=column, sticky="NEWS", ipadx=5)

        body.grid(row=2, sticky="SEW")
        # END body

    def validate(self, newvalue: str, widgetname: str) -> bool:
        """Validate command for entries."""
        valid = self.validate_float(newvalue)
        row = self.link_wname2row[widgetname]
        entry = self.nametowidget(widgetname)

        if valid:
            self.action(row)
            entry.configure(style="TEntry")
        else:
            self.link_row2outputvar[row].set("")
            entry.configure(style="Invalid.TEntry")

        return valid

    @staticmethod
    def validate_float(value: str) -> bool:
        """Return true if the value is valid, that is, convertable to float or empty string."""
        try:
            float(value)
        except ValueError:
            return not value  # consider empty string valid
        else:
            return True

    def action(self, row: int | None = None):
        """Validate all rows in the table, calculate the result, and update the corresponding label."""

        if row is None:
            iterable = range(1, 13)
        else:
            iterable = (row,)

        for row in iterable:
            kwargs = {}
            value = ""  # output text if the operation fails

            for key, param in self.link_key2param.items():
                if key in self.link_keyrow2inputvar:
                    # head variable
                    var = self.link_keyrow2inputvar[key]
                else:
                    # body variable
                    var = self.link_keyrow2inputvar[key, row]

                try:
                    kwargs[param] = float(var.get())
                except ValueError:
                    break
            else:
                try:
                    result = etr(doy(row), **kwargs)
                    value = format(result, ".5f")
                except ValueError:
                    pass

            self.link_row2outputvar[row].set(value)


if __name__ == "__main__":
    root = tk.Tk()
    RefETFrame(root).pack(fill="both", expand=1)
    root.mainloop()
