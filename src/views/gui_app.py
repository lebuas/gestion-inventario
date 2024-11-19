import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class SistemaInventarioApp:
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
        # Crear botones en la pestaña Negocio
        tk.Button(self.tab_negocio, text="Registrar Producto",
                  command=self.registrar_producto).pack(pady=5)
        tk.Button(self.tab_negocio, text="Registrar Categoría",
                  command=self.registrar_categoria).pack(pady=5)
        tk.Button(self.tab_negocio, text="Registrar Proveedor",
                  command=self.registrar_proveedor).pack(pady=5)
        tk.Button(self.tab_negocio, text="Registrar Bodega",
                  command=self.registrar_bodega).pack(pady=5)
        tk.Button(self.tab_negocio, text="Consultar Información Producto",
                  command=self.consultar_informacion_producto).pack(pady=5)
        tk.Button(self.tab_negocio, text="Consultar Información Categoría",
                  command=self.consultar_informacion_categoria).pack(pady=5)
        tk.Button(self.tab_negocio, text="Consultar Información Proveedor",
                  command=self.consultar_informacion_proveedor).pack(pady=5)
        tk.Button(self.tab_negocio, text="Consultar Información Bodega",
                  command=self.consultar_informacion_bodega).pack(pady=5)
        tk.Button(self.tab_negocio, text="Consultar Producto en Bodega",
                  command=self.consultar_producto_en_bodega).pack(pady=5)
        tk.Button(self.tab_negocio, text="Calcular Valor Total Stock",
                  command=self.calcular_valor_total_stock).pack(pady=5)
        tk.Button(self.tab_negocio, text="Generar Informe Stock",
                  command=self.generar_informe_stock).pack(pady=5)

    def create_producto_tab(self):
        # Crear botones en la pestaña Producto
        tk.Button(self.tab_producto, text="Aumentar Stock",
                  command=self.aumentar_stock).pack(pady=5)
        tk.Button(self.tab_producto, text="Disminuir Stock",
                  command=self.disminuir_stock).pack(pady=5)

    def create_categoria_tab(self):
        # Crear botones en la pestaña Categoría
        tk.Button(self.tab_categoria, text="Agregar Producto a Categoría",
                  command=self.agregar_producto_categoria).pack(pady=5)
        tk.Button(self.tab_categoria, text="Eliminar Producto de Categoría",
                  command=self.eliminar_producto_categoria).pack(pady=5)

    def create_proveedor_tab(self):
        # Crear botones en la pestaña Proveedor
        tk.Button(self.tab_proveedor, text="Agregar Producto a Proveedor",
                  command=self.agregar_producto_proveedor).pack(pady=5)
        tk.Button(self.tab_proveedor, text="Eliminar Producto de Proveedor",
                  command=self.eliminar_producto_proveedor).pack(pady=5)

    def create_bodega_tab(self):
        # Crear botones en la pestaña Bodega
        tk.Button(self.tab_bodega, text="Agregar Producto a Bodega",
                  command=self.agregar_producto_bodega).pack(pady=5)
        tk.Button(self.tab_bodega, text="Retirar Producto de Bodega",
                  command=self.retirar_producto_bodega).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaInventarioApp(root)
    root.mainloop()
