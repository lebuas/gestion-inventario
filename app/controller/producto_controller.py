from tkinter import messagebox
import tkinter as tk
from models.producto import Producto


class ProductoController:
    def __init__(self):
        self.producto = Producto()
        self.formulario_frame = None
        self.get_productos = self.producto.get_datos()

    # def debug(self):
    #     print(self.get_productos)

    def __limpiar_formulario(self):
        """
        Limpiar todos los widgets dentro del frame,
        especialmente los campos Entry del formulario.
        """
        for widget in self.formulario_frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)

    def verificar_datos(self, datos):
        # Verificar si algún campo que viene del formulario está vacío
        if '' in datos or None in datos:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        return True

    def controller_aumentar_stock(self, nombre, cantida, formulario):
        self.formulario_frame = formulario
        if not self.verificar_datos([nombre, cantida]):
            return
        # self.debug()
        elif nombre not in self.get_productos:
            messagebox.showinfo(
                "Aviso", f"El producto '{nombre}' no se encuentra registrado")
            return

        try:
            cantida = float(cantida)
            if self.producto.aumentar_stock(nombre, cantida):
                messagebox.showinfo(
                    "Aviso", f"Al producto '{nombre}' se añadieron '{cantida}' \
                    unidades correctamente")
            else:
                messagebox.showerror(
                    "Error", "La cantidad que se va a restar al producto \
                    es mayor a lo que hay disponible en el stock")

            self.__limpiar_formulario()

        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número")

    def controller_disminuir_stock(self, nombre, cantida, formulario):
        self.formulario_frame = formulario
        if not self.verificar_datos([nombre, cantida]):
            return
        # self.debug()
        elif nombre not in self.get_productos:
            messagebox.showinfo(
                "Aviso", f"El producto '{nombre}' no se encuentra registrado")
            return

        try:
            cantida = float(cantida)
            if self.producto.disminuir_stock(nombre, cantida):
                messagebox.showinfo(
                    "Aviso", f"Al producto '{nombre}' se le quitaron '{cantida}'\
                    unidades correctamente")
            else:
                messagebox.showerror(
                    "Error", "La cantidad que se va a restar\
                    es mayor al stock disponible")

            self.__limpiar_formulario()

        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número")
