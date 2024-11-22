from tkinter import messagebox
import tkinter as tk
from models.bodega import Bodega


class BodegaController:
    def __init__(self):
        self.bodega = Bodega()
        self.formulario_frame = None
        self.get_bodegas = self.bodega.get_datos()

    def debug(self):
        print(self.get_bodegas)

    def __limpiar_formulario(self):
        """
        Limpiar todos los widgets dentro del frame,
        especialmente los campos Entry del formulario.
        """
        for widget in self.formulario_frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)

    def verificar_datos(self, datos):
        """
        Verificar si algún campo del formulario está vacío.
        """
        if '' in datos or None in datos:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        return True

    def controller_añadir_producto(self, producto, bodega, formulario):
        self.formulario_frame = formulario
        if not self.verificar_datos([bodega, producto]):
            return

        self.debug()
        if bodega not in self.get_bodegas:
            messagebox.showinfo(
                "Aviso", f"La bodega {bodega} no se encuentra registrada")
            return

        if self.bodega.añadir_producto(bodega, producto):
            messagebox.showinfo(
                "Aviso", f"El producto {producto} se añadió a la bodega {bodega} correctamente")
        else:
            messagebox.showerror(
                "Error", f"El producto {producto} ya está asociado a la bodega {bodega} o ocurrió un problema")

        self.__limpiar_formulario()

    def controller_retirar_producto(self, producto, bodega, formulario):
        self.formulario_frame = formulario
        if not self.verificar_datos([bodega, producto]):
            return

        self.debug()
        if bodega not in self.get_bodegas:
            messagebox.showinfo(
                "Aviso", f"La bodega {bodega} no se encuentra registrada")
            return

        if self.bodega.retirar_producto(bodega, producto):
            messagebox.showinfo(
                "Aviso", f"El producto {producto} se retiró de la bodega {bodega} correctamente")
        else:
            messagebox.showerror(
                "Error", f"El producto {producto} no está asociado a la bodega {bodega} o ocurrió un problema")

        self.__limpiar_formulario()
