from models.database import DataBase


class Proveedor:
    def __init__(self):
        self.db = DataBase()
        self.proveedores = self.db.get_proveedores()

    def get_datos(self):
        return self.proveedores

    def añadir_producto(self, proveedor, producto):
        """
        Añade un producto a la lista de productos de un proveedor específico.
        """

        if proveedor not in self.proveedores:
            return False
        elif producto in self.proveedores[proveedor]['productos']:
            return False

        # Añadir el producto a la lista del proveedor
        self.proveedores[proveedor]['productos'].append(producto)
        # Guardar los cambios
        self.db.set_proveedores(self.proveedores)
        return True

    def retirar_producto(self, proveedor, producto):
        """
        Retira un producto de la lista de productos de un proveedor específico.
        """
        if proveedor not in self.proveedores:
            return False
        elif producto not in self.proveedores[proveedor]['productos']:
            return False

        # Retirar el producto de la lista del proveedor
        self.proveedores[proveedor]['productos'].remove(producto)
        # Guardar los cambios
        self.db.set_proveedores(self.proveedores)
        return True
