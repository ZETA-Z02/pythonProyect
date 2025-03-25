import tkinter as tk 

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Grafica")
        self.iconbitmap("")
        self.geometry("450x750+500+200")
        self.minsize(450, 750)
        self.maxsize(450,750)
        self.resizable(False, False)
        self.mainloop()
            
if __name__ == "__main__":
    Calculadora()