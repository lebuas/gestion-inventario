import tkinter as tk
from controller.proveedor_controller import ProveedorController


class FormProveedor:
    def __init__(self):
        self.controller = ProveedorController()
        self.formulario_frame = None

    def __crear_formulario(self, frame):
        """Crea un formulario dentro del frame principal."""
        self.formulario_frame = tk.Frame(frame)
        self.formulario_frame.pack(
            expand=True, fill="both", padx=10, pady=10)

    def __boton_cerrar(self, n_row):
        """Crea un botón de cerrar que destruye el formulario."""
        tk.Button(self.formulario_frame, text="Cerrar", command=self.formulario_frame.destroy).grid(
            row=n_row, column=1, columnspan=2, pady=10)

    def agregar_producto_proveedor(self, frame):
        self.__crear_formulario(frame)

        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(self.formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(self.formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para el nombre del proveedor
        tk.Label(self.formulario_frame, text="Nombre del Proveedor:").grid(
            row=1, column=0, padx=10, pady=5)
        proveedor_entry = tk.Entry(self.formulario_frame)
        proveedor_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para agregar el producto al proveedor
        tk.Button(self.formulario_frame, text="Agregar", command=lambda: self.controller.controller_añadir_producto(
            producto_entry.get(), proveedor_entry.get(), self.formulario_frame)
        ).grid(row=2, column=0, columnspan=2, pady=10)
        self.__boton_cerrar(2)

    def eliminar_producto_proveedor(self, frame):
        self.__crear_formulario(frame)

        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(self.formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(self.formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para el nombre del proveedor
        tk.Label(self.formulario_frame, text="Nombre del Proveedor:").grid(
            row=1, column=0, padx=10, pady=5)
        proveedor_entry = tk.Entry(self.formulario_frame)
        proveedor_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para eliminar el producto del proveedor
        tk.Button(self.formulario_frame, text="Eliminar", command=lambda: self.controller.controller_retirar_producto(
            producto_entry.get(), proveedor_entry.get(), self.formulario_frame)
        ).grid(row=2, column=0, columnspan=2, pady=10)

        self.__boton_cerrar(2)
