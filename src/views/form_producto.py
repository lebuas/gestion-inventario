from tkinter import messagebox, Toplevel, Label, Entry, Button


class FormProducto:
    def aumentar_stock(self):
        ventana = Toplevel()
        ventana.title("Aumentar Stock")

        Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = Entry(ventana)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(ventana, text="Cantidad a Aumentar:").grid(
            row=1, column=0, padx=10, pady=5)
        cantidad_entry = Entry(ventana)
        cantidad_entry.grid(row=1, column=1, padx=10, pady=5)

        Button(ventana, text="Aumentar", command=lambda: self.confirmar_aumento_stock(
            producto_entry.get(), cantidad_entry.get(), ventana)
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def confirmar_aumento_stock(self, producto, cantidad, ventana):
        if not producto or not cantidad.isdigit() or int(cantidad) <= 0:
            messagebox.showerror(
                "Error", "Debe ingresar un nombre de producto y una cantidad válida.")
            return

        # Simulación de aumento de stock
        messagebox.showinfo(
            "Éxito", f"Se aumentaron {cantidad} unidades del producto '{producto}' al stock.")
        ventana.destroy()

    def disminuir_stock(self):
        ventana = Toplevel()
        ventana.title("Disminuir Stock")

        Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = Entry(ventana)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(ventana, text="Cantidad a Disminuir:").grid(
            row=1, column=0, padx=10, pady=5)
        cantidad_entry = Entry(ventana)
        cantidad_entry.grid(row=1, column=1, padx=10, pady=5)

        Button(ventana, text="Disminuir", command=lambda: self.confirmar_disminucion_stock(
            producto_entry.get(), cantidad_entry.get(), ventana)
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def confirmar_disminucion_stock(self, producto, cantidad, ventana):
        if not producto or not cantidad.isdigit() or int(cantidad) <= 0:
            messagebox.showerror(
                "Error", "Debe ingresar un nombre de producto y una cantidad válida.")
            return

        # Simulación de disminución de stock
        messagebox.showinfo(
            "Éxito", f"Se disminuyeron {cantidad} unidades del producto '{producto}' del stock.")
        ventana.destroy()
