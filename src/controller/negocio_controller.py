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

    def controller_registro_producto(self, datos, ventana):
        """
        controller_registro_producto, recibe una lista los datos que
        recoge del formulario.
        El orden es: datos = [nombre, descripcion, precio, categoria]
        y se le envian al metodo registrar producto desempaquedao *datos
        """
        self.negocio.registrar_producto(*datos)

        if not (x for x in datos):
            """se itera sobre la lista de datos para encontar pasibles datos
            vacios, provenientes desde el formulario
            """
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            datos[2] = float(datos[2])  # esto seria elprecio
            datos[3] = int(datos[3])  # esto seria el stock inicial
            # Simular guardado
            messagebox.showinfo(
                "Éxito", f"Producto '{datos[1]}' registrado correctamente.")
            ventana.destroy()
        except ValueError:
            messagebox.showerror(
                "Error", "Precio debe ser un número y stock un entero.")
