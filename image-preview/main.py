import os
import sys
import tkinter as tk
from PIL import Image, ImageTk


class Window:
    def __init__(self, master):
        self.img = Image.open(get_resource_path("images/lion.jpg")).resize(
            (320, 300), Image.ANTIALIAS
        )
        self.img = ImageTk.PhotoImage(self.img)

        label = tk.Label(master, image=self.img)
        label.pack(expand=True, fill=tk.BOTH)


def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.title("Image Preview")
window = Window(root)
root.mainloop()
