import re
from models.database import DataBase


class Negocio:
    def __init__(self):
        self.db = DataBase()

    def get_datos(self):
        return {"productos": self.db.get_productos(),
                "categorias": self.db.get_categorias(),
                "proveedores": self.db.get_proveedores(),
                "bodegas": self.db.get_bodegas(), }

    def registrar_producto(self, nombre, descripcion, precio, stock, categoria, proveedor):
        # Crear un producto con los datos proporcionados
        producto = {
            "descripcion": descripcion,
            "categoria": categoria,
            "proveedor": proveedor,
            "precio": precio,
            "stock": stock
        }

        # Obtener los productos actuales
        productos = self.db.get_productos()
        # Añadir el nuevo producto
        productos[nombre] = producto

        # Añadir el nombre del producto a la lista de productos de la categoría y proveedor correspondientes
        self.db.get_categorias()[categoria]['productos'].append(nombre)
        self.db.get_proveedores()[proveedor]['productos'].append(nombre)

        # Eliminar duplicados de la lista de productos del proveedor
        self.db.get_proveedores()[proveedor]['productos'] = list(
            set(self.db.get_proveedores()[proveedor]['productos']))

        # Guardar los cambios
        self.db.set_productos(productos)
        self.db.set_categorias(self.db.get_categorias())
        self.db.set_proveedores(self.db.get_proveedores())

    def registrar_categoria(self, nombre, descripcion):
        # Crear una nueva categoría
        categoria = {
            "descripcion": descripcion,
            "productos": []  # Iniciar la lista de productos vacía
        }

        # Obtener las categorías existentes
        categorias = self.db.get_categorias()
        categorias[nombre] = categoria

        # Guardar los cambios
        self.db.set_categorias(categorias)

    def registrar_proveedor(self, nombre, direccion, telefono, lista_productos):
        # Limpiar y procesar la lista de productos del proveedor
        lista_productos = re.sub(r",\s+", ",", lista_productos)
        lista_productos = [f"{x}" for x in lista_productos.split(",")]

        # Obtener los proveedores actuales
        proveedores = self.db.get_proveedores()
        proveedores[nombre] = {
            "direccion": direccion,
            "telefono": telefono,
            "productos": lista_productos
        }

        # Guardar los cambios
        self.db.set_proveedores(proveedores)

        return True

    def registrar_bodega(self, nombre, ubicacion, capacidad, lista_productos):
        # Limpiar y procesar la lista de productos de la bodega
        lista_productos = re.sub(r",\s+", ",", lista_productos)
        lista_productos = [f"{x}" for x in lista_productos.split(",")]

        # Obtener las bodegas actuales
        bodegas = self.db.get_bodegas()
        bodegas[nombre] = {
            "ubicacion": ubicacion,
            "capacidad": capacidad,
            "productos": lista_productos
        }

        # Guardar los cambios
        self.db.set_bodegas(bodegas)

        return True

    def consultar_informacion_producto(self, nombre):
        return self.db.get_productos().get(nombre)

    def consultar_informacion_categoria(self, nombre):
        return self.db.get_categorias().get(nombre)

    def consultar_informacion_proveedor(self, nombre):
        return self.db.get_proveedores().get(nombre)

    def consultar_informacion_bodega(self, nombre):
        return self.db.get_bodegas().get(nombre)

    def consultar_producto_en_bodega(self, producto, bodega):
        return producto in self.db.get_bodegas().get(bodega, {}).get('productos', [])

    def calcular_valor_total_stock(self):
        total_stock = 0
        # Calcular el valor total del stock de todos los productos
        for producto in self.db.get_productos().values():
            total_stock += producto['stock'] * producto['precio']
        return total_stock

    def genera_informes_stock(self):
        def obtener_datos(entidades):
            informe = {}
            """
            Genera un informe con el total de productos y el stock total
            para cada entidad (categoría, proveedor o bodega).

            Parámetros:
            - entidades (dict): Diccionario que contiene las entidades
            (categorías, bodegas o proveedores) con sus productos.

            Retorna:
            - informe (dict): Diccionario con la información agregada de stock
            por cada entidad.
            """
            for entidad, datos in entidades.items():
                # Obtener la lista de productos de la entidad
                lista_productos = datos.get('productos', [])
                stock_total_productos = 0

                # Calcular el stock total de los productos en esta entidad
                for producto in lista_productos:
                    if producto in self.db.get_productos():  # Verificar si el producto existe
                        stock_total_productos += self.db.get_productos()[
                            producto]['stock']

                # Guardar la información en el informe
                informe[entidad] = [
                    len(lista_productos),  # Número de productos
                    stock_total_productos  # Stock total
                ]
            return informe

        def stock_total():
            stock_total = 0
            total_productos = len(self.db.get_productos())
            for producto, datos in self.db.get_productos().items():
                stock_total += datos['stock']
            return [total_productos, stock_total]

        # Generar informes separados para cada tipo de entidad
        informe_categoria = obtener_datos(self.db.get_categorias())
        informe_proveedor = obtener_datos(self.db.get_proveedores())
        informe_bodega = obtener_datos(self.db.get_bodegas())

        return {
            "stock_total": stock_total(),
            "categorias": informe_categoria,
            "proveedores": informe_proveedor,
            "bodegas": informe_bodega
        }
