import os
from enum import Enum
from tkinter import *

class Destinos(Enum):
    SANTA_FE_DE_ANTIOQUIA = ("Santa Fe de Antioquia", 120000, "santafedeantioquia.png","")
    COMUNA_13 = ("Comuna 13", 80000, "comuna13.png","")
    JARDIN = ("Jardín", 90000, "jardin.png","")
    PARQUE_ARVI = ("Parque Arví", 110000, "parquearvi.png","")
    SANTA_ELENA = ("Santa Elena", 130000, "santaelena.png","")
    PEÑOL_GUADELOUPE = ("Piedra Del Peñol", 200000, "piedradelpeñol.png","")
    COMBO_COMPLETO =("Combo turistico completo", 700000, "","")

    def __init__(self, nombre, valor, imagen, descripcion):
        self.nombre = nombre
        self.valor = valor
        self.imagen = imagen
        self.descripcion = descripcion

    def getNombre(self):
        return self.nombre

    def getValor(self):
        return self.valor

    def getImagen(self):
        return self.imagen
    
    def getDescripcion(self):
        return self.descripcion
