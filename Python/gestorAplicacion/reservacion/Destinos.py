from enum import Enum

class Destinos(Enum):
    GUATAPE = ("Guatapé", 100000)
    SANTA_FE_DE_ANTIOQUIA = ("Santa Fe de Antioquia", 120000)
    COMUNA_13 = ("Comuna 13", 80000)
    JARDIN = ("Jardín", 90000)
    PARQUE_ARVI = ("Parque Arví", 110000)
    SANTA_ELENA = ("Santa Elena", 130000)
    PEÑOL_GUADELOUPE = ("Piedra Del Peñol", 150000)
    COMBO_COMPLETO =("Combo turistico completo", 750000)

    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

    def get_nombre(self):
        return self.nombre

    def get_valor(self):
        return self.valor
