import tkinter as tk
from tkinter import ttk
from pathlib import Path

class LoginView:
    def __init__(self, raiz, servicio, al_ingresar):
        self.raiz = raiz
        self.servicio = servicio
        self.al_ingresar = al_ingresar
        self.logo_imagen = None  
        self._construir()

    def _construir(self):
        self.raiz.configure(bg="#FFE6F2")
        
        marco_principal = tk.Frame(self.raiz, bg="#FFE6F2", padx=30, pady=30)
        marco_principal.pack(expand=True, fill="both")

        tarjeta = tk.Frame(marco_principal, bg="#FFCCE5", padx=25, pady=25)
        tarjeta.pack(expand=True)

        ruta_raiz = Path(__file__).parent.parent
        ruta_logo = ruta_raiz / "assets" / "logotipo.png"

        print(f"🔍 Buscando logo en: {ruta_logo.resolve()}")
        print(f"✅ Existe: {ruta_logo.exists()}")

        if ruta_logo.exists():
            try:
                self.logo_imagen = tk.PhotoImage(file=str(ruta_logo))
                if self.logo_imagen.width() > 180:
                    escala = 4  # Reduce a la mitad
                    self.logo_imagen = self.logo_imagen.subsample(escala)
                
                etiqueta_logo = tk.Label(
                    tarjeta,
                    image=self.logo_imagen,
                    bg="#FFCCE5"
                )
                etiqueta_logo.pack(pady=(0, 15))
                print("✅ Logo cargado correctamente")
            except Exception as e:
                print(f"❌ Error al cargar logo: {e}")
        else:
            print("❌ No se encontró el archivo logotipo.png")

        tk.Label(
            tarjeta, text="🔐 Inicio de Sesión",
            font=("Arial", 16, "bold"),
            bg="#FF99CC", fg="white", padx=20, pady=10
        ).pack(fill="x", pady=(0, 20))

        tk.Label(tarjeta, text="Usuario:", font=("Arial", 11, "bold"),
                 bg="#FFCCE5", fg="#993366").pack(anchor="w")
        self.entry_usuario = tk.Entry(
            tarjeta, font=("Arial", 12), width=30,
            bg="white", relief="solid", bd=1
        )
        self.entry_usuario.pack(pady=(5, 12))

        tk.Label(tarjeta, text="Contraseña:", font=("Arial", 11, "bold"),
                 bg="#FFCCE5", fg="#993366").pack(anchor="w")
        self.entry_clave = tk.Entry(
            tarjeta, font=("Arial", 12), width=30,
            show="*", bg="white", relief="solid", bd=1
        )
        self.entry_clave.pack(pady=(5, 20))

        tk.Button(
            tarjeta, text="✅ Ingresar",
            font=("Arial", 12, "bold"),
            bg="#FF66B2", fg="white",
            relief="flat", padx=40, pady=12,
            command=self._validar
        ).pack()

        self.etiqueta_error = tk.Label(
            tarjeta, text="", font=("Arial", 10),
            bg="#FFCCE5", fg="#CC0000"
        )
        self.etiqueta_error.pack(pady=(12, 0))

        self.entry_clave.bind("<Return>", lambda e: self._validar())
        self.entry_usuario.bind("<Return>", lambda e: self.entry_clave.focus())

    def _validar(self):
        usu = self.entry_usuario.get().strip()
        cla = self.entry_clave.get().strip()
        usuario = self.servicio.validar_acceso(usu, cla)
        if usuario:
            self.al_ingresar(usuario)
        else:
            self.etiqueta_error.config(text="❌ Usuario o contraseña incorrectos")