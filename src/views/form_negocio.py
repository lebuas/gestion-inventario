from tkinter import messagebox


class FormNegocio:

    def registrar_producto(self):
        messagebox.showinfo(
            "Registrar Producto", "Aquí iría el formulario para registrar un producto.")

    def registrar_categoria(self):
        messagebox.showinfo(
            "Registrar Categoría", "Aquí iría el formulario para registrar una categoría.")

    def registrar_proveedor(self):
        messagebox.showinfo(
            "Registrar Proveedor", "Aquí iría el formulario para registrar un proveedor.")

    def registrar_bodega(self):
        messagebox.showinfo(
            "Registrar Bodega", "Aquí iría el formulario para registrar una bodega.")

    def consultar_informacion_producto(self):
        messagebox.showinfo("Consultar Información Producto",
                            "Aquí iría el formulario para consultar un producto.")

    def consultar_informacion_categoria(self):
        messagebox.showinfo("Consultar Información Categoría",
                            "Aquí iría el formulario para consultar una categoría.")

    def consultar_informacion_proveedor(self):
        messagebox.showinfo("Consultar Información Proveedor",
                            "Aquí iría el formulario para consultar un proveedor.")

    def consultar_informacion_bodega(self):
        messagebox.showinfo("Consultar Información Bodega",
                            "Aquí iría el formulario para consultar una bodega.")

    def consultar_producto_en_bodega(self):
        messagebox.showinfo("Consultar Producto en Bodega",
                            "Aquí iría el formulario para consultar un producto en la bodega.")

    def calcular_valor_total_stock(self):
        messagebox.showinfo("Calcular Valor Total Stock",
                            "Aquí iría el formulario para calcular el valor total del stock.")

    def generar_informe_stock(self):
        messagebox.showinfo("Generar Informe Stock",
                            "Aquí iría el formulario para generar un informe de stock.")
