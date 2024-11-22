import tkinter as tk
from tkinter import ttk
from views.form_bodega import FormBodega
from views.form_negocio import FormNegocio
from views.form_proveedor import FormProveedor
from views.form_producto import FormProducto
from views.form_categoria import FormCategoria


class GuiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Inventarios")
        self.root.geometry("800x500")  # Define tamaño de la ventana

        # Crear un frame para dividir la ventana
        self.top_frame = tk.Frame(self.root, bg="lightgray")  # Barra superior
        self.left_frame = tk.Frame(
            self.root, width=200, bg="lightgray")  # Panel de acciones
        # Frame para contenido dinámico
        self.right_frame = tk.Frame(self.root, bg="white")

        # Organizar frames
        self.top_frame.pack(side="top", fill="x")
        self.left_frame.pack(side="left", fill="y")
        self.right_frame.pack(side="right", expand=True, fill="both")

        # Crear un Notebook (pestañas) centrado
        self.notebook = ttk.Notebook(self.top_frame)
        self.notebook.pack(fill="x", pady=5)

        # Crear las pestañas (tabs)
        self.tab_negocio = tk.Frame(self.notebook)
        self.tab_producto = tk.Frame(self.notebook)
        self.tab_categoria = tk.Frame(self.notebook)
        self.tab_proveedor = tk.Frame(self.notebook)
        self.tab_bodega = tk.Frame(self.notebook)

        # Añadir las pestañas al Notebook
        self.notebook.add(self.tab_negocio, text="Negocio")
        self.notebook.add(self.tab_producto, text="Producto")
        self.notebook.add(self.tab_categoria, text="Categoría")
        self.notebook.add(self.tab_proveedor, text="Proveedor")
        self.notebook.add(self.tab_bodega, text="Bodega")

        # Crear una línea horizontal debajo del Notebook
        self.separator_top = tk.Canvas(
            self.top_frame, height=2, bg="gray", bd=0, highlightthickness=0)
        self.separator_top.pack(fill="x", padx=10, pady=5)

        # Título "Opciones" en el panel izquierdo (centrado)
        self.title_left = tk.Label(
            self.left_frame, text="Opciones", font=("Arial", 14), bg="lightgray")
        self.title_left.pack(pady=10, anchor="center")

        # Crear una línea horizontal debajo del título "Opciones"
        self.separator_left = tk.Canvas(
            self.left_frame, height=2, bg="gray", bd=0, highlightthickness=0)
        self.separator_left.pack(fill="x", padx=10, pady=5)

        # Crear un Label para el título de la sección (sin borde ni relieve)
        self.section_title = tk.Label(
            self.right_frame, text="", font=("Arial", 14), bg="lightgray")
        self.section_title.pack(fill="x")

        # Contenedor dinámico para el contenido de la derecha
        self.current_content = None
        self.current_actions_frame = None
        self.show_negocio_tab()  # Mostrar la primera pestaña por defecto

        # Asociar las funciones de cada tab
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

    def __message_welcome(self, dependence, frame):
        welcome_message = tk.Label(frame, text=f"Bienvenido a la {dependence}.\n Selecciona una de las opciones para comenzar.",
                                   font=("Arial", 12), bg="lightgray", anchor="center")
        welcome_message.pack(pady=20, padx=10, expand=True, fill="both")

    def clear_frame(self, frame, action):
        """
        Limpia el contenido del frame derecho y ejecuta una acción.

        Args:
        frame (tk.Frame): El contenedor que debe ser limpiado.
        action (callable): La acción que se ejecutará después de limpiar.
        """
        for widget in frame.winfo_children():
            widget.destroy()  # Eliminar todos los widgets del frame
        action()  # Ejecutar la acción proporcionada

    def on_tab_change(self, event):
        """Actualizar las opciones a la izquierda cuando se cambia de pestaña."""
        current_tab = self.notebook.index(
            self.notebook.select())  # Obtener el índice de la pestaña seleccionada
        if current_tab == 0:
            self.show_negocio_tab()
        elif current_tab == 1:
            self.show_producto_tab()
        elif current_tab == 2:
            self.show_categoria_tab()
        elif current_tab == 3:
            self.show_proveedor_tab()
        elif current_tab == 4:
            self.show_bodega_tab()

    def show_content(self, content):
        """Actualizar el contenido mostrado en el frame derecho."""
        if self.current_content:
            self.current_content.destroy()
        self.current_content = content
        self.current_content.pack(expand=True, fill="both")

    def update_left_buttons(self, actions):
        """Actualizar los botones en el panel izquierdo."""
        # Eliminar botones actuales si existen
        for widget in self.left_frame.winfo_children():
            # No eliminar el título "Opciones" ni la línea
            if widget != self.title_left and widget != self.separator_left:
                widget.destroy()

        # Añadir nuevos botones de acuerdo a la sección
        for text, command in actions:
            tk.Button(self.left_frame, text=text, command=command,
                      anchor="w", height=1, bg="white", relief="flat").pack(pady=3, padx=10, fill="x")

    def show_section_title(self, title):
        """Actualizar el título de la sección en la parte superior del panel derecho."""
        self.section_title.config(text=title)

    def show_negocio_tab(self):
        frame = tk.Frame(self.right_frame)
        negocio = FormNegocio()
        dependence = "Gestión de Negocio"

        # Actualizar el título de la sección
        self.show_section_title(dependence)
        self.__message_welcome(dependence, frame)

        # Opciones específicas para Negocio
        actions = [
            ("Registrar Producto", lambda: self.clear_frame(
                frame, lambda: negocio.registrar_producto(frame))),
            ("Registrar Categoría", lambda: self.clear_frame(
                frame, lambda: negocio.registrar_categoria(frame))),
            ("Registrar Proveedor", lambda: self.clear_frame(
                frame, lambda: negocio.registrar_proveedor(frame))),
            ("Registrar Bodega", lambda: self.clear_frame(
                frame, lambda: negocio.registrar_bodega(frame))),
            ("Consultar Información Producto", lambda: self.clear_frame(
                frame, lambda: negocio.consultar_informacion_producto(frame))),
            ("Consultar Información Categoría", lambda: self.clear_frame(
                frame, lambda: negocio.consultar_informacion_categoria(frame))),
            ("Consultar Información Proveedor", lambda: self.clear_frame(
                frame, lambda: negocio.consultar_informacion_proveedor(frame))),
            ("Consultar Información Bodega", lambda: self.clear_frame(
                frame, lambda: negocio.consultar_informacion_bodega(frame))),
            ("Consultar Producto en Bodega", lambda: self.clear_frame(
                frame, lambda: negocio.consultar_producto_en_bodega(frame))),
            ("Calcular Valor Total Stock", lambda: self.clear_frame(
                frame, lambda: negocio.calcular_valor_total_stock())),
            ("Generar Informe Stock", lambda: self.clear_frame(
                frame, lambda: negocio.generar_informe_stock())),
        ]
        # Actualizar botones en el panel izquierdo
        self.update_left_buttons(actions)

        self.show_content(frame)

    def show_producto_tab(self):
        frame = tk.Frame(self.right_frame)
        producto = FormProducto()
        dependence = "Gestión de Producto"

        # Actualizar el título de la sección
        self.show_section_title(dependence)
        self.__message_welcome(dependence, frame)

        # Opciones específicas para Producto
        actions = [
            ("Aumentar Stock", lambda: self.clear_frame(
                frame, lambda: producto.aumentar_stock(frame))),
            ("Disminuir Stock", lambda: self.clear_frame(
                frame, lambda: producto.disminuir_stock(frame))),
        ]

        # Actualizar botones en el panel izquierdo
        self.update_left_buttons(actions)

        self.show_content(frame)

    def show_categoria_tab(self):
        frame = tk.Frame(self.right_frame)
        categoria = FormCategoria()
        dependence = "Gestión de Categorías"

        # Actualizar el título de la sección
        self.show_section_title(dependence)
        self.__message_welcome(dependence, frame)

        # Opciones específicas para Categoría
        actions = [
            ("Agregar Producto a Categoría", lambda: self.clear_frame(
                frame, lambda: categoria.agregar_producto_categoria(frame))),
            ("Eliminar Producto de Categoría", lambda: self.clear_frame(
                frame, lambda: categoria.eliminar_producto_categoria(frame))),
        ]

        # Actualizar botones en el panel izquierdo
        self.update_left_buttons(actions)

        self.show_content(frame)

    def show_proveedor_tab(self):
        frame = tk.Frame(self.right_frame)
        proveedor = FormProveedor()
        dependence = "Gestión de Proveedores"

        # Actualizar el título de la sección
        self.show_section_title(dependence)
        self.__message_welcome(dependence, frame)

        # Opciones específicas para Proveedor
        actions = [
            ("Agregar Producto a Proveedor", lambda: self.clear_frame(
                frame, lambda: proveedor.agregar_producto_proveedor(frame))),
            ("Eliminar Producto de Proveedor", lambda: self.clear_frame(
                frame, lambda: proveedor.eliminar_producto_proveedor(frame))),
        ]

        # Actualizar botones en el panel izquierdo
        self.update_left_buttons(actions)

        self.show_content(frame)

    def show_bodega_tab(self):
        frame = tk.Frame(self.right_frame)
        bodega = FormBodega()
        dependence = "Gestión de Bodega"

        # Actualizar el título de la sección
        self.show_section_title(dependence)
        self.__message_welcome(dependence, frame)

        # Opciones específicas para Bodega
        actions = [
            ("Agregar Producto a Bodega", lambda: self.clear_frame(
                frame, lambda: bodega.agregar_producto_bodega(frame))),
            ("Retirar Producto de Bodega", lambda: self.clear_frame(
                frame, lambda: bodega.retirar_producto_bodega(frame))),
        ]

        # Actualizar botones en el panel izquierdo
        self.update_left_buttons(actions)

        self.show_content(frame)
