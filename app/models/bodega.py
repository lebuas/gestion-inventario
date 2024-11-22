from models.database import DataBase


class Bodega:
    def __init__(self):
        self.db = DataBase()
        self.bodegas = self.db.get_bodegas()

    def get_datos(self):
        return self.bodegas

    def agregar_producto(self, bodega, producto):
        """
        Añade un producto a la lista de productos de una bodega específica.
        """
        if bodega not in self.bodegas:
            return
        elif producto in self.bodegas[bodega]['productos']:
            return False  # El producto ya está asociado a la bodega

        # Añadir el producto a la lista de la bodega
        self.bodegas[bodega]['productos'].append(producto)
        # Guardar los cambios
        self.db.set_bodegas(self.bodegas)
        return True

    def retirar_producto(self, bodega, producto):
        """
        Retira un producto de la lista de productos de una bodega específica.
        """
        if bodega not in self.bodegas:
            return False  # La bodega no está registrada
        elif producto not in self.bodegas[bodega]['productos']:
            return False  # El producto no está asociado a la bodega

        # Retirar el producto de la lista de la bodega
        self.bodegas[bodega]['productos'].remove(producto)

        # Guardar los cambios
        self.db.set_bodegas(self.bodegas)
        return True
