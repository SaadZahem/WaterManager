import functools
import tkinter as tk
from typing import Any, Callable


def debounce(wait: int):
    """
    Tkinter-safe debounce decorator.
    Auto-detects root using the widget from the first call.

    Args:
        widget (tk.Widget): Any widget (usually root) to call `after()` on.
        wait (int): Delay in milliseconds before executing the function.
    """

    def decorator(fn: Callable):
        job = None
        top = None

        @functools.wraps(fn)
        def debounced(*args: Any, **kwargs: Any):
            nonlocal top, job

            # Parse arguments
            while top is None:
                if not args:
                    error = "No arguments were given"
                    break

                first = args[0]

                # Infer widget from first argument if it is a widget or an event
                if isinstance(first, tk.Widget):
                    top = first.winfo_toplevel()
                elif isinstance(first, tk.Event):
                    top = first.widget.winfo_toplevel()
                else:
                    error = f"First argument {first!r}."

                break

            # Report any error
            if top is None:
                errmsg = "Couldn't infer Tkinter root widget. "
                try:
                    raise ValueError(errmsg + error)  # type: ignore
                except NameError:
                    raise ValueError(errmsg) from None

            # Cancel previous job
            if job is not None:
                top.after_cancel(job)

            # Create a new one
            job = top.after(wait, lambda: fn(*args, **kwargs))

        return debounced

    return decorator
