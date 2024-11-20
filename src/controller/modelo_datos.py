
class ModeloDatos:
    def __init__(self):
        # Inicializa las listas para almacenar los datos
        self.productos = []
        self.proveedores = []
        self.bodegas = []

    def agregar_producto(self, nombre, descripcion, precio, stock, categoria):
        producto = {
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
            "categoria": categoria
        }
        self.productos.append(producto)

    def obtener_productos(self):
        return self.productos

    def agregar_proveedor(self, nombre, direccion, telefono):
        proveedor = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono
        }
        self.proveedores.append(proveedor)

    def obtener_proveedores(self):
        return self.proveedores

    def agregar_bodega(self, nombre, ubicacion, capacidad):
        bodega = {
            "nombre": nombre,
            "ubicacion": ubicacion,
            "capacidad": capacidad
        }
        self.bodegas.append(bodega)

    def obtener_bodegas(self):
        return self.bodegas
