class Producto:
    def __init__(self, nombre, nueva_cantidad, lista_productos):
        self.nombre = nombre
        # self.descripcion = lista_productos[nombre]['descripcion']
        # self.precio = lista_productos[nombre]['precio']
        # self.stock = lista_productos[nombre]['stock']
        self.cantida = nueva_cantidad
        self.productos = lista_productos

    def aumentar_stock(self):
        self.stock += self.cantida
        self.productos[self.nombre]['stock'] = self.stock

    def disminuir_stock(self):
        # Implementación para disminuir el stock
        if self.stock >= self.cantida:
            self.stock -= self.cantida
            self.productos[self.nombre]['stock'] = self.stock
            return True
        else:
            return False
