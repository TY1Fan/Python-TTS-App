import tkinter as tk

class Slider:
    def __init__(self):
        None

    def create_slider(self, parent, name, from_, to, resolution=0.05, initial=0.5):
        tk.Label(parent, text=name.capitalize()).pack()
        var = tk.DoubleVar(value=initial)
        slider = tk.Scale(
            parent,
            from_=from_,
            to=to,
            resolution=resolution,
            orient="horizontal",
            length=200,
            variable=var,
        )
        slider.pack(pady=5)
        return var