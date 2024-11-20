from controller.lista_datos import LisDatos
from models.negocio import Negocio
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

    def controller_registro_producto(self, datos, ventana):
        """
        controller_registro_producto, recibe una lista con los datos que
        recoge del formulario.
        El orden es: datos = [nombre, descripcion, precio, stock, categoria]
        y se le envían al método registrar_producto desempaquetado como *datos.
        """

        if not self.verificar_datos(datos):
            return  # Si los datos no son válidos, no continuar con el registro

        if datos[0] in self.productos:  # verificar si el producto
            messagebox.showinfo(
                "Aviso", f"el producto{datos[0]} ya se encuentra registrado")
            return
        if datos[4] not in self.categorias:
            messagebox.showinfo(
                "Aviso", "Esa categoria no esta registrada, registrela antes de agregar el producto")
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

            ventana.destroy()

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
            ventana.destroy()

        except Exception as e:
            # Captura cualquier otro error general
            messagebox.showerror(
                "Error", f"Hubo un error al registrar la categoría: {e}")

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
        datos = [nombre, hubicacion, capacida, lista_producotos]
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
