from controller.lista_datos import LisDatos
from models.negocio import Negocio
from tkinter import messagebox


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
                "Error", f"Hubo un error al registrar el proveedor: {e}")

    def controller_registro_bodega(self, datos, ventana):
        """
        Recibe una lista con los datos para registrar una bodega:
        datos = [nombre_bodega, direccion_bodega]
        """

        if not self.verificar_datos(datos):
            return  # Si los datos no son válidos, no continuar con el registro

        if datos[0] in self.bodegas:  # Verificar si la bodega ya está registrada
            messagebox.showinfo(
                "Aviso", f"La bodega '{datos[0]}' ya se encuentra registrada.")
            return

        try:
            # Registrar la bodega en el diccionario
            self.bodegas[datos[0]] = {"direccion": datos[1]}

            # Mostrar mensaje de éxito
            messagebox.showinfo(
                "Éxito", f"Bodega '{datos[0]}' registrada correctamente.")

            # Cerrar la ventana del formulario solo si el registro es exitoso
            ventana.destroy()

        except Exception as e:
            # Captura cualquier otro error general
            messagebox.showerror(
                "Error", f"Hubo un error al registrar la bodega: {e}")
