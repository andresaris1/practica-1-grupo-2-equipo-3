import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dos Frames que ocupen la mitad")
        
        self.rowconfigure(0, weight=1)  # Ajustar filas al tamaño de la ventana
        self.columnconfigure(0, weight=1)  # Ajustar columnas al tamaño de la ventana
        
        # Frame 1
        frame1 = tk.Frame(self, bg="red")
        frame1.grid(row=0, column=0, sticky="nsew")  # Aplicar cambios al tamaño
        
        # Frame 2
        frame2 = tk.Frame(self, bg="blue")
        frame2.grid(row=0, column=1, sticky="nsew")  # Aplicar cambios al tamaño
        
        # Ajustar tamaño de las columnas al tamaño de la ventana
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

if __name__ == "__main__":
    window = Window()
    window.mainloop()
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dos Frames que ocupen la mitad")
        
        self.rowconfigure(0, weight=1)  # Ajustar filas al tamaño de la ventana
        self.columnconfigure(0, weight=1)  # Ajustar columnas al tamaño de la ventana
        
        # Frame 1
        frame1 = tk.Frame(self, bg="red")
        frame1.grid(row=0, column=0, sticky="nsew")  # Aplicar cambios al tamaño
        
        # Frame 2
        frame2 = tk.Frame(self, bg="blue")
        frame2.grid(row=0, column=1, sticky="nsew")  # Aplicar cambios al tamaño
        
        # Ajustar tamaño de las columnas al tamaño de la ventana
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

if __name__ == "__main__":
    window = Window()
    window.mainloop()

