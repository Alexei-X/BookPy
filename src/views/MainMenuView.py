import tkinter as tk

class MainMenuView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BookPy")
        self.root.geometry("1280x720")
        self.root.resizable(width=False, height=False)
        self.root.mainloop()

    def stop(self):
        self.root.destroy()
