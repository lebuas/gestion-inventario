from models.database import DataBase


class Categoria:
    def __init__(self):
        self.db = DataBase()
        self.categorias = self.db.get_categorias()

    def get_datos(self):
        return self.categorias

    def añadir_producto(self, categoria, producto):
        """
        Añade un producto a la lista de productos de una categoría específica.
        """
        # Verificar si el producto ya está en la lista
        if producto in self.categorias[categoria]['productos']:
            return False  # El producto ya está en la lista

        self.categorias[categoria]['productos'].append(producto)

        # Guardar los cambios
        self.db.set_categorias(self.categorias)
        return True

    def retirar_producto(self, categoria, producto):
        """
        Retira un producto de la lista de productos de una categoría específica.
        """
        if categoria not in self.categorias:
            return False

        if producto not in self.categorias[categoria]['productos']:
            return False

        self.categorias[categoria]['productos'].remove(producto)

        # Guardar los cambios
        self.db.set_categorias(self.categorias)
        return True
