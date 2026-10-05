from datetime import datetime

class Venta:
    def __init__(self, id, id_usuario, nombre_usuario, id_producto, nombre_producto, precio_producto, fecha=None):
        self.id = id
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.precio_producto = precio_producto
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "id_producto": self.id_producto,
            "nombre_producto": self.nombre_producto,
            "precio_producto": self.precio_producto,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(**datos)
