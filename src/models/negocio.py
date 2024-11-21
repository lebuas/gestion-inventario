import re


class Negocio:
    def __init__(self, productos, categorias, proveedores, bodegas):
        self.productos = productos
        self.categorias = categorias
        self.proveedores = proveedores
        self.bodegas = bodegas

    def registrar_producto(self, nombre, descripcion, precio, stock, categoria, proveedor):
        producto = {
            "descripcion": descripcion,
            "categoria": categoria,
            "proveedor": proveedor,
            "precio": precio,
            "stock": stock
        }

        self.productos[nombre] = producto
        self.categorias[categoria]['productos'].append(nombre)
        self.proveedores[proveedor]['productos'].append(nombre)

        self.proveedores[proveedor]['productos'] = list(
            set(self.proveedores[proveedor]['productos']))

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
        self.proveedores[nombre]['productos'] = list(
            set(self.proveedores[nombre]['productos']))

    def registrar_bodega(self, nombre, ubicacion, capacidad, lista_productos):
        lista_productos = re.sub(r",\s+", ",", lista_productos)
        lista_productos = [f"{x}" for x in lista_productos.split(",")]
        datos_bodega = {"ubicacion": ubicacion,
                        "capacidad": capacidad,
                        "productos": list(lista_productos)
                        }
        self.bodegas[nombre] = datos_bodega

    def consultar_informacion_producto(self, nombre):
        datos_producto = self.productos[nombre]
        return datos_producto

    def consultar_informacion_categoria(self, nombre):
        datos_categoria = self.categorias[nombre]
        return datos_categoria

    def consultar_informacion_proveedor(self, nombre):
        datos_proveedor = self.proveedores[nombre]
        return datos_proveedor

    def consultar_informacion_bodega(self, nombre):
        datos_bodega = self.bodegas[nombre]
        return datos_bodega

    def consultar_producto_en_bodega(self, producto, bodega):
        if producto not in self.bodegas[bodega]['productos']:
            return False
        return True

    def calcular_valor_total_stock(self):
        total_stock = 0
        for _, datos in self.productos.items():
            total_producto = datos['stock'] * datos['precio']
            total_stock += total_producto
        return total_stock

    def genera_informes_stock(self):
        self.stock_total = 0
        self.total_productos = 0

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

                # Inicializar el stock total de los productos
                stock_total_productos = 0

                # Calcular el stock total de los productos en esta entidad
                for producto in lista_productos:
                    if producto in self.productos:  # Verificar si el producto existe en self.productos
                        stock_total_productos += self.productos[producto]['stock']
                    # Si el producto no existe, simplemente lo salta y no hace nada

                # Guardar la información en el informe
                informe[entidad] = [
                    len(lista_productos),  # Número de productos
                    stock_total_productos  # Stock total
                ]

                # Actualizar los totales
                self.stock_total += stock_total_productos
                self.total_productos += len(lista_productos)

            return informe

        # Generar informes separados para cada tipo de entidad
        informe_categoria = obtener_datos(self.categorias)
        informe_proveedor = obtener_datos(self.proveedores)
        informe_bodega = obtener_datos(self.bodegas)

        return {
            "stock_total": [self.total_productos, self.stock_total],
            "categorias": informe_categoria,
            "proveedores": informe_proveedor,
            "bodegas": informe_bodega
        }
