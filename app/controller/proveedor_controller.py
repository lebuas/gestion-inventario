
from tkinter import messagebox
import tkinter as tk
from models.proveedor import Proveedor


class ProveedorController:
    def __init__(self):
        self.proveedor = Proveedor()
        self.formulario_frame = None
        self.get_proveedores = self.proveedor.get_datos()

    def debug(self):
        print(self.get_proveedores)

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

    def controller_añadir_producto(self, producto, proveedor, formulario):
        self.formulario_frame = formulario
        if not self.verificar_datos([proveedor, producto]):
            return
        # self.debug()
        elif proveedor not in self.get_proveedores:
            messagebox.showinfo(
                "Aviso", f"El proveedor '{proveedor}' no se encuentra registrado")
            return
        elif self.proveedor.añadir_producto(proveedor, producto):
            messagebox.showinfo(
                "Aviso", f"El producto '{producto}' se añadió al proveedor '{proveedor}' correctamente")
        else:
            messagebox.showerror(
                "Error", f"El producto '{producto}' ya está asociado al proveedor '{proveedor}' o ocurrió un problema")

        self.__limpiar_formulario()

    def controller_retirar_producto(self, producto, proveedor, formulario):
        self.formulario_frame = formulario
        if not self.verificar_datos([proveedor, producto]):
            return
        # self.debug()
        elif proveedor not in self.get_proveedores:
            messagebox.showinfo(
                "Aviso", f"El proveedor '{proveedor}' no se encuentra registrado")
            return

        if self.proveedor.retirar_producto(proveedor, producto):
            messagebox.showinfo(
                "Aviso", f"El producto '{producto}' se retiró del proveedor '{proveedor}' correctamente")
        else:
            messagebox.showerror(
                "Error", f"El producto '{producto}' no está asociado al proveedor '{proveedor}' o ocurrió un problema")

        self.__limpiar_formulario()
