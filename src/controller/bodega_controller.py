from controller.lista_datos import LisDatos
from models.bodega import Bodega
from tkinter import messagebox
import tkinter as tk


class BodegaController(LisDatos):
    def __init__(self):
        super().__init__()
        self.bodega = Bodega(
            self.productos,
            self.categorias,
            self.proveedores,
            self.bodegas
        )
