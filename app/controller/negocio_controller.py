from models.negocio import Negocio
from tkinter import messagebox, ttk
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
        """Genera el informe de stock y lo muestra en una ventana emergente"""
        # Crear ventana emergente para mostrar el informe
        ventana = tk.Toplevel()
        ventana.title("Informe de Stock")
        ventana.geometry("600x720")

        # Obtener los datos del informe
        informe_stock_total = self.negocio.genera_informes_stock()

        # Mostrar el informe de "Stock Total"
        tk.Label(ventana, text="Informe de Stock",
                 font=("Arial", 20, "bold")).pack(pady=10)

        # Crear Treeview para Stock Total
        tree = ttk.Treeview(ventana, columns=(
            "Total stock", "Unidades en total"), show="headings", height=1)  # Ajustar el alto
        tree.heading("Total stock", text="Productos Total stock")
        tree.heading("Unidades en total", text="Unidades en total")

        # Añadir datos
        datos = informe_stock_total['stock_total']
        tree.insert("", "end", values=(datos[0], datos[1]))

        tree.pack(padx=10, pady=10)

        # Crear Treeview para Stock por Categoría
        tk.Label(ventana, text="Stock por Categoría",
                 font=("Arial", 16, "bold")).pack(pady=10)

        tree_categorias = ttk.Treeview(ventana, columns=(
            "Categoría", "Productos Registrados", "Cantidad en stock"), show="headings", height=5)
        tree_categorias.heading("Categoría", text="Categoría")
        tree_categorias.heading("Productos Registrados",
                                text="Productos Registrados")
        tree_categorias.heading("Cantidad en stock", text="Cantidad en stock")

        # Añadir datos por categoría
        for categoria, datos in informe_stock_total["categorias"].items():
            tree_categorias.insert("", "end", values=(
                categoria, datos[0], datos[1]))

        tree_categorias.pack(padx=10, pady=10)

        # Crear Treeview para Stock por Proveedor
        tk.Label(ventana, text="Stock por Proveedor",
                 font=("Arial", 16, "bold")).pack(pady=10)

        tree_proveedores = ttk.Treeview(ventana, columns=(
            "Proveedor", "Productos Registrados", "Cantidad suministrada"), show="headings", height=5)
        tree_proveedores.heading("Proveedor", text="Proveedor")
        tree_proveedores.heading(
            "Productos Registrados", text="Productos Registrados")
        tree_proveedores.heading(
            "Cantidad suministrada", text="Cantidad suministrada")

        # Añadir datos por proveedor
        for proveedor, datos in informe_stock_total["proveedores"].items():
            tree_proveedores.insert("", "end", values=(
                proveedor, datos[0], datos[1]))

        tree_proveedores.pack(padx=10, pady=10)

        # Crear Treeview para Stock por Bodega
        tk.Label(ventana, text="Stock por Bodega",
                 font=("Arial", 16, "bold")).pack(pady=10)

        tree_bodegas = ttk.Treeview(ventana, columns=(
            "Bodega", "Productos Registrados", "Unidades disponibles"), show="headings", height=5)
        tree_bodegas.heading("Bodega", text="Bodega")
        tree_bodegas.heading("Productos Registrados",
                             text="Productos Registrados")
        tree_bodegas.heading("Unidades disponibles",
                             text="Unidades disponibles")

        # Añadir datos por bodega
        for bodega, datos in informe_stock_total["bodegas"].items():
            tree_bodegas.insert("", "end", values=(bodega, datos[0], datos[1]))

        tree_bodegas.pack(padx=10, pady=10)

        # Botón para cerrar la ventana con fuente más grande
        tk.Button(ventana, text="Cerrar", font=("Arial", 12),
                  command=ventana.destroy).pack(pady=10)
