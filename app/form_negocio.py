import tkinter as tk
from negocio_controller import NegocioController


class FormNegocio:
    def __init__(self):
        self.controller = NegocioController()

    def registrar_producto(self, frame):
        # Crear un frame para el formulario dentro del frame principal
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Etiquetas y entradas para los campos del formulario
        tk.Label(formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(formulario_frame)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Descripción:").grid(
            row=1, column=0, padx=10, pady=5)
        descripcion_entry = tk.Entry(formulario_frame)
        descripcion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Precio:").grid(
            row=2, column=0, padx=10, pady=5)
        precio_entry = tk.Entry(formulario_frame)
        precio_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Stock Inicial:").grid(
            row=3, column=0, padx=10, pady=5)
        stock_entry = tk.Entry(formulario_frame)
        stock_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Categoría:").grid(
            row=4, column=0, padx=10, pady=5)
        categoria_entry = tk.Entry(formulario_frame)
        categoria_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Proveedor:").grid(
            row=5, column=0, padx=10, pady=5)
        proveedor_entry = tk.Entry(formulario_frame)
        proveedor_entry.grid(row=5, column=1, padx=10, pady=5)

        # Botón para guardar
        tk.Button(formulario_frame, text="Guardar", command=lambda: self.controller.controller_registro_producto(
            [nombre_entry.get(),
             descripcion_entry.get(),
             precio_entry.get(),
             stock_entry.get(),
             categoria_entry.get(),
             proveedor_entry.get()], frame
        )).grid(row=6, column=0, columnspan=2, pady=10)

    def registrar_categoria(self, frame):
        # Usar el frame para crear el formulario dentro de la interfaz
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Etiquetas y entradas del formulario
        tk.Label(formulario_frame, text="Nombre de la Categoría:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(formulario_frame)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Descripción:").grid(
            row=1, column=0, padx=10, pady=5)
        descripcion_entry = tk.Entry(formulario_frame)
        descripcion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(formulario_frame, text="Guardar", command=lambda: self.controller.controller_registro_categoria(
                  [
                      nombre_entry.get(),
                      descripcion_entry.get()],
                  frame)
                  ).grid(row=2, column=0, columnspan=2, pady=10)

    def registrar_bodega(self, frame):
        # Usar el frame para crear el formulario dentro de la interfaz
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        tk.Label(formulario_frame, text="Nombre de la Bodega:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(formulario_frame)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Ubicación:").grid(
            row=1, column=0, padx=10, pady=5)
        ubicacion_entry = tk.Entry(formulario_frame)
        ubicacion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Capacidad Máxima:").grid(
            row=2, column=0, padx=10, pady=5)
        capacidad_entry = tk.Entry(formulario_frame)
        capacidad_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Productos Almacenados:").grid(
            row=3, column=0, padx=10, pady=5)
        lista_productos_entry = tk.Entry(formulario_frame)
        lista_productos_entry.grid(row=3, column=1, padx=10, pady=5)

        # Agregar una etiqueta para dar una instrucción al usuario
        tk.Label(formulario_frame, text="* Separe los productos con comas (,)",
                 fg="red", font=("Arial", 8)).grid(
            row=4, column=1, padx=10, pady=5, sticky="w")

        tk.Button(formulario_frame, text="Guardar", command=lambda: self.controller.controller_registro_bodega(
            [nombre_entry.get(),
             ubicacion_entry.get(),
             capacidad_entry.get(),
             lista_productos_entry.get()
             ],
            frame)
        ).grid(row=5, column=0, columnspan=2, pady=10)

    def registrar_proveedor(self, frame):
        # Crear el formulario en el frame proporcionado
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        tk.Label(formulario_frame, text="Nombre del Proveedor:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(formulario_frame)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Dirección:").grid(
            row=1, column=0, padx=10, pady=5)
        direccion_entry = tk.Entry(formulario_frame)
        direccion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Teléfono:").grid(
            row=2, column=0, padx=10, pady=5)
        telefono_entry = tk.Entry(formulario_frame)
        telefono_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Productos que suministra:").grid(
            row=3, column=0, padx=10, pady=5)
        productos_entry = tk.Entry(formulario_frame)
        productos_entry.grid(row=3, column=1, padx=10, pady=5)

        # Agregar una etiqueta para dar una instrucción al usuario
        tk.Label(formulario_frame, text="* Separe los productos con comas (,)",
                 fg="red", font=("Arial", 8)).grid(
            row=4, column=1, padx=10, pady=5, sticky="w")

        tk.Button(formulario_frame, text="Guardar", command=lambda: self.controller.controller_registro_proveedor(
            [
                nombre_entry.get(),
                direccion_entry.get(),
                telefono_entry.get(),
                productos_entry.get()
            ],
            frame)
        ).grid(row=5, column=0, columnspan=2, pady=10)

    def consultar_informacion_producto(self, frame):
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        tk.Label(formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(formulario_frame, text="Consultar", command=lambda: self.controller.controller_consulta_informacion_producto([producto_entry.get()], frame)).grid(
            row=1, column=0, columnspan=2, pady=10)

    def consultar_informacion_categoria(self, frame):
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        tk.Label(formulario_frame, text="Nombre de la Categoría:").grid(
            row=0, column=0, padx=10, pady=5)
        categoria_entry = tk.Entry(formulario_frame)
        categoria_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(formulario_frame, text="Consultar", command=lambda: self.controller.controller_consulta_informacion_categoria([categoria_entry.get()], frame)).grid(
            row=1, column=0, columnspan=2, pady=10)

    def consultar_informacion_proveedor(self, frame):
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        tk.Label(formulario_frame, text="Nombre del Proveedor:").grid(
            row=0, column=0, padx=10, pady=5)
        proveedor_entry = tk.Entry(formulario_frame)
        proveedor_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(formulario_frame, text="Consultar", command=lambda: self.controller.controller_consulta_informacion_proveedor([proveedor_entry.get()], frame)).grid(
            row=1, column=0, columnspan=2, pady=10)

    def consultar_informacion_bodega(self, frame):
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        tk.Label(formulario_frame, text="Nombre de la Bodega:").grid(
            row=0, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(formulario_frame)
        bodega_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(formulario_frame, text="Consultar", command=lambda: self.controller.controller_consulta_informacion_bodega([bodega_entry.get()], frame)).grid(
            row=1, column=0, columnspan=2, pady=10)

    def consultar_producto_en_bodega(self, frame):
        formulario_frame = tk.Frame(frame)
        formulario_frame.pack(expand=True, fill="both", padx=10, pady=10)

        tk.Label(formulario_frame, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(formulario_frame)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(formulario_frame, text="Bodega:").grid(
            row=1, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(formulario_frame)
        bodega_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(formulario_frame, text="Consultar", command=lambda: self.controller.controller_consulta_producto_en_bodega(
            [producto_entry.get(), bodega_entry.get()], frame)).grid(row=2, column=0, columnspan=2, pady=10)

    def calcular_valor_total_stock(self):
        self.controller.controller_calcular_total_stock()

    def generar_informe_stock(self):
        self.controller.controller_generar_informe_stock()
