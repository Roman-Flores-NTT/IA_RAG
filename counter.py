import tkinter as tk

class ClickCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Clicks")

        self.count = 0

        self.label = tk.Label(root, text="0", font=("Helvetica", 48))
        self.label.pack()

        self.button = tk.Button(root, text="Haz Click Aquí", font=("Helvetica", 24), command=self.increment)
        self.button.pack()

    def increment(self):
        self.count += 1
        self.label.config(text=str(self.count))

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickCounterApp(root)
    root.mainloop()
