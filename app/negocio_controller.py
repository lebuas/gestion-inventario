from lista_datos import LisDatos
from negocio import Negocio
from tkinter import messagebox
import tkinter as tk


class NegocioController(LisDatos):
    def __init__(self):
        super().__init__()
        self.negocio = Negocio(
            self.productos,
            self.categorias,
            self.proveedores,
            self.bodegas
        )

    def debug(self):
        print(self.productos, "\n")
        print(self.categorias, "\n")
        print(self.proveedores, "\n")
        print(self.bodegas, "\n")

    def verificar_datos(self, datos):
        # Verificar si algún campo que viene del formulario esta vacion
        if '' in datos:
            # ventana.attributes("-topmost", False)
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        return True

    def limpiar_formulario(self, frame):
        """
        Limpiar todos los widgets dentro del frame, especialmente los campos Entry.
        """
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Entry):  # Si el widget es un campo de texto (Entry)
                widget.delete(0, tk.END)  # Limpiar el contenido

    def controller_registro_producto(self, datos, ventana):
        """
        controller_registro_producto, recibe una lista con los datos que
        recoge del formulario.
        El orden es: datos = [nombre, descripcion, precio, stock, categoria,proveedor]
        y se le envían al método registrar_producto desempaquetado como *datos.
        """

        if not self.verificar_datos(datos):
            return  # Si los datos no son válidos, no continuar con el registro

        # verificar si el producto se encuentra registrado
        if datos[0] in self.productos:
            messagebox.showinfo(
                "Aviso", f"el producto{datos[0]} ya se encuentra registrado")
            return

        # verificar si la categoria se encuentra registrada
        if datos[4] not in self.categorias:
            messagebox.showinfo(
                "Aviso", "Esa categoria no esta registrada, registrela antes de agregar el producto")
            return

        if datos[5] not in self.proveedores:
            messagebox.showinfo(
                "Aviso", "El proveedor no se encuentra registrardo, registrelo")
            return

        try:
            # Modificar los datos si es necesario antes de enviarlos
            datos[3] = int(datos[3])  # Convertir stock a entero (índice 3)
            datos[2] = float(datos[2])  # Convertir precio a float (índice 2)

            # Llamar al método de registrar producto con los datos modificados
            self.negocio.registrar_producto(*datos)

            # Mostrar mensaje de éxito
            messagebox.showinfo(
                "Éxito", f"Producto '{datos[0]}' registrado correctamente.")

            # Cerrar la ventana del formulario solo si el registro es exitoso
            self.debug()

            self.limpiar_formulario(ventana)

        except ValueError:
            # Captura el error si no se puede convertir precio o stock
            messagebox.showerror(
                "Error", "Precio debe ser un número y stock un entero.")

    def controller_registro_categoria(self, datos, ventana):
        """
        Recibe una lista con los datos que recoge del formulario.
        El orden es: datos = [nombre, descripcion]
        y se le envían al diccionario de categorias.
        """

        if not self.verificar_datos(datos):
            return  # Si los datos no son válidos, no continuar con el registro

        if datos[0] in self.categorias:  # verificar si el producto
            messagebox.showinfo(
                "Aviso", f"la categoria {datos[0]} ya se encuentra registrado")
            return

        try:

            self.negocio.registrar_categoria(*datos)

            # Mostrar mensaje de éxito
            messagebox.showinfo(
                "Éxito", f"Categoría '{datos[0]}' fue registrada correctamente.")

            self.debug()
            # Cerrar la ventana del formulario solo si el registro es exitoso
            # ventana.destroy()

        except Exception as e:
            # Captura cualquier otro error general
            messagebox.showerror(
                "Error", f" Error al registrar la categoría: {e}")

    def controller_registro_proveedor(self, datos, ventana):
        """
        Recibe una lista con los datos que recoge del formulario.
        El orden es: datos = [nombre, direccion, telefono, lista_productos que suministra]
        y se le envían al diccionario de proveedores.
        """

        # Verificar si hay datos vacíos
        if not self.verificar_datos(datos):
            return  # Si los datos no son válidos, no continuar con el registro

        # Verificar si el proveedor ya está registrado
        if datos[0] in self.proveedores:
            messagebox.showinfo(
                "Aviso", f"El proveedor '{datos[0]}' ya se encuentra registrado.")
            return

        try:
            # Registrar el proveedor utilizando el método del modelo
            datos[2] = int(datos[2])
            self.negocio.registrar_proveedor(*datos)

            # Mostrar mensaje de éxito

            messagebox.showinfo(
                "Éxito", f"Proveedor '{datos[0]}' fue registrado correctamente.")

            # Debug para confirmar los cambios
            self.debug()

            # Cerrar la ventana del formulario solo si el registro es exitoso
            ventana.destroy()

        except Exception as e:
            # Captura cualquier error general durante el proceso
            messagebox.showerror(
                "Error", f"El telefono tiene que ser un numero: {e}")

    def controller_registro_bodega(self, datos, ventana):
        """
        Recibe una lista con los datos para registrar una bodega:
        datos = [nombre, ubicacion, capacida, lista_producotos]
        """

        if not self.verificar_datos(datos):
            return  # Si los datos no son válidos, no continuar con el registro

        if datos[0] in self.bodegas:  # Verificar si la bodega ya está registrada
            messagebox.showinfo(
                "Aviso", f"La bodega '{datos[0]}' ya se encuentra registrada.")
            return

        try:

            datos[2] = float(datos[2])
            self.negocio.registrar_bodega(*datos)

            # Mostrar mensaje de éxito
            messagebox.showinfo(
                "Éxito", f"Bodega '{datos[0]}' registrada correctamente.")

            self.debug()

            # Cerrar la ventana del formulario solo si el registro es exitoso
            ventana.destroy()

        except Exception as e:
            # Captura cualquier otro error general
            messagebox.showerror(
                "Error", f"La capacidad tiene que ser un numero {e}")

    def controller_consulta_informacion_producto(self, datos, ventana):

        if not self.verificar_datos(datos):
            return  # Si los datos no son válidos, no continuar con el registro

        if datos[0] not in self.productos:  # Verificar si  hay un producto con ese nombre
            messagebox.showinfo(
                "Aviso", f"El producto'{datos[0]}' no se encuentra registrado.")
            return

        try:

            producto = self.negocio.consultar_informacion_producto(*datos)

            # Crear ventana para mostrar información del prodcuto
            ventana_info = tk.Toplevel()
            ventana_info.title(f"{datos[0]}")

            # Mostrar información en la ventana
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

            self.debug()

            # Cerrar la ventana del formulario solo si el registro es exitoso
            ventana.destroy()

        except Exception as e:
            # Captura cualquier otro error general
            messagebox.showerror(
                "Error", f" Error al consultar proveedor {e}")

    def controller_consulta_informacion_categoria(self, datos, ventana):

        if not self.verificar_datos(datos):
            return  # Si los datos no son válidos, no continuar con el registro

        if datos[0] not in self.categorias:  # Verificar si  hay un categoria con ese nombre
            messagebox.showinfo(
                "Aviso", f" La categoria'{datos[0]}' no se encuentra registrado.")
            return

        try:

            categoria = self.negocio.consultar_informacion_categoria(*datos)

            # Crear ventana para mostrar información del proveedor
            ventana_info = tk.Toplevel()
            ventana_info.title(f"{datos[0]}")

            # Mostrar información en la ventana
            info = f"""
            INFORMACION SOBRE CATEGORIA:

            Nombre: {datos[0]}
            Descripcion: {categoria['descripcion']}
            Productos: {', '.join(categoria['productos'])}
            """
            tk.Label(ventana_info, text=info, justify="left",
                     font=("Arial", 10)).pack(padx=10, pady=10)

            self.debug()

            # Cerrar la ventana del formulario solo si el registro es exitoso
            ventana.destroy()

        except Exception as e:
            # Captura cualquier otro error general
            messagebox.showerror(
                "Error", f" Error al consultar categoria {e}")

    def controller_consulta_informacion_proveedor(self, datos, ventana):

        if not self.verificar_datos(datos):
            return  # Si los datos no son válidos, no continuar con el registro

        if datos[0] not in self.proveedores:  # Verificar si  hay un proveedor con ese nombre
            messagebox.showinfo(
                "Aviso", f"El proveedor'{datos[0]}' no se encuentra registrado.")
            return

        try:

            proveedor = self.negocio.consultar_informacion_proveedor(*datos)

            # Crear ventana para mostrar información del proveedor
            ventana_info = tk.Toplevel()
            ventana_info.title(f"{datos[0]}")

            # Mostrar información en la ventana
            info = f"""
            INFORMACION SOBRE PROVEEDOR:

            Nombre: {datos[0]}
            Dirección: {proveedor['direccion']}
            Teléfono: {proveedor['telefono']}
            Productos: {', '.join(proveedor['productos'])}
            """
            tk.Label(ventana_info, text=info, justify="left",
                     font=("Arial", 10)).pack(padx=10, pady=10)

            self.debug()

            # Cerrar la ventana del formulario solo si el registro es exitoso
            ventana.destroy()

        except Exception as e:
            # Captura cualquier otro error general
            messagebox.showerror(
                "Error", f" Error al consultar proveedor {e}")

    def controller_consulta_informacion_bodega(self, datos, ventana):

        if not self.verificar_datos(datos):
            return  # Si los datos no son válidos, no continuar con el registro

        if datos[0] not in self.bodegas:  # Verificar si  hay un bodegas con ese nombre
            messagebox.showinfo(
                "Aviso", f"La bodega'{datos[0]}' no se encuentra registrado.")
            return

        try:

            bodega = self.negocio.consultar_informacion_bodega(*datos)

            # Crear ventana para mostrar información del proveedor
            ventana_info = tk.Toplevel()
            ventana_info.title(f"{datos[0]}")

            # Mostrar información en la ventana
            info = f"""
            INFORMACION SOBRE BODEGA:

            Nombre: {datos[0]}
            Ubicacion: {bodega['ubicacion']}
            Capacidad: {bodega['capacidad']}
            Productos: {', '.join(bodega['productos'])}
            """
            tk.Label(ventana_info, text=info, justify="left",
                     font=("Arial", 10)).pack(padx=10, pady=10)

            self.debug()

            # Cerrar la ventana del formulario solo si el registro es exitoso
            ventana.destroy()

        except Exception as e:
            # Captura cualquier otro error general
            messagebox.showerror(
                "Error", f" Error al consultar bodega {e}")

    def controller_consulta_producto_en_bodega(self, datos, ventana):
        """
        recibe los datos del formulario datos = [producto,bodega]
        """

        if not self.verificar_datos(datos):
            return  # Si los datos no son válidos, no continuar con el registro

        if datos[1] not in self.bodegas:  # Verificar si  hay un bodegas con ese nombre
            messagebox.showinfo(
                "Aviso", f"La bodega'{datos[1]}' no se encuentra registrada.")
            return

        if self.negocio.consultar_producto_en_bodega(*datos):
            detalles = f"Producto: {datos[0]}\nEncontrado en Bodega: {datos[1]}"
            messagebox.showinfo("Producto en Bodega", detalles)
        else:
            messagebox.showwarning(
                "No encontrado", f"El producto '{datos[0]}' no está en la bodega '{datos[1]}'.")

    def controller_calcular_total_stock(self):
        total_stock = self.negocio.calcular_valor_total_stock()
        messagebox.showinfo(
            'Aviso', f'El saldo total del  stock es de$: {total_stock}')

    def controller_generar_informe_stock(self):
        # Crear ventana emergente para mostrar el informe
        ventana = tk.Toplevel()
        ventana.title("Informe de Stock")
        ventana.geometry("600x430")  # Ajustar tamaño de la ventana

        # Obtener los datos del informe desde el negocio
        informe_stock_total = self.negocio.genera_informes_stock()

        # Preparar los textos para mostrar cada sección del informe
        informe_texto = "Informe de Stock Total\n"
        datos = informe_stock_total['stock_total']
        informe_texto += f"Total stock: {datos[0]} Productos -- Unidades en total: {datos[1]} \n\n"

        # Generar texto para Categorías
        informe_texto += "Stock por Categoría:\n"
        for categoria, datos in informe_stock_total["categorias"].items():
            informe_texto += f"- {categoria}:Productos Registrados {datos[0]} Cantidas en stock {datos[1]} unidades en total\n"

        # Generar texto para Proveedores
        informe_texto += "\nStock por Proveedor:\n"
        for proveedor, datos in informe_stock_total["proveedores"].items():
            informe_texto += f"- {proveedor}: Productos Registrados: {datos[0]} Cantidad que suministro: {datos[1]}\n"

        # Generar texto para Bodegas
        informe_texto += "\nStock por Bodega:\n"
        for bodega, datos in informe_stock_total["bodegas"].items():
            informe_texto += f"- {bodega}: Productos Registrados: {datos[0]}, Unidades Disponibles: {datos[1]}\n"

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

        # Botón para cerrar la ventana
        tk.Button(ventana, text="Cerrar",
                  command=ventana.destroy).pack(pady=10)
