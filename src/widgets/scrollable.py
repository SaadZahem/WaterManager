import tkinter as tk
from tkinter import ttk
from typing import Literal

from .debounce import debounce


class Scrollable(tk.Canvas):
    """A scrollable container that adapts to its content."""

    def __init__(
        self,
        parent: tk.Misc,
        orient: Literal["horizontal", "vertical"] = "vertical",
        **kw,
    ) -> None:
        super().__init__(parent, borderwidth=0, **kw)

        self.orient = orient
        self.frame = tk.Frame(self)  # inner frame
        self._window = self.create_window((0, 0), window=self.frame, anchor="nw")

        # Scrollbar (but not placed yet)
        self.scrollbar = ttk.Scrollbar(parent, orient=orient, command=self.view)
        self.configure({self.select(*"yx") + "scrollcommand": self.scrollbar.set})

        # Bind resizing events.
        self.frame.bind("<Configure>", self._update_scrollregion)
        self.bind("<Configure>", self._resize_canvas)

        # Bind mouse wheel for scrolling on different os
        for event in {"MouseWheel", "Button-4", "Button-5"}:
            self.bind_all(f"<{event}>", self._on_mousewheel)

    def select[T](self, ifvertical: T, ifhorizontal: T) -> T:
        return ifhorizontal if self.orient == "horizontal" else ifvertical

    @property
    def view_scroll(self):
        return self.xview_scroll if self.orient == "horizontal" else self.yview_scroll

    @property
    def view(self):
        return self.xview if self.orient == "horizontal" else self.yview

    @debounce(1000)
    def _update_scrollregion(self, event=None):
        self.configure(scrollregion=self.bbox("all"))
        self._check_scrollbar()

    @debounce(50)
    def _resize_canvas(self, event=None):
        dim = self.select("width", "height")
        inner_size = getattr(self.frame, f"winfo_req{dim}")()
        self_size = getattr(self, f"winfo_{dim}")()

        if inner_size < self_size:
            self.itemconfig(self._window, {dim: self_size})
        else:
            self.configure({dim: inner_size})

        self._check_scrollbar()

    def _check_scrollbar(self, event=None):
        dim = self.select("height", "width")
        frame_size = getattr(self.frame, f"winfo_req{dim}")()
        canvas_size = getattr(self, f"winfo_{dim}")()
        need_scroll = frame_size > canvas_size

        if need_scroll != self.scrollbar.winfo_ismapped():
            self.scrollbar.grid() if need_scroll else self.scrollbar.grid_remove()

    def _on_mousewheel(self, event) -> None:
        if not self.scrollbar.winfo_ismapped():
            return
        if event.num == 4:  # Linux scroll up
            self.view_scroll(-1, "units")
        elif event.num == 5:  # Linux scroll down
            self.view_scroll(1, "units")
        else:  # Windows / macOS
            self.view_scroll(int(-1 * (event.delta / 120)), "units")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scrollable Table Example")
    root.geometry("600x400")

    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    # Make the container grid expand
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # Create a vertical scrollable container
    scroll = Scrollable(container, orient="vertical", background="white")
    scroll.grid(row=0, column=0, sticky="nsew")
    scroll.scrollbar.grid(row=0, column=1, sticky="ns")

    # --- Build a table inside scroll.frame ---
    rows, cols = 20, 6
    cells = {}

    for r in range(rows):
        for c in range(cols):
            if (r + c) % 2 == 0:  # Example: alternate Entry/Label
                var = tk.StringVar()
                e = tk.Entry(scroll.frame, textvariable=var, width=12)
                e.grid(row=r, column=c, sticky="nsew", padx=1, pady=1)

                # Example: update right-hand label when typing
                def update_label(*_, row=r, col=c, v=var):
                    target = (row, col + 1)
                    if target in cells and isinstance(cells[target], tk.Label):
                        cells[target].config(text=v.get())

                var.trace_add("write", update_label)
                cells[(r, c)] = var
            else:
                lbl = tk.Label(
                    scroll.frame, text=f"R{r},C{c}", width=12, relief="solid"
                )
                lbl.grid(row=r, column=c, sticky="nsew", padx=1, pady=1)
                cells[(r, c)] = lbl

            # Expand columns evenly
            scroll.frame.grid_columnconfigure(c, weight=1)
        scroll.frame.grid_rowconfigure(r, weight=1)

    root.mainloop()
