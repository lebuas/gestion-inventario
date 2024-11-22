import tkinter as tk
from categoria_controller import CategoriaController


class FormCategoria:
    def __init__(self):
        # Asegúrate de tener el controlador adecuado
        self.controller = CategoriaController()

    def agregar_producto_categoria(self, frame):
        # Crear un Frame para el formulario dentro del frame principal
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para el nombre de la categoría
        tk.Label(formulario_frame, text="Nombre de la Categoría:").grid(
            row=1, column=0, padx=10, pady=5)
        categoria_entry = tk.Entry(formulario_frame)
        categoria_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para agregar el producto a la categoría
        tk.Button(formulario_frame, text="Agregar", command=lambda: self.confirmar_agregar_producto_categoria(
            producto_entry.get(), categoria_entry.get())
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def eliminar_producto_categoria(self, frame):
        # Crear un Frame para el formulario dentro del frame principal
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para el nombre de la categoría
        tk.Label(formulario_frame, text="Nombre de la Categoría:").grid(
            row=1, column=0, padx=10, pady=5)
        categoria_entry = tk.Entry(formulario_frame)
        categoria_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para eliminar el producto de la categoría
        tk.Button(formulario_frame, text="Eliminar", command=lambda: self.confirmar_eliminar_producto_categoria(
            producto_entry.get(), categoria_entry.get())
        ).grid(row=2, column=0, columnspan=2, pady=10)
