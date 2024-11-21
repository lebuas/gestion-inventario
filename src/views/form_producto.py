from controller.producto_controller import ProductoController
import tkinter as tk


class FormProducto:
    def __init__(self):
        self.controller = ProductoController()

    def aumentar_stock(self, frame):
        # Crear un Frame para el formulario dentro del frame principal
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para la cantidad a aumentar
        tk.Label(formulario_frame, text="Cantidad a Aumentar:").grid(
            row=1, column=0, padx=10, pady=5)
        cantidad_entry = tk.Entry(formulario_frame)
        cantidad_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para confirmar el aumento de stock
        tk.Button(formulario_frame, text="Aumentar", command=lambda: self.controller.controller_aumentar_stock(
            producto_entry.get(), cantidad_entry.get(), frame),
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def disminuir_stock(self, frame):
        # Crear un Frame para el formulario dentro del frame principal
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para la cantidad a disminuir
        tk.Label(formulario_frame, text="Cantidad a Disminuir:").grid(
            row=1, column=0, padx=10, pady=5)
        cantidad_entry = tk.Entry(formulario_frame)
        cantidad_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para confirmar la disminución de stock
        tk.Button(formulario_frame, text="Disminuir", command=lambda: self.controller.controller_disminuir_stock(
            producto_entry.get(), cantidad_entry.get(), frame)
        ).grid(row=2, column=0, columnspan=2, pady=10)
