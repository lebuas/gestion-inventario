from tkinter import messagebox
import tkinter as tk
from models.categoria import Categoria


class CategoriaController:
    def __init__(self):
        self.categoria = Categoria()
        self.formulario_frame = None
        self.get_categorias = self.categoria.get_datos()

    def debug(self):
        print(self.get_categorias)

    def __limpiar_formulario(self):
        """
        Limpiar todos los widgets dentro del frame,
        especialmente los campos Entry del formulario.
        """
        for widget in self.formulario_frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)

    def verificar_datos(self, datos):

        if '' in datos or None in datos:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        return True

    def controller_añadir_producto(self, producto, categoria, formulario):
        self.formulario_frame = formulario
        if not self.verificar_datos([categoria, producto]):
            return
        # self.debug()
        elif categoria not in self.get_categorias:
            messagebox.showinfo(
                "Aviso", f"La categoría '{categoria}' no se encuentra registrada")
            return

        if self.categoria.añadir_producto(categoria, producto):
            messagebox.showinfo(
                "Aviso", f"El producto '{producto}' se añadió a la categoría '{categoria}' correctamente")
        else:
            messagebox.showerror(
                "Error", f"El producto '{producto}'  ya está en la categoría '{categoria}' o ocurrió un problema")

        self.__limpiar_formulario()

    def controller_retirar_producto(self, producto, categoria, formulario):
        self.formulario_frame = formulario
        if not self.verificar_datos([categoria, producto]):
            return

        self.debug()
        if categoria not in self.get_categorias:
            messagebox.showinfo(
                "Aviso", f"La categoría '{categoria}' no se encuentra registrada")
            return

        if self.categoria.retirar_producto(categoria, producto):
            messagebox.showinfo(
                "Aviso", f"El producto '{producto}' se retiró de la categoría '{categoria}' correctamente")
        else:
            messagebox.showerror(
                "Error", f"El producto '{producto}' no está en la categoría '{categoria}' o ocurrió un problema")

        self.__limpiar_formulario()
