
from tkinter import messagebox, Toplevel, Label, Entry, Button


class FormCategoria:
    def agregar_producto_categoria(self):
        ventana = Toplevel()
        ventana.title("Agregar Producto a Categoría")

        Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = Entry(ventana)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(ventana, text="Nombre de la Categoría:").grid(
            row=1, column=0, padx=10, pady=5)
        categoria_entry = Entry(ventana)
        categoria_entry.grid(row=1, column=1, padx=10, pady=5)

        Button(ventana, text="Agregar", command=lambda: self.confirmar_agregar_producto_categoria(
            producto_entry.get(), categoria_entry.get(), ventana)
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def confirmar_agregar_producto_categoria(self, producto, categoria, ventana):
        if not producto or not categoria:
            messagebox.showerror(
                "Error", "Debe ingresar tanto el producto como la categoría.")
            return

        # Simulación de agregar el producto a la categoría
        messagebox.showinfo(
            "Éxito", f"El producto '{producto}' ha sido agregado a la categoría '{categoria}'.")
        ventana.destroy()

    def eliminar_producto_categoria(self):
        ventana = Toplevel()
        ventana.title("Eliminar Producto de Categoría")

        Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = Entry(ventana)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(ventana, text="Nombre de la Categoría:").grid(
            row=1, column=0, padx=10, pady=5)
        categoria_entry = Entry(ventana)
        categoria_entry.grid(row=1, column=1, padx=10, pady=5)

        Button(ventana, text="Eliminar", command=lambda: self.confirmar_eliminar_producto_categoria(
            producto_entry.get(), categoria_entry.get(), ventana)
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def confirmar_eliminar_producto_categoria(self, producto, categoria, ventana):
        if not producto or not categoria:
            messagebox.showerror(
                "Error", "Debe ingresar tanto el producto como la categoría.")
            return

        # Simulación de eliminar el producto de la categoría
        messagebox.showinfo(
            "Éxito", f"El producto '{producto}' ha sido eliminado de la categoría '{categoria}'.")
        ventana.destroy()
