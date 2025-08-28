import tkinter as tk
from tkinter import ttk
from datetime import date, timedelta
from typing import Callable, Literal

from .scrollable import Scrollable


class DataTable(Scrollable):
    """A scrollable table with headers, input rows, and multiple outputs."""

    def __init__(
        self,
        parent: tk.Misc,
        headers: list[str],
        callback: Callable[[int, list[float]], None],
        output_count: int = 1,
        orient: Literal["horizontal", "vertical"] = "vertical",
        blanks: int = 15,
        **kwargs,
    ):
        super().__init__(parent, orient=orient, **kwargs)
        assert output_count <= len(headers), (
            "output_count cannot exceed number of headers"
        )

        self.headers = headers
        self.callback = callback
        self.output_count = output_count
        self.blanks = blanks

        self.rows: list[dict] = []  # keep references to widgets per row
        self._build_header()

        for i in range(blanks):
            self._build_blank_row(-~i)

    def _build_header(self):
        """Create header row with labels."""
        # Date columns first
        base_headers = ["Day", "DOY", "Date"]

        # Split headers into input + output
        input_headers = self.headers[: -self.output_count]
        output_headers = self.headers[-self.output_count :]

        all_headers = base_headers + input_headers + output_headers

        for j, text in enumerate(all_headers):
            lbl = ttk.Label(self.frame, text=text, style="Heading.TLabel")
            lbl.grid(row=0, column=j, sticky="nsew", padx=2, pady=2)
            self.frame.grid_columnconfigure(j, weight=1)

    def populate(self, start: date, end: date):
        """Replace existing rows with new ones for given date range."""
        # clear old rows
        for widgets in self.rows:
            for w in widgets["widgets"]:
                w.destroy()
        self.rows.clear()

        # build new rows
        current = start
        i = 1
        while current <= end:
            self._build_row(i, current)
            i += 1
            current += timedelta(days=1)

        self._adjust_size()

    def _adjust_size(self) -> None:
        self.update_idletasks()
        dim = self.select("width", "height")
        self.configure({dim: getattr(self.frame, f"winfo_req{dim}")()})

    def _build_blank_row(self, row: int):
        """Build a blank row of the table."""
        widgets = []

        for column in range(3 + len(self.headers)):
            blank = ttk.Label(self.frame, text="-", anchor="center")
            blank.grid(row=row, column=column, sticky="news", padx=2, pady=2)
            widgets.append(blank)

        self.rows.append(
            {
                "widgets": widgets,
                "entries": [],
                "outputs": [],
                "doy": 0,
            }
        )

    def _build_row(self, row_index: int, current_date: date):
        """Build a single row of the table."""
        widgets = []

        # (a) date labels
        day_name = current_date.strftime("%a")
        doy = current_date.timetuple().tm_yday
        date_str = current_date.strftime("%Y-%m-%d")

        for column, text in enumerate((day_name, str(doy), date_str)):
            lbl = ttk.Label(self.frame, text=text)
            lbl.grid(row=row_index, column=column, sticky="news", padx=2, pady=2)
            widgets.append(lbl)

        # (b) numerical entries (all input columns)
        entries = []
        for j in range(len(self.headers) - self.output_count):
            e = ttk.Entry(self.frame, width=10)
            e.grid(row=row_index, column=3 + j, sticky="nsew", padx=2, pady=2)

            def validate(event, entry=e, row=row_index):
                val = entry.get().strip()
                if val == "":
                    entry.configure(foreground="black")
                    return
                try:
                    float(val)
                    entry.configure(foreground="black")
                except ValueError:
                    entry.configure(foreground="red")
                self._check_row_complete(row)

            e.bind("<FocusOut>", validate)
            e.bind("<Return>", self._on_enter)
            e.bind("<Tab>", self._on_enter)
            for event, (handler, steps) in dict(
                up=(self._move_vertically, -1),
                down=(self._move_vertically, 1),
                left=(self._move_horizontally, -1),
                right=(self._move_horizontally, 1),
            ).items():
                e.bind(
                    f"<{event.title()}>",
                    lambda e, r=row_index, c=j: handler(e, r, c, steps),
                )

            entries.append(e)
            widgets.append(e)

        # (c) output labels
        outputs = []
        for k in range(self.output_count):
            out_lbl = ttk.Label(self.frame, text="")
            out_lbl.grid(
                row=row_index,
                column=3 + len(self.headers) - self.output_count + k,
                sticky="nsew",
                padx=2,
                pady=2,
            )
            widgets.append(out_lbl)
            outputs.append(out_lbl)

        self.rows.append(
            {
                "widgets": widgets,
                "entries": entries,
                "outputs": outputs,
                "doy": doy,
            }
        )

    @staticmethod
    def _on_enter(event: tk.Event) -> Literal["break"]:
        event.widget.tk_focusNext().focus()  # type: ignore
        return "break"  # prevent default ding sound

    def _move_horizontally(
        self, _event: tk.Event, row: int, column: int, steps: int
    ) -> Literal["break"]:
        self.rows[~-row]["entries"][
            (column + steps) % (len(self.headers) - self.output_count)
        ].focus()
        return "break"  # prevent default ding sound

    def _move_vertically(
        self, _event: tk.Event, row: int, column: int, steps: int
    ) -> Literal["break"]:
        self.rows[(~-row + steps) % len(self.rows)]["entries"][column].focus()
        return "break"  # prevent default ding sound

    def _check_row_complete(self, row_index: int):
        """Check if all entries are valid, then call callback."""
        row = self.rows[row_index - 1]  # adjust for header row
        values = []
        for e in row["entries"]:
            val = e.get().strip()
            if val == "":
                return
            try:
                values.append(float(val))
            except ValueError:
                return
        # all valid
        self.callback(row["doy"], values)

    def set_output(self, row_index: int, col_index: int, text: str):
        """Set or clear output label in given row."""
        row = self.rows[row_index - 1]  # adjust for header
        if 0 <= col_index < len(row["outputs"]):
            row["outputs"][col_index].config(text=text)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("DataTable Example")
    root.grid_columnconfigure(0, weight=1)

    def on_row_complete(doy, values):
        print(f"Row complete for DOY {doy}: {values}")
        # Example: output the sum & average
        total = sum(values)
        avg = total / len(values)
        rel_index = doy - start.timetuple().tm_yday + 1
        table.set_output(rel_index, 0, f"{total:.2f}")
        table.set_output(rel_index, 1, f"{avg:.2f}")

    start = date(2025, 8, 25)
    end = date(2025, 8, 28)

    headers = ["Irrigation", "Fertilizer", "Rainfall", "Sum", "Avg"]

    table = DataTable(root, headers=headers, callback=on_row_complete, output_count=2)
    table.grid(row=0, column=0, sticky="nsew")
    table.scrollbar.grid(row=0, column=1, sticky="ns")

    root.update()
    table.configure(width=table.frame.winfo_reqwidth())
    root.bind(
        "<p>",
        lambda e: (
            table.populate(start, end),
            root.update(),
            table.configure(width=table.frame.winfo_reqwidth()),
        ),
    )

    root.mainloop()
