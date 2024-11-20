from tkinter import messagebox, Toplevel, Label, Entry, Button


class FormProveedor:
    def agregar_producto_proveedor(self):
        ventana = Toplevel()
        ventana.title("Agregar Producto a Proveedor")

        Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = Entry(ventana)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(ventana, text="Nombre del Proveedor:").grid(
            row=1, column=0, padx=10, pady=5)
        proveedor_entry = Entry(ventana)
        proveedor_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(ventana, text="Cantidad:").grid(row=2, column=0, padx=10, pady=5)
        cantidad_entry = Entry(ventana)
        cantidad_entry.grid(row=2, column=1, padx=10, pady=5)

        Button(ventana, text="Agregar", command=lambda: self.guardar_producto_proveedor(
            producto_entry.get(), proveedor_entry.get(), cantidad_entry.get(), ventana)
        ).grid(row=3, column=0, columnspan=2, pady=10)

    def guardar_producto_proveedor(self, producto, proveedor, cantidad, ventana):
        if not producto or not proveedor or not cantidad.isdigit():
            messagebox.showerror(
                "Error", "Debe completar todos los campos correctamente.")
            return

        # Simulación de guardado
        messagebox.showinfo(
            "Éxito", f"Se agregó {cantidad} unidades del producto '{producto}' al proveedor '{proveedor}'.")
        ventana.destroy()

    def eliminar_producto_proveedor(self):
        ventana = Toplevel()
        ventana.title("Eliminar Producto de Proveedor")

        Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = Entry(ventana)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(ventana, text="Nombre del Proveedor:").grid(
            row=1, column=0, padx=10, pady=5)
        proveedor_entry = Entry(ventana)
        proveedor_entry.grid(row=1, column=1, padx=10, pady=5)

        Button(ventana, text="Eliminar", command=lambda: self.confirmar_eliminar_producto_proveedor(
            producto_entry.get(), proveedor_entry.get(), ventana)
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def confirmar_eliminar_producto_proveedor(self, producto, proveedor, ventana):
        if not producto or not proveedor:
            messagebox.showerror("Error", "Debe completar todos los campos.")
            return

        # Simulación de eliminación
        messagebox.showinfo(
            "Éxito", f"Se eliminó el producto '{producto}' del proveedor '{proveedor}'.")
        ventana.destroy()
