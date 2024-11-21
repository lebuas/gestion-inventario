import tkinter as tk
from controller.proveedor_controller import ProveedorController


class FormProveedor:
    def __init__(self):
        self.controller = ProveedorController()

    def agregar_producto_proveedor(self, frame):
        # Crear un Frame para el formulario dentro del frame principal
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para el nombre del proveedor
        tk.Label(formulario_frame, text="Nombre del Proveedor:").grid(
            row=1, column=0, padx=10, pady=5)
        proveedor_entry = tk.Entry(formulario_frame)
        proveedor_entry.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para la cantidad
        tk.Label(formulario_frame, text="Cantidad:").grid(
            row=2, column=0, padx=10, pady=5)
        cantidad_entry = tk.Entry(formulario_frame)
        cantidad_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botón para agregar el producto al proveedor
        tk.Button(formulario_frame, text="Agregar", command=lambda: self.guardar_producto_proveedor(
            producto_entry.get(), proveedor_entry.get(), cantidad_entry.get())
        ).grid(row=3, column=0, columnspan=2, pady=10)

    def eliminar_producto_proveedor(self, frame):
        # Crear un Frame para el formulario dentro del frame principal
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para el nombre del proveedor
        tk.Label(formulario_frame, text="Nombre del Proveedor:").grid(
            row=1, column=0, padx=10, pady=5)
        proveedor_entry = tk.Entry(formulario_frame)
        proveedor_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para eliminar el producto del proveedor
        tk.Button(formulario_frame, text="Eliminar", command=lambda: self.confirmar_eliminar_producto_proveedor(
            producto_entry.get(), proveedor_entry.get())
        ).grid(row=2, column=0, columnspan=2, pady=10)
