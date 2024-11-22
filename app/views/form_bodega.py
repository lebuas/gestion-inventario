import tkinter as tk
from controller.bodega_controller import BodegaController


class FormBodega:
    def __init__(self):
        self.controller = BodegaController()
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

    def agregar_producto_bodega(self, frame):
        self.__crear_formulario(frame)

        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(self.formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(self.formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para el nombre de la bodega
        tk.Label(self.formulario_frame, text="Bodega:").grid(
            row=1, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(self.formulario_frame)
        bodega_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para agregar el producto a la bodega
        tk.Button(self.formulario_frame, text="Agregar", command=lambda: self.controller.controller_agregar_producto(
            producto_entry.get().lower(), bodega_entry.get().lower(), self.formulario_frame)
        ).grid(row=2, column=0, columnspan=2, pady=10)
        self.__boton_cerrar(2)

    def retirar_producto_bodega(self, frame):
        self.__crear_formulario(frame)

        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(self.formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(self.formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para el nombre de la bodega
        tk.Label(self.formulario_frame, text="Bodega:").grid(
            row=1, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(self.formulario_frame)
        bodega_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para retirar el producto de la bodega
        tk.Button(self.formulario_frame, text="Retirar", command=lambda: self.controller.controller_retirar_producto(
            producto_entry.get().lower(), bodega_entry.get().lower(), self.formulario_frame)
        ).grid(row=2, column=0, columnspan=2, pady=10)
        self.__boton_cerrar(2)
