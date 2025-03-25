import tkinter as tk

class Calculadora:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculadora Grafica")
        self.window.geometry("370x570+500+200")
        self.window.resizable(False, False)
        self.valor_a = 0
        self.valor_b = 0
        self.operacion = "sumar"
        self.resultado = 0
        self.main()
        self.window.mainloop()

    def main(self):
        self.pantalla = tk.Entry(self.window, bd=5, justify="right", font=("Arial", 24))
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            (".", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for texto, fila, columna in botones:
            color = "#4CAF50" if texto.isdigit() else "#FF9800"
            tk.Button(self.window, text=texto, width=6, height=3, bg=color, fg="white", font=("Arial", 18),
                      command=lambda t=texto: self.click_boton(t)).grid(row=fila, column=columna, sticky="nsew")

        tk.Button(self.window, text="C", width=6, height=3, bg="#F44336", fg="white", font=("Arial", 18),
                  command=self.borrar).grid(row=5, column=0, columnspan=4, sticky="nsew")

        for i in range(6):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i % 4, weight=1)

    def borrar(self):
        self.pantalla.delete(0, tk.END)

    def click_boton(self, valor):
        if valor.isdigit() or valor == ".":
            self.pantalla.insert(tk.END, valor)
        elif valor == "C":
            self.borrar()
        elif valor == "=":
            self.resultado_igual()
        else:
            self.operar(valor)

    def operar(self, simbolo):
        try:
            self.valor_a = float(self.pantalla.get())
            self.pantalla.delete(0, tk.END)
            self.operacion = simbolo
        except ValueError:
            self.borrar()

    def resultado_igual(self):
        try:
            self.valor_b = float(self.pantalla.get())
            self.pantalla.delete(0, tk.END)
            if self.operacion == "+":
                self.pantalla.insert(tk.END, self.valor_a + self.valor_b)
            elif self.operacion == "-":
                self.pantalla.insert(tk.END, self.valor_a - self.valor_b)
            elif self.operacion == "*":
                self.pantalla.insert(tk.END, self.valor_a * self.valor_b)
            elif self.operacion == "/":
                if self.valor_b != 0:
                    self.pantalla.insert(tk.END, self.valor_a / self.valor_b)
                else:
                    self.pantalla.insert(tk.END, "Error")
        except ValueError:
            self.pantalla.insert(tk.END, "Error")

if __name__ == "__main__":
    Calculadora()
