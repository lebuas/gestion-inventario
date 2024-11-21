from controller.lista_datos import LisDatos
from models.producto import Producto
from tkinter import messagebox
import tkinter as tk


class ProductoController(LisDatos):
    def __init__(self):
        super().__init__()
        self.nombre = ''
        self.cantida = 0
        self.producto = Producto(self.nombre, self.cantida, self.productos)

    def verificar_datos(self, datos):
        # Verificar si algún campo que viene del formulario esta vacion
        if '' in datos:
            # ventana.attributes("-topmost", False)
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        return True

    def controller_aumentar_stock(self, nombre, cantida, frame):
        self.nombre = nombre
        self.cantida = cantida
        if not self.verificar_datos([nombre, cantida]):
            return

        if nombre not in self.productos:
            messagebox.showinfo(
                "Aviso", f"El producto {nombre} no se encuentra registrado")

        try:
            cantida = float(cantida)
            if self.producto.aumentar_stock():
                messagebox.showinfo(
                    "Aviso", f"Al producto {nombre} se le añadiern {cantida} unidades correctamente")
            messagebox.showerror(
                "Error", "La cantida que se va a restar es mayor a lo que hay disponible en el stock")
            return

        except ValueError:
            messagebox.showerror("Error", "Cantida debe ser un numero")

    def controller_disminuir_stock(self):
        pass
