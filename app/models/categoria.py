from models.database import DataBase


class Categoria:
    def __init__(self):
        self.db = DataBase()
        self.categorias = self.db.get_categorias()

    def get_datos(self):
        return self.categorias

    def añadir_producto(self, categoria, producto):
        if producto in self.categorias[categoria]['productos']:
            return False
        self.categorias[categoria]['productos'].append(producto)
        self.db.set_categorias(self.categorias)
        return True

    def retirar_producto(self, categoria, producto):
        """
        Retira un producto de la lista de productos de una categoría específica.
        """
        if categoria not in self.categorias:
            return False
        elif producto not in self.categorias[categoria]['productos']:
            return False

        self.categorias[categoria]['productos'].remove(producto)
        self.db.set_categorias(self.categorias)
        return True
