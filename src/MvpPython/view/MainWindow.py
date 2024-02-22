import re
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Application:
    def __init__(self):
        self.root = tk.Tk()

        self.frame = tk.Frame(self.root)
        self.frame.grid()

        self.label = tk.Label(self.frame, text="Выберите изображение").grid(row=1, column=1)

        self.button = tk.Button(self.frame, text="выбрать", command=self.my_event_handler).grid(row=1, column=2)

        self.canvas = tk.Canvas(self.root, height=1000, width=1000)
        # self.c_image = self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        # self.canvas.grid(row=2, column=1)
        self.root.mainloop()

    def my_event_handler(self):
        self.image = Image.open("view/test.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=1)

app = Application()