
import tkinter as tk
from tkinter import messagebox
from controller.negocio_controller import NegocioController


class FormNegocio:
    def __init__(self):
        self.controller = NegocioController()

    def registrar_producto(self):
        # Crear una nueva ventana para el formulario
        ventana = tk.Toplevel()
        ventana.title("Registrar Producto")

        # Etiquetas y entradas para los campos del formulario
        tk.Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Descripción:").grid(
            row=1, column=0, padx=10, pady=5)
        descripcion_entry = tk.Entry(ventana)
        descripcion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Precio:").grid(
            row=2, column=0, padx=10, pady=5)
        precio_entry = tk.Entry(ventana)
        precio_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Stock Inicial:").grid(
            row=3, column=0, padx=10, pady=5)
        stock_entry = tk.Entry(ventana)
        stock_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Categoría:").grid(
            row=4, column=0, padx=10, pady=5)
        categoria_entry = tk.Entry(ventana)
        categoria_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Proveedor:").grid(
            row=5, column=0, padx=10, pady=5)
        proveedor_entry = tk.Entry(ventana)
        proveedor_entry.grid(row=5, column=1, padx=10, pady=5)

        # Botón para guardar
        tk.Button(
            ventana,
            text="Guardar",
            command=lambda: self.controller.controller_registro_producto(
                [
                    nombre_entry.get(),
                    descripcion_entry.get(),
                    precio_entry.get(),
                    stock_entry.get(),
                    categoria_entry.get(),
                    proveedor_entry.get()
                ],
                ventana
            )
        ).grid(row=6, column=0, columnspan=2, pady=10)

    def registrar_categoria(self):
        ventana = tk.Toplevel()
        ventana.title("Registrar Categoría")

        tk.Label(ventana, text="Nombre de la Categoría:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Descripción:").grid(
            row=1, column=0, padx=10, pady=5)
        descripcion_entry = tk.Entry(ventana)
        descripcion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Guardar", command=lambda: self.controller.controller_registro_categoria(
                  [
                      nombre_entry.get(),
                      descripcion_entry.get()],
                  ventana)
                  ).grid(row=2, column=0, columnspan=2, pady=10)

    def registrar_bodega(self):
        ventana = tk.Toplevel()
        ventana.title("Registrar Bodega")

        tk.Label(ventana, text="Nombre de la Bodega:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Ubicación:").grid(
            row=1, column=0, padx=10, pady=5)
        ubicacion_entry = tk.Entry(ventana)
        ubicacion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Capacidad Máxima:").grid(
            row=2, column=0, padx=10, pady=5)
        capacidad_entry = tk.Entry(ventana)
        capacidad_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Productos Almacenados:").grid(
            row=3, column=0, padx=10, pady=5)
        lista_productos_entry = tk.Entry(ventana)
        lista_productos_entry.grid(row=3, column=1, padx=10, pady=5)

        # Agregar una etiqueta para dar una instrucción al usuario
        tk.Label(ventana, text="* Separe los productos con comas (,)",
                 fg="red", font=("Arial", 8)).grid(
            row=4, column=1, padx=10, pady=5, sticky="w")

        tk.Button(ventana, text="Guardar", command=lambda: self.controller.controller_registro_bodega(
            [nombre_entry.get(),
             ubicacion_entry.get(),
             capacidad_entry.get(),
             lista_productos_entry.get()
             ],
            ventana)
        ).grid(row=5, column=0, columnspan=2, pady=10)

    def registrar_proveedor(self):
        ventana = tk.Toplevel()
        ventana.title("Registrar Proveedor")

        tk.Label(ventana, text="Nombre del Proveedor:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Dirección:").grid(
            row=1, column=0, padx=10, pady=5)
        direccion_entry = tk.Entry(ventana)
        direccion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Teléfono:").grid(
            row=2, column=0, padx=10, pady=5)
        telefono_entry = tk.Entry(ventana)
        telefono_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Productos que suministra:").grid(
            row=3, column=0, padx=10, pady=5)
        productos_entry = tk.Entry(ventana)
        productos_entry.grid(row=3, column=1, padx=10, pady=5)

        # Agregar una etiqueta para dar una instrucción al usuario
        tk.Label(ventana, text="* Separe los productos con comas (,)",
                 fg="red", font=("Arial", 8)).grid(
            row=4, column=1, padx=10, pady=5, sticky="w")

        tk.Button(ventana, text="Guardar", command=lambda: self.controller.controller_registro_proveedor(
            [
                nombre_entry.get(),
                direccion_entry.get(),
                telefono_entry.get(),
                productos_entry.get()
            ],
            ventana)
        ).grid(row=5, column=0, columnspan=2, pady=10)

    def consultar_informacion_producto(self):
        ventana = tk.Toplevel()
        ventana.title("Consultar Información Producto")

        tk.Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(ventana)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Consultar", command=lambda: self.controller.controller_consulta_informacion_producto([producto_entry.get()], ventana)).grid(
            row=1, column=0, columnspan=2, pady=10)

    def mostrar_informacion_producto(self, producto):
        # Simular consulta
        if producto:  # Reemplazar con la lógica real
            messagebox.showinfo("Información del Producto",
                                f"Detalles del producto: {producto}")
        else:
            messagebox.showerror(
                "Error", "Debe ingresar un nombre de producto.")

    def consultar_informacion_categoria(self):
        ventana = tk.Toplevel()
        ventana.title("Consultar Información Categoría")

        tk.Label(ventana, text="Nombre de la Categoría:").grid(
            row=0, column=0, padx=10, pady=5)
        categoria_entry = tk.Entry(ventana)
        categoria_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Consultar", command=lambda: self.controller.controller_consulta_informacion_categoria([categoria_entry.get()], ventana)).grid(
            row=1, column=0, columnspan=2, pady=10)

    def consultar_informacion_proveedor(self):
        ventana = tk.Toplevel()
        ventana.title("Consultar Información Proveedor")

        tk.Label(ventana, text="Nombre del Proveedor:").grid(
            row=0, column=0, padx=10, pady=5)
        proveedor_entry = tk.Entry(ventana)
        proveedor_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Consultar", command=lambda: self.controller.controller_consulta_informacion_proveedor([proveedor_entry.get()], ventana)).grid(
            row=1, column=0, columnspan=2, pady=10)

    def consultar_informacion_bodega(self):
        ventana = tk.Toplevel()
        ventana.title("Consultar Información Bodega")

        tk.Label(ventana, text="Nombre de la Bodega:").grid(
            row=0, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(ventana)
        bodega_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Consultar", command=lambda: self.controller.controller_consulta_informacion_bodega([bodega_entry.get()], ventana)).grid(
            row=1, column=0, columnspan=2, pady=10)

    def consultar_producto_en_bodega(self):
        ventana = tk.Toplevel()
        ventana.title("Consultar Producto en Bodega")

        tk.Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(ventana)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Bodega:").grid(
            row=1, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(ventana)
        bodega_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Consultar", command=lambda: self.controller.controller_consulta_producto_en_bodega(
            [producto_entry.get(), bodega_entry.get()], ventana)).grid(row=2, column=0, columnspan=2, pady=10)

    def calcular_valor_total_stock(self):
        self.controller.controller_calcular_total_stock()

    def generar_informe_stock(self):
        self.controller.controller_generar_informe_stock()
