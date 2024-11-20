from tkinter import messagebox
import tkinter as tk


class FormBodega:

    def agregar_producto_bodega(self):
        ventana = tk.Toplevel()
        ventana.title("Agregar Producto a Bodega")

        tk.Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(ventana)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Bodega:").grid(
            row=1, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(ventana)
        bodega_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Cantidad a agregar:").grid(
            row=2, column=0, padx=10, pady=5)
        cantidad_entry = tk.Entry(ventana)
        cantidad_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Agregar", command=lambda: self.guardar_producto_bodega(
            producto_entry.get(), bodega_entry.get(), cantidad_entry.get(), ventana)
        ).grid(row=3, column=0, columnspan=2, pady=10)

    def guardar_producto_bodega(self, producto, bodega, cantidad, ventana):
        if not producto or not bodega or not cantidad.isdigit():
            messagebox.showerror(
                "Error", "Debe completar todos los campos correctamente.")
            return

        # Simulación de guardado
        messagebox.showinfo(
            "Éxito", f"Se agregó {cantidad} unidades de '{producto}' a la bodega '{bodega}'.")
        ventana.destroy()

    def retirar_producto_bodega(self):
        ventana = tk.Toplevel()
        ventana.title("Retirar Producto de Bodega")

        tk.Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(ventana)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Bodega:").grid(
            row=1, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(ventana)
        bodega_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Cantidad a retirar:").grid(
            row=2, column=0, padx=10, pady=5)
        cantidad_entry = tk.Entry(ventana)
        cantidad_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Retirar", command=lambda: self.guardar_retiro_bodega(
            producto_entry.get(), bodega_entry.get(), cantidad_entry.get(), ventana)
        ).grid(row=3, column=0, columnspan=2, pady=10)

    def guardar_retiro_bodega(self, producto, bodega, cantidad, ventana):
        if not producto or not bodega or not cantidad.isdigit():
            messagebox.showerror(
                "Error", "Debe completar todos los campos correctamente.")
            return

        # Simulación de retiro
        messagebox.showinfo(
            "Éxito", f"Se retiraron {cantidad} unidades de '{producto}' de la bodega '{bodega}'.")
        ventana.destroy()
