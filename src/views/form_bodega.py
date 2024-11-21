import tkinter as tk
from controller.bodega_controller import BodegaController


class FormBodega:
    def __init__(self):
        self.controller = BodegaController()

    def agregar_producto_bodega(self, frame):
        # Crear un Frame para el formulario dentro del frame principal
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para el nombre de la bodega
        tk.Label(formulario_frame, text="Bodega:").grid(
            row=1, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(formulario_frame)
        bodega_entry.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para la cantidad a agregar
        tk.Label(formulario_frame, text="Cantidad a agregar:").grid(
            row=2, column=0, padx=10, pady=5)
        cantidad_entry = tk.Entry(formulario_frame)
        cantidad_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botón para agregar el producto a la bodega
        tk.Button(formulario_frame, text="Agregar", command=lambda: self.guardar_producto_bodega(
            producto_entry.get(), bodega_entry.get(), cantidad_entry.get())
        ).grid(row=3, column=0, columnspan=2, pady=10)

    def retirar_producto_bodega(self, frame):
        # Crear un Frame para el formulario dentro del frame principal
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para el nombre de la bodega
        tk.Label(formulario_frame, text="Bodega:").grid(
            row=1, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(formulario_frame)
        bodega_entry.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para la cantidad a retirar
        tk.Label(formulario_frame, text="Cantidad a retirar:").grid(
            row=2, column=0, padx=10, pady=5)
        cantidad_entry = tk.Entry(formulario_frame)
        cantidad_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botón para retirar el producto de la bodega
        tk.Button(formulario_frame, text="Retirar", command=lambda: self.guardar_retiro_bodega(
            producto_entry.get(), bodega_entry.get(), cantidad_entry.get())
        ).grid(row=3, column=0, columnspan=2, pady=10)
