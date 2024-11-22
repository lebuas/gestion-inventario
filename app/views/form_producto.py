from controller.producto_controller import ProductoController
import tkinter as tk


class FormProducto:
    def __init__(self):
        self.controller = ProductoController()
        self.formulario_frame = None

    def __crear_formulario(self, frame):
        """Crea un formulario dentro del frame principal."""
        self.formulario_frame = tk.Frame(frame)
        self.formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

    def __boton_cerrar(self, n_row):
        """Crea un botón de cerrar que destruye el formulario."""
        tk.Button(self.formulario_frame, text="Cerrar", command=self.formulario_frame.destroy).grid(
            row=n_row, column=1, columnspan=2, pady=10)

    def aumentar_stock(self, frame):
        """Formulario para aumentar el stock de un producto."""
        self.__crear_formulario(frame)  # Crear formulario en el frame
        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(self.formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(self.formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para la cantidad a aumentar
        tk.Label(self.formulario_frame, text="Cantidad a Aumentar:").grid(
            row=1, column=0, padx=10, pady=5)
        cantidad_entry = tk.Entry(self.formulario_frame)
        cantidad_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para confirmar el aumento de stock
        tk.Button(self.formulario_frame, text="Aumentar", command=lambda: self.controller.controller_aumentar_stock(
            producto_entry.get(), cantidad_entry.get(), self.formulario_frame)
        ).grid(row=2, column=0, columnspan=2, pady=10)

        # Agregar el botón de cerrar
        self.__boton_cerrar(2)

    def disminuir_stock(self, frame):
        """Formulario para disminuir el stock de un producto."""
        self.__crear_formulario(frame)  # Crear formulario en el frame
        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(self.formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(self.formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para la cantidad a disminuir
        tk.Label(self.formulario_frame, text="Cantidad a Disminuir:").grid(
            row=1, column=0, padx=10, pady=5)
        cantidad_entry = tk.Entry(self.formulario_frame)
        cantidad_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para confirmar la disminución de stock
        tk.Button(self.formulario_frame, text="Disminuir", command=lambda: self.controller.controller_disminuir_stock(
            producto_entry.get(), cantidad_entry.get(), self.formulario_frame)
        ).grid(row=2, column=0, columnspan=2, pady=10)

        # Agregar el botón de cerrar
        self.__boton_cerrar(2)
