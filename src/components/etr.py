from datetime import date
import tkinter as tk
from tkinter import ttk


class RefETFrame(ttk.Frame):
    def __init__(self, master: tk.Misc):
        super().__init__(master)

        # head
        head = ttk.Frame(self)
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

            ttk.Label(head, text=label).grid(
                column=column,
                row=row,
                columnspan=span,
                sticky="W"
            )
            ttk.Entry(head).grid(
                column=column + span,
                row=row,
                columnspan=span,
                sticky="E",
            )

            index += 2 * span
        head.grid(row=1, sticky="WE")

        # body
        body = ttk.Frame(self)
        inputs = {
            "Tmin (C)": "tmin",
            "Tmax (C)": "tmax",
            "Humidity (%)": "humidity",
            "Wind Speed (m/s)": "wind_speed",
            "Sun (hour)": "sun_hours",
        }
        outputs = {"ETr (mm/day)": lambda r: ""}
        loop = {
            "": lambda r: date(date.today().year, r, 1).strftime("%B"),
            **inputs,
            **outputs,
        }
        for row in range(13):
            for column, (key, value) in enumerate(loop.items()):
                if row == 0:
                    widget = ttk.Label(body, text=key)

                elif key in inputs:
                    widget = ttk.Entry(body)

                else:
                    widget = ttk.Label(body, text=value(row))

                widget.grid(row=row, column=column)
        body.grid(row=2)


if __name__ == "__main__":
    root = tk.Tk()
    RefETFrame(root).grid(padx=8, pady=8)
    root.mainloop()
