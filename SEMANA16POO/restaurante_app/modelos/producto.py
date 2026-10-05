class Producto:
    def __init__(self, id, nombre, precio, descripcion, categoria=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.categoria = categoria

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "descripcion": self.descripcion,
            "categoria": self.categoria
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(**datos)