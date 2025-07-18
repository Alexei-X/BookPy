import tkinter as tk

class MainMenuView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BookPy")
        self.root.geometry("1280x720")
        self.root.resizable(width=False, height=False)

    def stop(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

    def display_basic_elements(self):

        titleLabel = tk.Label(self.root, text="BookPy", font=("Arial bold", 24))
        titleLabel.pack(ipady=20)
