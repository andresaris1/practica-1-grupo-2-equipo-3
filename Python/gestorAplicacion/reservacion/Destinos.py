import os
from enum import Enum
from tkinter import *

class Destinos(Enum):
    SANTA_FE_DE_ANTIOQUIA = ("Santa Fe de Antioquia", 120000, "santafedeantioquia.png")
    COMUNA_13 = ("Comuna 13", 80000, "comuna13.png")
    JARDIN = ("Jardín", 90000, "jardin.png")
    PARQUE_ARVI = ("Parque Arví", 110000, "parquearvi.png")
    SANTA_ELENA = ("Santa Elena", 130000, "santaelena.png")
    PEÑOL_GUADELOUPE = ("Piedra Del Peñol", 200000, "penolguadeloupe.png")
    COMBO_COMPLETO =("Combo turistico completo", 720000, "")

    def __init__(self, nombre, valor, imagen):
        self.nombre = nombre
        self.valor = valor
        self.imagen = os.path.join(os.path.dirname(__file__), "img1", imagen)

    def get_nombre(self):
        return self.nombre

    def get_valor(self):
        return self.valor

def cargarDestinos():
    for i, destino in enumerate(Destinos):
        if destino != Destinos.COMBO_COMPLETO:
            imagen = PhotoImage(file=destino.imagen)
            boton = Button(frame2, command=lambda destino=destino: mostrarImagen(destino.nombre))
            boton.config(image=imagen)
            boton.image = imagen
            boton.place(relx=0.05, rely=0.35 + (i * 0.225), relwidth=0.25, relheight=0.3)

            nombre_label = Label(frame2, text=destino.nombre, font=("Arial", 12))
            nombre_label.place(relx=0.375, rely=0.375 + (i * 0.225), relwidth=0.25, relheight=0.075)

            valor_label = Label(frame2, text=destino.valor, font=("Arial", 12))
            valor_label.place(relx=0.375, rely=0.425 + (i * 0.225), relwidth=0.25, relheight=0.075)

    # Botón Combo Completo
    boton_combo = Button(frame2, text="COMBO COMPLETO", command=lambda: mostrarImagen(Destinos.COMBO_COMPLETO.nombre))
    boton_combo.place(relx=0.05, rely=0.35 + (len(Destinos) * 0.225), relwidth=0.25, relheight=0.3)
