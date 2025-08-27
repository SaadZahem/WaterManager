from datetime import date
import tkinter as tk
from tkinter import ttk


class RefETFrame(ttk.Frame):
    def __init__(self, master: tk.Misc):
        super().__init__(master)

        from .styles import bold_font

        self.columnconfigure(0, weight=3)
        self.rowconfigure(2, weight=3)

        # head
        head = ttk.Frame(self, borderwidth="3")
        head.columnconfigure(tuple(range(12)), weight=1)
        dimensions = {
            "Country": 3,
            "Governorate": 3,
            "Altitude": 2,
            "Latitude": 2,
            "Longitude": 2,
        }
        index = 0
        for label, span in dimensions.items():
            row, column = divmod(index, 12)

            ttk.Label(head, text=label, font=bold_font).grid(
                column=column,
                row=row,
                columnspan=span,
                sticky="E",
            )
            ttk.Entry(head).grid(
                column=column + span,
                row=row,
                columnspan=span,
                sticky="W",
            )

            index += 2 * span
        head.grid(row=0, sticky="NEW")
        ttk.Separator(self, orient="horizontal", style="Thick.TSeparator").grid(
            column=0, row=1, padx=10, pady=8
        )

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
        loop = {
            "": lambda r: date(date.today().year, r, 1).strftime("%B"),
            **inputs,
            **outputs,
        }
        for row in range(13):
            body.rowconfigure(row, weight=row)
            for column, (key, value) in enumerate(loop.items()):
                if row == 0:
                    widget = ttk.Label(body, text=key, font=bold_font)

                elif key in inputs:
                    widget = ttk.Entry(
                        body,
                        justify="center",
                    )

                elif column == 0:
                    widget = ttk.Label(
                        body, text=value(row), style="Const.TLabel", anchor="center"
                    )
                else:
                    widget = ttk.Label(body, text=value, style="Output.TLabel")

                widget.grid(row=row, column=column, sticky="NEWS", ipadx=5)
        body.grid(row=2, sticky="SEW")


if __name__ == "__main__":
    root = tk.Tk()
    RefETFrame(root).grid(padx=8, pady=8, sticky="NEWS")
    root.mainloop()
