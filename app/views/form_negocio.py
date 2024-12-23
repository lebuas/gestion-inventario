import tkinter as tk
from controller.negocio_controller import NegocioController


class FormNegocio:
    def __init__(self):
        self.controller = NegocioController()
        self.formulario_frame = None

    def __crear_formulario(self, frame):
        # Crear un frame para el formulario dentro del frame principal
        self.formulario_frame = tk.Frame(frame)
        self.formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

    def __boton_cerrar(self, n_row):
        # Botón para cerrar
        tk.Button(self.formulario_frame, text="Cerrar", command=self.formulario_frame.destroy).grid(
            row=n_row, column=1, columnspan=2, pady=10)

    def registrar_producto(self, frame):
        # Crear el formulario
        self.__crear_formulario(frame)

        # Etiquetas y entradas para los campos del formulario
        tk.Label(self.formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(self.formulario_frame)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Descripción:").grid(
            row=1, column=0, padx=10, pady=5)
        descripcion_entry = tk.Entry(self.formulario_frame)
        descripcion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Precio:").grid(
            row=2, column=0, padx=10, pady=5)
        precio_entry = tk.Entry(self.formulario_frame)
        precio_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Stock Inicial:").grid(
            row=3, column=0, padx=10, pady=5)
        stock_entry = tk.Entry(self.formulario_frame)
        stock_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Categoría:").grid(
            row=4, column=0, padx=10, pady=5)
        categoria_entry = tk.Entry(self.formulario_frame)
        categoria_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Proveedor:").grid(
            row=5, column=0, padx=10, pady=5)
        proveedor_entry = tk.Entry(self.formulario_frame)
        proveedor_entry.grid(row=5, column=1, padx=10, pady=5)

        # Botón para guardar
        tk.Button(self.formulario_frame, text="Guardar", command=lambda: self.controller.controller_registro_producto(
            [nombre_entry.get(),
             descripcion_entry.get(),
             precio_entry.get(),
             stock_entry.get(),
             categoria_entry.get(),
             proveedor_entry.get()], self.formulario_frame
        )).grid(row=6, column=0, columnspan=2, pady=10)

        self.__boton_cerrar(6)

    def registrar_categoria(self, frame):
        # Crear el formulario
        self.__crear_formulario(frame)

        # Etiquetas y entradas del formulario
        tk.Label(self.formulario_frame, text="Nombre de la Categoría:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(self.formulario_frame)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Descripción:").grid(
            row=1, column=0, padx=10, pady=5)
        descripcion_entry = tk.Entry(self.formulario_frame)
        descripcion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(self.formulario_frame, text="Guardar", command=lambda: self.controller.controller_registro_categoria(
                  [
                      nombre_entry.get(),
                      descripcion_entry.get()], self.formulario_frame)
                  ).grid(row=2, column=0, columnspan=2, pady=10)
        self.__boton_cerrar(2)

    def registrar_bodega(self, frame):
        # Crear el formulario
        self.__crear_formulario(frame)

        tk.Label(self.formulario_frame, text="Nombre de la Bodega:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(self.formulario_frame)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Ubicación:").grid(
            row=1, column=0, padx=10, pady=5)
        ubicacion_entry = tk.Entry(self.formulario_frame)
        ubicacion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Capacidad Máxima:").grid(
            row=2, column=0, padx=10, pady=5)
        capacidad_entry = tk.Entry(self.formulario_frame)
        capacidad_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Productos Almacenados:").grid(
            row=3, column=0, padx=10, pady=5)
        lista_productos_entry = tk.Entry(self.formulario_frame)
        lista_productos_entry.grid(row=3, column=1, padx=10, pady=5)

        # Agregar una etiqueta para dar una instrucción al usuario
        tk.Label(self.formulario_frame, text="* Separe los productos con comas (,)",
                 fg="red", font=("Arial", 8)).grid(
            row=4, column=1, padx=10, pady=5, sticky="w")

        tk.Button(self.formulario_frame, text="Guardar", command=lambda: self.controller.controller_registro_bodega(
            [nombre_entry.get(),
             ubicacion_entry.get(),
             capacidad_entry.get(),
             lista_productos_entry.get()
             ], self.formulario_frame)
        ).grid(row=5, column=0, columnspan=2, pady=10)
        self.__boton_cerrar(5)

    def registrar_proveedor(self, frame):
        # Crear el formulario
        self.__crear_formulario(frame)

        tk.Label(self.formulario_frame, text="Nombre del Proveedor:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(self.formulario_frame)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Dirección:").grid(
            row=1, column=0, padx=10, pady=5)
        direccion_entry = tk.Entry(self.formulario_frame)
        direccion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Teléfono:").grid(
            row=2, column=0, padx=10, pady=5)
        telefono_entry = tk.Entry(self.formulario_frame)
        telefono_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Productos que suministra:").grid(
            row=3, column=0, padx=10, pady=5)
        productos_entry = tk.Entry(self.formulario_frame)
        productos_entry.grid(row=3, column=1, padx=10, pady=5)

        # Agregar una etiqueta para dar una instrucción al usuario
        tk.Label(self.formulario_frame, text="* Separe los productos con comas (,)",
                 fg="red", font=("Arial", 8)).grid(
            row=4, column=1, padx=10, pady=5, sticky="w")

        tk.Button(self.formulario_frame, text="Guardar", command=lambda: self.controller.controller_registro_proveedor(
            [
                nombre_entry.get(),
                direccion_entry.get(),
                telefono_entry.get(),
                productos_entry.get()
            ], self.formulario_frame)
        ).grid(row=5, column=0, columnspan=2, pady=10)
        self.__boton_cerrar(5)

    def consultar_informacion_producto(self, frame):
        # Crear el formulario
        self.__crear_formulario(frame)

        tk.Label(self.formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(self.formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(self.formulario_frame, text="Consultar", command=lambda: self.controller.controller_consulta_informacion_producto([producto_entry.get()], self.formulario_frame)).grid(
            row=1, column=0, columnspan=2, pady=10)
        self.__boton_cerrar(1)

    def consultar_informacion_categoria(self, frame):
        # Crear el formulario
        self.__crear_formulario(frame)

        tk.Label(self.formulario_frame, text="Nombre de la Categoría:").grid(
            row=0, column=0, padx=10, pady=5)
        categoria_entry = tk.Entry(self.formulario_frame)
        categoria_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(self.formulario_frame, text="Consultar", command=lambda: self.controller.controller_consulta_informacion_categoria([categoria_entry.get()], self.formulario_frame)).grid(
            row=1, column=0, columnspan=2, pady=10)
        self.__boton_cerrar(1)

    def consultar_informacion_proveedor(self, frame):
        # Crear el formulario
        self.__crear_formulario(frame)

        tk.Label(self.formulario_frame, text="Nombre del Proveedor:").grid(
            row=0, column=0, padx=10, pady=5)
        proveedor_entry = tk.Entry(self.formulario_frame)
        proveedor_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(self.formulario_frame, text="Consultar", command=lambda: self.controller.controller_consulta_informacion_proveedor([proveedor_entry.get()], self.formulario_frame)).grid(
            row=1, column=0, columnspan=2, pady=10)
        self.__boton_cerrar(1)

    def consultar_informacion_bodega(self, frame):
        # Crear el formulario
        self.__crear_formulario(frame)

        tk.Label(self.formulario_frame, text="Nombre de la Bodega:").grid(
            row=0, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(self.formulario_frame)
        bodega_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(self.formulario_frame, text="Consultar", command=lambda: self.controller.controller_consulta_informacion_bodega([bodega_entry.get()], self.formulario_frame)).grid(
            row=1, column=0, columnspan=2, pady=10)
        self.__boton_cerrar(1)

    def consultar_producto_en_bodega(self, frame):
        # Crear el formulario
        self.__crear_formulario(frame)

        tk.Label(self.formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(self.formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.formulario_frame, text="Bodega:").grid(
            row=1, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(self.formulario_frame)
        bodega_entry.grid(row=1, column=1, padx=10, pady=5)
        self.__boton_cerrar(2)

        tk.Button(self.formulario_frame, text="Consultar", command=lambda: self.controller.controller_consulta_producto_en_bodega(
            [producto_entry.get(), bodega_entry.get()], self.formulario_frame)).grid(row=2, column=0, columnspan=2, pady=10)

    def calcular_valor_total_stock(self):
        self.controller.controller_calcular_total_stock()

    def generar_informe_stock(self):
        self.controller.controller_generar_informe_stock()
