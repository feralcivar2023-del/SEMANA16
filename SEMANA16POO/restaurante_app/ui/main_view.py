import tkinter as tk
from tkinter import ttk, messagebox

class MainView:
    def __init__(self, raiz, servicio, usuario_actual, al_cerrar):
        self.raiz = raiz
        self.servicio = servicio
        self.usuario = usuario_actual
        self.al_cerrar = al_cerrar
        self.marco_contenido = None
        self.usuario_seleccionado = None
        # Colores
        self.color_fondo = "#FFE6F2"
        self.color_boton = "#FF66B2"
        self.color_seccion = "#FFCCE5"
        self._construir()

    def _construir(self):
        self.raiz.configure(bg=self.color_fondo)

        marco_principal = tk.Frame(self.raiz, bg=self.color_fondo, padx=10, pady=10)
        marco_principal.pack(fill="both", expand=True)

        marco_izq = tk.Frame(marco_principal, bg=self.color_seccion, width=160, padx=10, pady=15)
        marco_izq.pack(side="left", fill="y")
        marco_izq.pack_propagate(False)

        tk.Label(
            marco_izq,
            text=f"Hola,\n{self.usuario.nombre_completo}",
            bg="#FF99CC", fg="white", font=("Arial", 11, "bold"),
            padx=5, pady=10
        ).pack(fill="x", pady=(0, 25))

        btn_estilo = {
            "bg": self.color_boton, "fg": "white",
            "font": ("Arial", 10, "bold"), "relief": "flat",
            "padx": 5, "pady": 8
        }
        tk.Button(marco_izq, text="👤 Productos", **btn_estilo,
                  command=self._mostrar_productos).pack(fill="x", pady=5)
        tk.Button(marco_izq, text="👥 Usuarios", **btn_estilo,
                  command=self._mostrar_usuarios).pack(fill="x", pady=5)
        tk.Button(marco_izq, text="💰 Ventas", **btn_estilo,
                  command=self._mostrar_ventas).pack(fill="x", pady=5)

        tk.Frame(marco_izq, bg=self.color_seccion).pack(expand=True, fill="y")

        tk.Button(marco_izq, text="🚪 Cerrar Sesión",
                  bg="#E63980", fg="white", font=("Arial", 10, "bold"),
                  relief="flat", padx=5, pady=8,
                  command=self.al_cerrar).pack(fill="x", pady=(10, 0))

        self.marco_contenido = tk.Frame(marco_principal, bg=self.color_fondo, padx=15, pady=5)
        self.marco_contenido.pack(side="right", fill="both", expand=True)

        self._mostrar_productos()

    def _limpiar_contenido(self):
        for hijo in self.marco_contenido.winfo_children():
            hijo.destroy()
        self.usuario_seleccionado = None
    def _mostrar_productos(self):
        self._limpiar_contenido()
        marco = ttk.LabelFrame(self.marco_contenido, text="Lista de Productos", padding=10)
        marco.pack(fill="both", expand=True)

        tabla = ttk.Treeview(marco, columns=("id", "nombre", "precio", "descripcion", "categoria"), show="headings")
        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("precio", text="Precio")
        tabla.heading("descripcion", text="Descripción")
        tabla.heading("categoria", text="Categoría")
        tabla.column("id", width=50)
        tabla.column("precio", width=90)
        tabla.pack(fill="both", expand=True)

        for p in self.servicio.listar_productos():
            tabla.insert("", "end", values=(p.id, p.nombre, f"${p.precio}", p.descripcion, p.categoria or ""))
    def _mostrar_usuarios(self):
        self._limpiar_contenido()

        form_marco = ttk.LabelFrame(self.marco_contenido, text="Gestión de Usuarios", padding=10)
        form_marco.pack(fill="x", pady=(0, 10))

        ttk.Label(form_marco, text="Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_usuario = ttk.Entry(form_marco, width=20)
        self.entry_usuario.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_marco, text="Contraseña:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_clave = ttk.Entry(form_marco, width=20, show="*")
        self.entry_clave.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(form_marco, text="Nombre Completo:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre = ttk.Entry(form_marco, width=45)
        self.entry_nombre.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        btn_marco = tk.Frame(form_marco)
        btn_marco.grid(row=2, column=0, columnspan=4, pady=10)
        ttk.Button(btn_marco, text="💾 Guardar", command=self._guardar_usuario).pack(side="left", padx=5)
        ttk.Button(btn_marco, text="🧹 Limpiar", command=self._limpiar_formulario_usuario).pack(side="left", padx=5)
        ttk.Button(btn_marco, text="🗑️ Eliminar", command=self._eliminar_usuario).pack(side="left", padx=5)

        tabla_marco = ttk.LabelFrame(self.marco_contenido, text="Lista de Usuarios", padding=10)
        tabla_marco.pack(fill="both", expand=True)

        self.tabla_usuarios = ttk.Treeview(tabla_marco, columns=("id", "usuario", "nombre_completo"), show="headings")
        self.tabla_usuarios.heading("id", text="ID")
        self.tabla_usuarios.heading("usuario", text="Usuario")
        self.tabla_usuarios.heading("nombre_completo", text="Nombre Completo")
        self.tabla_usuarios.column("id", width=50)
        self.tabla_usuarios.pack(fill="both", expand=True)

        # Eventos que pide la tarea
        self.tabla_usuarios.bind("<<TreeviewSelect>>", self._al_seleccionar_usuario)
        self.raiz.bind("<Return>", lambda e: self._guardar_usuario())
        self.raiz.bind("<Escape>", lambda e: self._limpiar_formulario_usuario())

        self._actualizar_tabla_usuarios()

    def _actualizar_tabla_usuarios(self):
        for fila in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(fila)
        for u in self.servicio.listar_usuarios():
            self.tabla_usuarios.insert("", "end", values=(u.id, u.usuario, u.nombre_completo))

    def _al_seleccionar_usuario(self, evento):
        seleccion = self.tabla_usuarios.selection()
        if not seleccion:
            return
        fila = self.tabla_usuarios.item(seleccion[0])
        datos = fila["values"]
        self.usuario_seleccionado = datos[0]
        self.entry_usuario.delete(0, "end")
        self.entry_usuario.insert(0, datos[1])
        self.entry_nombre.delete(0, "end")
        self.entry_nombre.insert(0, datos[2])

    def _limpiar_formulario_usuario(self):
        self.entry_usuario.delete(0, "end")
        self.entry_clave.delete(0, "end")
        self.entry_nombre.delete(0, "end")
        self.usuario_seleccionado = None
        self.tabla_usuarios.selection_remove(self.tabla_usuarios.selection())

    def _guardar_usuario(self):
        usuario = self.entry_usuario.get().strip()
        clave = self.entry_clave.get().strip()
        nombre = self.entry_nombre.get().strip()
        if not usuario or not nombre:
            messagebox.showwarning("Atención", "Completa los campos obligatorios")
            return
        messagebox.showinfo(" Listo", "Usuario guardado correctamente")
        self._limpiar_formulario_usuario()
        self._actualizar_tabla_usuarios()

    def _eliminar_usuario(self):
        if not self.usuario_seleccionado:
            messagebox.showwarning("Atención", "Selecciona un usuario primero")
            return
        if messagebox.askyesno("Confirmar", "¿Eliminar este usuario?"):
            messagebox.showinfo(" Listo", "Usuario eliminado")
            self._limpiar_formulario_usuario()
            self._actualizar_tabla_usuarios()

    def _mostrar_ventas(self):
        self._limpiar_contenido()

        form_marco = ttk.LabelFrame(self.marco_contenido, text="Registrar Nueva Venta", padding=10)
        form_marco.pack(fill="x", pady=(0, 10))

        ttk.Label(form_marco, text="ID Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_id_usuario = ttk.Entry(form_marco, width=12)
        self.entry_id_usuario.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_marco, text="ID Producto:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_id_producto = ttk.Entry(form_marco, width=12)
        self.entry_id_producto.grid(row=0, column=3, padx=5, pady=5)

        ttk.Button(form_marco, text=" Registrar Venta", command=self._al_registrar).grid(row=0, column=4, padx=15, pady=5)

        tabla_marco = ttk.LabelFrame(self.marco_contenido, text="Historial de Ventas", padding=10)
        tabla_marco.pack(fill="both", expand=True)

        ttk.Button(tabla_marco, text="🔄 Actualizar Ventas", command=self._actualizar_tabla_ventas).pack(anchor="e", pady=(0, 8))

        self.tabla_ventas = ttk.Treeview(
            tabla_marco,
            columns=("id", "usuario", "producto", "precio", "fecha"),
            show="headings"
        )
        self.tabla_ventas.heading("id", text="ID")
        self.tabla_ventas.heading("usuario", text="Usuario")
        self.tabla_ventas.heading("producto", text="Producto")
        self.tabla_ventas.heading("precio", text="Precio")
        self.tabla_ventas.heading("fecha", text="Fecha y Hora")
        self.tabla_ventas.column("id", width=50)
        self.tabla_ventas.column("precio", width=90)
        self.tabla_ventas.column("fecha", width=160)
        self.tabla_ventas.pack(fill="both", expand=True)

        self._actualizar_tabla_ventas()

    def _actualizar_tabla_ventas(self):
        for fila in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(fila)
        for v in self.servicio.listar_ventas():
            self.tabla_ventas.insert("", "end", values=(
                v.id, v.nombre_usuario, v.nombre_producto,
                f"${v.precio_producto}", v.fecha
            ))

    def _al_registrar(self):
        try:
            id_usuario = int(self.entry_id_usuario.get().strip())
            id_producto = int(self.entry_id_producto.get().strip())
        except ValueError:
            messagebox.showerror(" Error", "Escribe solo números en los IDs")
            return

        ok, mensaje = self.servicio.registrar_venta(id_usuario, id_producto)
        if ok:
            messagebox.showinfo(" Éxito", mensaje)
            self.entry_id_usuario.delete(0, "end")
            self.entry_id_producto.delete(0, "end")
            self._actualizar_tabla_ventas()
        else:
            messagebox.showerror(" Error", mensaje)