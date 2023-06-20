import tkinter as tk

root = tk.Tk()

# Crear la barra de menú
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Crear un menú y agregarlo a la barra de menú
file_menu = tk.Menu(menu_bar, tearoff=0, font='Arial 19')
menu_bar.add_cascade(label='Archivo', menu=file_menu)

# Agregar elementos al menú
file_menu.add_command(label='Nuevo')
file_menu.add_command(label='Abrir')
file_menu.add_separator()
file_menu.add_command(label='Salir', command=root.quit)

root.mainloop()



