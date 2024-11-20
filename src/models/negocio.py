import re


class Negocio:
    def __init__(self, productos, categorias, proveedores, bodegas):
        self.productos = productos
        self.categorias = categorias
        self.proveedores = proveedores
        self.bodegas = bodegas

    def registrar_producto(self, nombre, descripcion, precio, stock, categoria):
        producto = {
            "descripcion": descripcion,
            "categoria": categoria,
            "precio": precio,
            "stock": stock
        }

        self.productos[nombre] = producto
        self.categorias[categoria]['productos'].append(nombre)

    def registrar_categoria(self, nombre, descripcion):
        categoria = {
            "descripcion": descripcion,
            "productos": []
        }
        self.categorias[nombre] = categoria

    def registrar_proveedor(self, nombre, direccion, telefono, lista_productos):
        lista_productos = re.sub(r",\s+", ",", lista_productos)
        lista_productos = [f"{x}" for x in lista_productos.split(",")]
        datos_proveedor = {"direccion": direccion,
                           "telefono": telefono,
                           "productos": list(lista_productos)
                           }
        self.proveedores[nombre] = datos_proveedor

    def registrar_bodega(self, nombre, ubicacion, capacidad, lista_productos):
        lista_productos = re.sub(r",\s+", ",", lista_productos)
        lista_productos = [f"{x}" for x in lista_productos.split(",")]
        datos_bodega = {"hubicacion": ubicacion,
                        "capacidad": capacidad,
                        "lista_producotos": list(lista_productos)
                        }
        self.bodegas[nombre] = datos_bodega

    def consultar_informacion_producto(self, producto_id):
        pass  # Lógica para consultar información de un producto

    def consultar_informacion_categoria(self, categoria_id):
        pass  # Lógica para consultar información de una categoría

    def consultar_informacion_proveedor(self, nombre):
        datos_proveedor = self.proveedores[nombre]
        return datos_proveedor

    def consultar_informacion_bodega(self, bodega_id):
        pass  # Lógica para consultar información de una bodega

    def consultar_producto_en_bodega(self, producto_id, bodega_id):
        pass  # Lógica para consultar si un producto está en una bodega

    def calcular_valor_total_stock(self):
        pass  # Lógica para calcular el valor total del stock
