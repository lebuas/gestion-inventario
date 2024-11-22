from models.database import DataBase


class Producto:
    def __init__(self):
        # Inicializa la base de datos correctamente
        self.db = DataBase()  # Asegúrate de que sea una instancia
        # Carga los productos desde la base de datos
        self.productos = self.db.get_productos()

    def get_datos(self):
        return self.productos

    def aumentar_stock(self, nombre, cantidad):
        # Verificar que el producto exista
        if nombre not in self.productos:
            return False
        stock_actual = self.productos[nombre]['stock']

        if cantidad <= 0:
            return False  # No se puede aumentar con una cantidad negativa o cero

        # Calcular el nuevo stock sumando la cantidad
        nuevo_stock = stock_actual + cantidad

        # Actualizar el stock del producto
        self.productos[nombre]['stock'] = nuevo_stock
        # Guarda los datos actualizados en el archivo
        self.db.set_productos(self.productos)
        return True

    def disminuir_stock(self, nombre, cantidad):
        stock_actual = self.productos[nombre]['stock']

        if cantidad > stock_actual:
            return False  # No se puede disminuir más del stock disponible

        # Calcular el nuevo stock restando la cantidad
        stock_actual -= cantidad
        self.productos[nombre]['stock'] = stock_actual

        # Guardar los cambios
        self.db.set_productos(self.productos)
        return True
