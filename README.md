# Sistema de Gestión de Inventario

## Integrantes del Proyecto
- **Nombre del Proyecto:** Sistema de Gestión de Inventario
- **Integrantes:**
  [Leymar Buenaventura Asprilla](https://github.com/lebuas)
  [Andres Felipe Martinez](https://github.com/PipeCoding03-COL)
```

## Requerimientos del Sistema

### Registro de Entidades
- El sistema debe permitir registrar un producto
- El sistema debe permitir registrar una categoría
- El sistema debe permitir registrar un proveedor

- El sistema debe permitir registrar una bodega 

### Gestión de Stock
- El sistema debe permitir agregar stock a un producto existente
- El sistema debe permitir retirar stock de un producto existente
- El sistema debe permitir calcular el valor total del stock

### Relaciones entre Entidades
- El sistema debe permitir agregar un producto a una categoría existente.
- El sistema debe permitir eliminar un producto de una categoría existente.
- El sistema debe permitir agregar un producto a la lista de productos suministrados por un proveedor existente.
- El sistema debe permitir eliminar un producto de la lista de productos suministrados por un proveedor existente.
- El sistema debe permitir agregar un producto a la lista de productos almacenados en una bodega existente, verificando si hay espacio disponible en la bodega.
- El sistema debe permitir retirar un producto de la lista de productos almacenados en una bodega.
- El sistema debe permitir consultar la disponibilidad de un producto en una bodega específica.

### Consultas y Reportes
- El sistema debe permitir consultar la información de un producto,
- El sistema debe permitir consultar la información de una categoría
- El sistema debe permitir consultar la información de un proveedor
- El sistema debe permitir consultar la información de una bodega
- El sistema debe permitir generar informes de stock


## Cómo Ejecutar la Aplicación

### 1. Clonar el Repositorio desde GitHub
Primero, necesitas clonar el repositorio del proyecto desde GitHub. Abre una terminal y ejecuta el siguiente comando:
```sh
https://github.com/lebuas/gestion-inventario.git
```
2. Navegar al Directorio del Proyecto

Accede al directorio del proyecto clonado desde la terminal

3. Crear y Activar un Entorno Virtual

Para evitar conflictos de dependencias, es recomendable usar un entorno virtual. Crea y activa un entorno virtual usando los siguientes comandos:

 Para crear el entorno virtual en Windows:
 ```sh
python -m venv venv
```

 Para activar el entorno virtual en Windows:
 ```sh
.\venv\Scripts\activate
```
 Para crear el entorno virtual en linux(ubuntu)/Mac:
 ```sh
python3 -m venv venv
```

 Para activar el entorno virtual en linux(ubuntu)/Mac:
 ```sh
source venv/bin/activa
```
4. Instalar los Requerimientos
Una vez activado el entorno virtual, instala las dependencias necesarias ejecutando:
```sh
pip install -r requirements.txt
```
5. Ejecutar la Aplicación

Con todo configurado, puedes ejecutar la aplicación desde la terminal, navegando hasta el directorio deonde se encuentra la entra del programa:

Desde la raíz del directorio, navegamos hasta el directorio app y dentro del directori ejecutamos:
Para linux(ubuntu)/mac
```sh
python3 main.py
```
Para windows

```sh
python main.py
