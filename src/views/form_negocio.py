
import tkinter as tk
from tkinter import messagebox


class FormNegocio:
    def registrar_producto(self):
        # Crear una nueva ventana para el formulario
        ventana = tk.Toplevel()
        ventana.title("Registrar Producto")

        # Etiquetas y entradas para los campos del formulario
        tk.Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Descripción:").grid(
            row=1, column=0, padx=10, pady=5)
        descripcion_entry = tk.Entry(ventana)
        descripcion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Precio:").grid(
            row=2, column=0, padx=10, pady=5)
        precio_entry = tk.Entry(ventana)
        precio_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Stock Inicial:").grid(
            row=3, column=0, padx=10, pady=5)
        stock_entry = tk.Entry(ventana)
        stock_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Categoría:").grid(
            row=4, column=0, padx=10, pady=5)
        categoria_entry = tk.Entry(ventana)
        categoria_entry.grid(row=4, column=1, padx=10, pady=5)

        # Botón para guardar
        tk.Button(ventana, text="Guardar", command=lambda: self.guardar_producto(
            nombre_entry.get(), descripcion_entry.get(), precio_entry.get(), stock_entry.get(), categoria_entry.get(), ventana)
        ).grid(row=5, column=0, columnspan=2, pady=10)

    def registrar_categoria(self):
        ventana = tk.Toplevel()
        ventana.title("Registrar Categoría")

        tk.Label(ventana, text="Nombre de la Categoría:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Descripción:").grid(
            row=1, column=0, padx=10, pady=5)
        descripcion_entry = tk.Entry(ventana)
        descripcion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Guardar", command=lambda: self.guardar_categoria(
            nombre_entry.get(), descripcion_entry.get(), ventana)
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def guardar_categoria(self, nombre, descripcion, ventana):
        if not (nombre and descripcion):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        # Simular guardado
        messagebox.showinfo(
            "Éxito", f"Categoría '{nombre}' registrada correctamente.")
        ventana.destroy()

    def registrar_bodega(self):
        ventana = tk.Toplevel()
        ventana.title("Registrar Bodega")

        tk.Label(ventana, text="Nombre de la Bodega:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Ubicación:").grid(
            row=1, column=0, padx=10, pady=5)
        ubicacion_entry = tk.Entry(ventana)
        ubicacion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Capacidad Máxima:").grid(
            row=2, column=0, padx=10, pady=5)
        capacidad_entry = tk.Entry(ventana)
        capacidad_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Guardar", command=lambda: self.guardar_bodega(
            nombre_entry.get(), ubicacion_entry.get(), capacidad_entry.get(), ventana)
        ).grid(row=3, column=0, columnspan=2, pady=10)

    def guardar_bodega(self, nombre, ubicacion, capacidad, ventana):
        if not (nombre and ubicacion and capacidad):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            capacidad = int(capacidad)
            # Simular guardado
            messagebox.showinfo(
                "Éxito", f"Bodega '{nombre}' registrada correctamente.")
            ventana.destroy()
        except ValueError:
            messagebox.showerror(
                "Error", "Capacidad debe ser un número entero.")

    def registrar_proveedor(self):
        ventana = tk.Toplevel()
        ventana.title("Registrar Proveedor")

        tk.Label(ventana, text="Nombre del Proveedor:").grid(
            row=0, column=0, padx=10, pady=5)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Dirección:").grid(
            row=1, column=0, padx=10, pady=5)
        direccion_entry = tk.Entry(ventana)
        direccion_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Teléfono:").grid(
            row=2, column=0, padx=10, pady=5)
        telefono_entry = tk.Entry(ventana)
        telefono_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Guardar", command=lambda: self.guardar_proveedor(
            nombre_entry.get(), direccion_entry.get(), telefono_entry.get(), ventana)
        ).grid(row=3, column=0, columnspan=2, pady=10)

    def guardar_proveedor(self, nombre, direccion, telefono, ventana):
        if not (nombre and direccion and telefono):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        # Simular guardado
        messagebox.showinfo(
            "Éxito", f"Proveedor '{nombre}' registrado correctamente.")
        ventana.destroy()

    def consultar_informacion_producto(self):
        ventana = tk.Toplevel()
        ventana.title("Consultar Información Producto")

        tk.Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(ventana)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Consultar", command=lambda: self.mostrar_informacion_producto(producto_entry.get())).grid(
            row=1, column=0, columnspan=2, pady=10)

    def mostrar_informacion_producto(self, producto):
        # Simular consulta
        if producto:  # Reemplazar con la lógica real
            messagebox.showinfo("Información del Producto",
                                f"Detalles del producto: {producto}")
        else:
            messagebox.showerror(
                "Error", "Debe ingresar un nombre de producto.")

    def consultar_informacion_categoria(self):
        ventana = tk.Toplevel()
        ventana.title("Consultar Información Categoría")

        tk.Label(ventana, text="Nombre de la Categoría:").grid(
            row=0, column=0, padx=10, pady=5)
        categoria_entry = tk.Entry(ventana)
        categoria_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Consultar", command=lambda: self.mostrar_informacion_categoria(categoria_entry.get())).grid(
            row=1, column=0, columnspan=2, pady=10)

    def mostrar_informacion_categoria(self, categoria):
        if categoria:  # Reemplazar con lógica real
            messagebox.showinfo("Información de la Categoría",
                                f"Detalles de la categoría: {categoria}")
        else:
            messagebox.showerror(
                "Error", "Debe ingresar un nombre de categoría.")

    def consultar_informacion_proveedor(self):
        ventana = tk.Toplevel()
        ventana.title("Consultar Información Proveedor")

        tk.Label(ventana, text="Nombre del Proveedor:").grid(
            row=0, column=0, padx=10, pady=5)
        proveedor_entry = tk.Entry(ventana)
        proveedor_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Consultar", command=lambda: self.mostrar_informacion_proveedor(proveedor_entry.get())).grid(
            row=1, column=0, columnspan=2, pady=10)

    def mostrar_informacion_proveedor(self, proveedor):
        if proveedor:  # Reemplazar con lógica real
            messagebox.showinfo("Información del Proveedor",
                                f"Detalles del proveedor: {proveedor}")
        else:
            messagebox.showerror(
                "Error", "Debe ingresar un nombre de proveedor.")

    def consultar_informacion_bodega(self):
        ventana = tk.Toplevel()
        ventana.title("Consultar Información Bodega")

        tk.Label(ventana, text="Nombre de la Bodega:").grid(
            row=0, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(ventana)
        bodega_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Consultar", command=lambda: self.mostrar_informacion_bodega(bodega_entry.get())).grid(
            row=1, column=0, columnspan=2, pady=10)

    def mostrar_informacion_bodega(self, bodega):
        if bodega:  # Reemplazar con lógica real
            messagebox.showinfo("Información de la Bodega",
                                f"Detalles de la bodega: {bodega}")
        else:
            messagebox.showerror("Error", "Debe ingresar un nombre de bodega.")

    def consultar_producto_en_bodega(self):
        ventana = tk.Toplevel()
        ventana.title("Consultar Producto en Bodega")

        tk.Label(ventana, text="Nombre del Producto:").grid(
            row=0, column=0, padx=10, pady=5)
        producto_entry = tk.Entry(ventana)
        producto_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Bodega:").grid(
            row=1, column=0, padx=10, pady=5)
        bodega_entry = tk.Entry(ventana)
        bodega_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(ventana, text="Consultar", command=lambda: self.mostrar_producto_en_bodega(
            producto_entry.get(), bodega_entry.get())).grid(row=2, column=0, columnspan=2, pady=10)

    def mostrar_producto_en_bodega(self, producto, bodega):
        if not producto or not bodega:
            messagebox.showerror("Error", "Debe completar todos los campos.")
            return

        # Aquí puedes agregar lógica para consultar el producto en la bodega
        # Simulación de una respuesta:
        encontrado = True  # Cambiar según la lógica real
        if encontrado:
            detalles = f"Producto: {producto}\nBodega: {bodega}\nStock disponible: 20 unidades"
            messagebox.showinfo("Producto en Bodega", detalles)
        else:
            messagebox.showwarning(
                "No encontrado", f"El producto '{producto}' no está en la bodega '{bodega}'.")

    def calcular_valor_total_stock(self):
        # Lógica simulada de cálculo de stock
        valor_total = 10000  # Reemplazar con el cálculo real
        messagebox.showinfo("Valor Total del Stock",
                            f"El valor total del stock es: ${valor_total}")

    def generar_informe_stock(self):
        ventana = tk.Toplevel()
        ventana.title("Generar Informe de Stock")

        informe_texto = "Stock Total: 100\nStock por Categoría: \n - Categoría 1: 50\n - Categoría 2: 50\n..."
        tk.Label(ventana, text="Informe de Stock:").pack(pady=10)
        text_widget = tk.Text(ventana, wrap="word", height=10, width=50)
        text_widget.insert("1.0", informe_texto)
        text_widget.config(state="disabled")  # Hacer el texto de solo lectura
        text_widget.pack(pady=10)
