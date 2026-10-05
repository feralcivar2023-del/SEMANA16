import json
from pathlib import Path

class ArchivoServicio:
    def __init__(self, ruta_base="datos"):
        self.carpeta_raiz = Path(__file__).parent.parent
        self.ruta = self.carpeta_raiz / ruta_base
        self.ruta.mkdir(exist_ok=True)

    def leer_json(self, nombre):
        ruta_completa = self.ruta / nombre
        try:
            with open(ruta_completa, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f" Archivo no encontrado: {ruta_completa}")
            return []

    def guardar_json(self, nombre, datos):
        ruta_completa = self.ruta / nombre
        with open(ruta_completa, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)