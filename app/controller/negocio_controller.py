from models.negocio import Negocio
from tkinter import messagebox
import tkinter as tk


class NegocioController():
    def __init__(self):
        self.negocio = Negocio()
        self.formulario_frame = None
        self.bd = self.negocio.get_datos()

        self.get_productos = self.bd['productos']
        self.get_categorias = self.bd['categorias']
        self.get_proveedores = self.bd['proveedores']
        self.get_bodegas = self.bd['bodegas']

    # def debug(self):
    #     print(self.get_productos, "\n")
    #     print(self.get_categorias, "\n")
    #     print(self.get_proveedores, "\n")
    #     print(self.get_bodegas, "\n")

    def verificar_datos(self, datos):
        # Verificar si algún campo que viene del  esta vacion
        if '' in datos:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        return True

    def limpiar_formulario(self):
        """
        Limpiar todos los widgets dentro del frame,
        especialmente los campos Entry del formlario.
        """
        for widget in self.formulario_frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)

    def controller_registro_producto(self, datos, formulario):
        self.formulario_frame = formulario
        """
        controller_registro_producto, recibe una lista con los datos que
        recoge del del formularo. El orden es: datos = [
            nombre, descripcion, precio, stock, categoria,proveedor
            ]
        y se le envían al método registrar_producto desempaquetado como *datos.
        """

        if not self.verificar_datos(datos):
            return
        elif datos[0] in self.get_productos:
            messagebox.showinfo(
                "Aviso", f"El producto '{datos[0]}' ya se encuentra registrado")
            return
        elif datos[4] not in self.get_categorias:
            messagebox.showinfo(
                "Aviso", "Esa categoria no se encuentra registrada")
            return
        elif datos[5] not in self.get_proveedores:
            messagebox.showinfo(
                "Aviso", "El proveedor no se encuentra registrardo")
            return

        try:
            datos[3] = int(datos[3])
            datos[2] = float(datos[2])

            self.negocio.registrar_producto(*datos)

            messagebox.showinfo(
                "Éxito", f"Producto '{datos[0]}' registrado correctamente.")

            # self.debug()
            self.limpiar_formulario()

        except ValueError:
            messagebox.showerror(
                "Error", "Precio debe ser un número y stock un entero.")

    def controller_registro_categoria(self, datos, formulario):
        self.formulario_frame = formulario
        """
        Recibe una lista con los datos que recoge del .
        El orden es: datos = [nombre, descripcion]
        y se le envían al diccionario de categorias.
        """

        if not self.verificar_datos(datos):
            return
        elif datos[0] in self.get_categorias:
            messagebox.showinfo(
                "Aviso", f"la categoria '{datos[0]}'\
                ya se encuentra registrado")
            return

        try:

            self.negocio.registrar_categoria(*datos)
            messagebox.showinfo(
                "Éxito", f"Categoría '{datos[0]}'\
                fue registrada correctamente.")

            # self.debug()
            self.limpiar_formulario()

        except Exception as e:
            messagebox.showerror(
                "Error", f" Error al registrar la categoría: {e}")

    def controller_registro_proveedor(self, datos, formulario):

        self.formulario_frame = formulario
        """
        Recibe una lista con los datos que recoge del .
        El orden es: datos = [nombre, direccion, telefono,
        lista_productos que suministra
        ]
        y se le envían al diccionario de proveedores.
        """

        if not self.verificar_datos(datos):
            return

        elif datos[0] in self.get_proveedores:
            messagebox.showinfo(
                "Aviso", f"El proveedor '{datos[0]}'\
                ya se encuentra registrado.")
            return

        try:
            datos[2] = int(datos[2])

            self.negocio.registrar_proveedor(*datos)
            messagebox.showinfo(
                "Éxito", f"Proveedor '{datos[0]}'\
                fue registrado correctamente.")

            # self.debug()
            self.limpiar_formulario()

        except Exception as e:
            messagebox.showerror(
                "Error", f"El telefono tiene que ser un numero: {e}")

    def controller_registro_bodega(self, datos, formulario):
        self.formulario_frame = formulario
        """
        Recibe una lista con los datos para registrar una bodega:
        datos = [nombre, ubicacion, capacida, lista_producotos]
        """

        if not self.verificar_datos(datos):
            return
        elif datos[0] in self.get_bodegas:
            messagebox.showinfo(
                "Aviso", f"La bodega '{datos[0]}' ya se encuentra registrada.")
            return

        try:

            datos[2] = float(datos[2])
            self.negocio.registrar_bodega(*datos)

            messagebox.showinfo(
                "Éxito", f"Bodega '{datos[0]}' registrada correctamente.")

            self.debug()
            self.limpiar_formulario()

        except Exception as e:
            messagebox.showerror(
                "Error", f"La capacidad tiene que ser un numero {e}")

    def controller_consulta_informacion_producto(self, datos, formulario):
        self.formulario_frame = formulario

        if not self.verificar_datos(datos):
            return

        if datos[0] not in self.get_productos:
            messagebox.showinfo(
                "Aviso", f"El producto'{datos[0]}'\
                no se encuentra registrado.")
            return

        try:

            producto = self.negocio.consultar_informacion_producto(*datos)

            # Crear ventana para mostrar información del prodcuto
            ventana_info = tk.Toplevel()
            ventana_info.title(f"{datos[0]}")

            info = f"""
            INFORMACION SOBRE PRODUCTO:

            Nombre: {datos[0]}
            Descripcion: {producto['descripcion']}
            Categoria: {producto['categoria']}
            Proveedor: {producto['proveedor']}
            Precio: {producto['precio']}
            Stock: {producto['stock']}

            """
            tk.Label(ventana_info, text=info, justify="left",
                     font=("Arial", 10)).pack(padx=10, pady=10)

            # self.debug()
            self.limpiar_formulario()

        except Exception as e:
            messagebox.showerror(
                "Error", f" Error al consultar proveedor {e}")

    def controller_consulta_informacion_categoria(self, datos, formulario):
        self.formulario_frame = formulario

        if not self.verificar_datos(datos):
            return

        if datos[0] not in self.get_categorias:
            messagebox.showinfo(
                "Aviso", f" La categoria'{datos[0]}' \
                no se encuentra registrado.")
            return

        try:

            categoria = self.negocio.consultar_informacion_categoria(*datos)
            ventana_info = tk.Toplevel()
            ventana_info.title(f"{datos[0]}")

            info = f"""
            INFORMACION SOBRE CATEGORIA:

            Nombre: {datos[0]}
            Descripcion: {categoria['descripcion']}
            Productos: {', '.join(categoria['productos'])}
            """
            tk.Label(ventana_info, text=info, justify="left",
                     font=("Arial", 10)).pack(padx=10, pady=10)

            # self.debug()
            self.limpiar_formulario()

        except Exception as e:
            messagebox.showerror(
                "Error", f" Error al consultar categoria: {e}")

    def controller_consulta_informacion_proveedor(self, datos, formulario):
        self.formulario_frame = formulario

        if not self.verificar_datos(datos):
            return
        elif datos[0] not in self.get_proveedores:
            messagebox.showinfo(
                "Aviso", f"El proveedor'{datos[0]}'\
                no se encuentra registrado.")
            return

        try:

            proveedor = self.negocio.consultar_informacion_proveedor(*datos)
            ventana_info = tk.Toplevel()
            ventana_info.title(f"{datos[0]}")

            info = f"""
            INFORMACION SOBRE PROVEEDOR:

            Nombre: {datos[0]}
            Direccion: {proveedor['direccion']}
            Telefono: {proveedor['telefono']}
            Productos que suministra: {', '.join(proveedor['productos'])}
            """
            tk.Label(ventana_info, text=info, justify="left",
                     font=("Arial", 10)).pack(padx=10, pady=10)

            # self.debug()
            self.limpiar_formulario()

        except Exception as e:
            messagebox.showerror(
                "Error", f" Error al consultar proveedor: {e}")

    def controller_consulta_informacion_bodega(self, datos, formulario):
        self.formulario_frame = formulario

        if not self.verificar_datos(datos):
            return

        if datos[0] not in self.get_bodegas:
            messagebox.showinfo(
                "Aviso", f"La bodega '{datos[0]}' no se encuentra registrada.")
            return

        try:

            bodega = self.negocio.consultar_informacion_bodega(*datos)

            # Crear ventana para mostrar información de la bodega
            ventana_info = tk.Toplevel()
            ventana_info.title(f"{datos[0]}")

            info = f"""
            INFORMACION SOBRE BODEGA:

            Nombre: {datos[0]}
            Ubicación: {bodega['ubicacion']}
            Capacidad: {bodega['capacidad']}
            Productos almacenados: {', '.join(bodega['productos'])}
            """
            tk.Label(ventana_info, text=info, justify="left",
                     font=("Arial", 10)).pack(padx=10, pady=10)

            # self.debug()
            self.limpiar_formulario()

        except Exception as e:
            messagebox.showerror(
                "Error", f" Error al consultar bodega: {e}")

    def controller_calcular_total_stock(self):
        total_stock = self.negocio.calcular_valor_total_stock()
        messagebox.showinfo(
            'Aviso', f'El saldo total del  stock es de$: {total_stock}')

    def controller_generar_informe_stock(self):
        # Crear ventana emergente para mostrar el informe
        ventana = tk.Toplevel()
        ventana.title("Informe de Stock")
        ventana.geometry("600x430")

        informe_stock_total = self.negocio.genera_informes_stock()
        informe_texto = "Informe de Stock Total\n"
        datos = informe_stock_total['stock_total']
        informe_texto += f"Total stock: {datos[0]} Productos -- \
        Unidades en total: {datos[1]} \n\n"

        # Generar texto para Categorías
        informe_texto += "Stock por Categoría:\n"
        for categoria, datos in informe_stock_total["categorias"].items():
            informe_texto += f"- {categoria}:Productos Registrados {datos[0]} \
            Cantidas en stock {datos[1]} unidades en total\n"

        # Generar texto para Proveedores
        informe_texto += "\nStock por Proveedor:\n"
        for proveedor, datos in informe_stock_total["proveedores"].items():
            informe_texto += f"- {proveedor}: Productos Registrados:\
            {datos[0]} Cantidad que suministro: {datos[1]}\n"

        # Generar texto para Bodegas
        informe_texto += "\nStock por Bodega:\n"
        for bodega, datos in informe_stock_total["bodegas"].items():
            informe_texto += f"- {bodega}: Productos Registrados:\
            {datos[0]}, Unidades Disponibles: {datos[1]}\n"

        # Mostrar título del informe
        tk.Label(ventana, text="Informe de Stock",
                 font=("Arial", 16, "bold")).pack(pady=10)

        # Widget de texto para mostrar el informe
        text_widget = tk.Text(ventana, wrap="word",
                              height=20, width=70, font=("Arial", 10))
        text_widget.insert("1.0", informe_texto)
        # Hacer que el widget sea de solo lectura
        text_widget.config(state="disabled")
        text_widget.pack(padx=10, pady=10)

        tk.Button(ventana, text="Cerrar",
                  command=ventana.destroy).pack(pady=10)
