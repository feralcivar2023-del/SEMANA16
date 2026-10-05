class Usuario:
    def __init__(self, id, usuario, contrasena, nombre_completo):
        self.id = id
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre_completo = nombre_completo

    def to_dict(self):
        return {
            "id": self.id,
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "nombre_completo": self.nombre_completo
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(**datos)