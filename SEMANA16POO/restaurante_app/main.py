import tkinter as tk
from pathlib import Path
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class Aplicacion:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Restaurante App — Semana 16")
        self.raiz.geometry("780x580")

        ruta_raiz = Path(__file__).parent
        ruta_icono = ruta_raiz / "assets" / "logo.ico"
        if ruta_icono.exists():
            try:
                self.raiz.iconbitmap(str(ruta_icono))
            except Exception as e:
                print(f"Ícono: {e}")

        self.servicio = RestauranteServicio()
        self._mostrar_login()

    def _mostrar_login(self):
        LoginView(self.raiz, self.servicio, self._al_iniciar_sesion)

    def _al_iniciar_sesion(self, usuario):
        for w in self.raiz.winfo_children():
            w.destroy()
        MainView(self.raiz, self.servicio, usuario, self._al_cerrar_sesion)

    def _al_cerrar_sesion(self):
        for w in self.raiz.winfo_children():
            w.destroy()
        self._mostrar_login()

    def ejecutar(self):
        self.raiz.mainloop()

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
   