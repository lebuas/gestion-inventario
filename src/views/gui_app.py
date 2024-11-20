import tkinter as tk
from tkinter import ttk
from views.form_bodega import FormBodega
from views.form_negocio import FormNegocio
from views.form_proveedor import FormProveedor
from views.form_producto import FormProducto
from views.form_categoria import FormCategoria


class GuiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Inventarios")

        # Crear el Notebook (pestañas)
        self.tab_control = ttk.Notebook(self.root)

        # Crear las pestañas
        self.tab_negocio = ttk.Frame(self.tab_control)
        self.tab_producto = ttk.Frame(self.tab_control)
        self.tab_categoria = ttk.Frame(self.tab_control)
        self.tab_proveedor = ttk.Frame(self.tab_control)
        self.tab_bodega = ttk.Frame(self.tab_control)

        # Añadir las pestañas al control de pestañas
        self.tab_control.add(self.tab_negocio, text="Negocio")
        self.tab_control.add(self.tab_producto, text="Producto")
        self.tab_control.add(self.tab_categoria, text="Categoría")
        self.tab_control.add(self.tab_proveedor, text="Proveedor")
        self.tab_control.add(self.tab_bodega, text="Bodega")

        self.tab_control.pack(expand=1, fill="both")

        # Llenar las pestañas con botones
        self.create_negocio_tab()
        self.create_producto_tab()
        self.create_categoria_tab()
        self.create_proveedor_tab()
        self.create_bodega_tab()

    def create_negocio_tab(self):
        negocio = FormNegocio()

        # Crear botones en la pestaña Negocio
        tk.Button(self.tab_negocio, text="Registrar Producto",
                  command=negocio.registrar_producto).pack(pady=5)
        tk.Button(self.tab_negocio, text="Registrar Categoría",
                  command=negocio.registrar_categoria).pack(pady=5)
        tk.Button(self.tab_negocio, text="Registrar Proveedor",
                  command=negocio.registrar_proveedor).pack(pady=5)
        tk.Button(self.tab_negocio, text="Registrar Bodega",
                  command=negocio.registrar_bodega).pack(pady=5)
        tk.Button(self.tab_negocio, text="Consultar Información Producto",
                  command=negocio.consultar_informacion_producto).pack(pady=5)
        tk.Button(self.tab_negocio, text="Consultar Información Categoría",
                  command=negocio.consultar_informacion_categoria).pack(pady=5)
        tk.Button(self.tab_negocio, text="Consultar Información Proveedor",
                  command=negocio.consultar_informacion_proveedor).pack(pady=5)
        tk.Button(self.tab_negocio, text="Consultar Información Bodega",
                  command=negocio.consultar_informacion_bodega).pack(pady=5)
        tk.Button(self.tab_negocio, text="Consultar Producto en Bodega",
                  command=negocio.consultar_producto_en_bodega).pack(pady=5)
        tk.Button(self.tab_negocio, text="Calcular Valor Total Stock",
                  command=negocio.calcular_valor_total_stock).pack(pady=5)
        tk.Button(self.tab_negocio, text="Generar Informe Stock",
                  command=negocio.generar_informe_stock).pack(pady=5)

    def create_producto_tab(self):
        producto = FormProducto()
        # Crear botones en la pestaña Producto
        tk.Button(self.tab_producto, text="Aumentar Stock",
                  command=producto.aumentar_stock).pack(pady=5)
        tk.Button(self.tab_producto, text="Disminuir Stock",
                  command=producto.disminuir_stock).pack(pady=5)

    def create_categoria_tab(self):
        categoria = FormCategoria()
        # Crear botones en la pestaña Categoría
        tk.Button(self.tab_categoria, text="Agregar Producto a Categoría",
                  command=categoria.agregar_producto_categoria).pack(pady=5)
        tk.Button(self.tab_categoria, text="Eliminar Producto de Categoría",
                  command=categoria.eliminar_producto_categoria).pack(pady=5)

    def create_proveedor_tab(self):
        proveedor = FormProveedor()
        # Crear botones en la pestaña Proveedor
        tk.Button(self.tab_proveedor, text="Agregar Producto a Proveedor",
                  command=proveedor.agregar_producto_proveedor).pack(pady=5)
        tk.Button(self.tab_proveedor, text="Eliminar Producto de Proveedor",
                  command=proveedor.eliminar_producto_proveedor).pack(pady=5)

    def create_bodega_tab(self):
        bodega = FormBodega()
        # Crear botones en la pestaña Bodega
        tk.Button(self.tab_bodega, text="Agregar Producto a Bodega",
                  command=bodega.agregar_producto_bodega).pack(pady=5)
        tk.Button(self.tab_bodega, text="Retirar Producto de Bodega",
                  command=bodega.retirar_producto_bodega).pack(pady=5)
