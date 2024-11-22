import json
import os


class DataBase:
    def __init__(self):
        # Definir las rutas para cada archivo JSON
        self.path_productos = os.path.join('database', 'productos.json')
        self.path_categorias = os.path.join('database', 'categorias.json')
        self.path_proveedores = os.path.join('database', 'proveedores.json')
        self.path_bodegas = os.path.join('database', 'bodegas.json')

        # Cargar los datos al iniciar
        self.productos = self.cargar_datos(self.path_productos)
        self.categorias = self.cargar_datos(self.path_categorias)
        self.proveedores = self.cargar_datos(self.path_proveedores)
        self.bodegas = self.cargar_datos(self.path_bodegas)

    def cargar_datos(self, path_archivo_json):
        """Cargar los datos desde un archivo JSON y devolver un diccionario."""
        with open(path_archivo_json, 'r', encoding='utf-8') as file:
            datos = json.load(file)
        return datos

    def actualizar_datos(self, path_archivo_json, diccionario_actualizado):
        """Actualizar los datos en el archivo JSON con un diccionario nuevo."""
        with open(path_archivo_json, 'w', encoding='utf-8') as file:
            json.dump(diccionario_actualizado, file,
                      indent=4, ensure_ascii=False)
        print(f"Datos actualizados correctamente en {path_archivo_json}.")

    def get_productos(self):
        return self.productos

    def get_categorias(self):
        return self.categorias

    def get_proveedores(self):
        return self.proveedores

    def get_bodegas(self):
        return self.bodegas

    def set_productos(self, productos):
        """Asignar nuevos datos a productos y luego guardar."""
        self.productos = productos
        self.actualizar_datos(self.path_productos, self.productos)

    def set_categorias(self, categorias):
        """Asignar nuevos datos a categorías y luego guardar."""
        self.categorias = categorias
        self.actualizar_datos(self.path_categorias, self.categorias)

    def set_proveedores(self, proveedores):
        """Asignar nuevos datos a proveedores y luego guardar."""
        self.proveedores = proveedores
        self.actualizar_datos(self.path_proveedores, self.proveedores)

    def set_bodegas(self, bodegas):
        """Asignar nuevos datos a bodegas y luego guardar."""
        self.bodegas = bodegas
        self.actualizar_datos(self.path_bodegas, self.bodegas)
