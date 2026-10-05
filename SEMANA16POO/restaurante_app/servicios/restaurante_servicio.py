from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.archivo = ArchivoServicio()
        self._productos = [Producto.from_dict(d) for d in self.archivo.leer_json("productos.json")]
        self._usuarios = [Usuario.from_dict(d) for d in self.archivo.leer_json("usuarios.json")]
        self._ventas = [Venta.from_dict(d) for d in self.archivo.leer_json("ventas.json")]

    def validar_acceso(self, usuario, clave):
        for u in self._usuarios:
            if u.usuario == usuario and u.contrasena == clave:
                return u
        return None

    def listar_productos(self):
        return self._productos

    def listar_usuarios(self):
        return self._usuarios

    def listar_ventas(self):
        return self._ventas

    def registrar_venta(self, id_usuario, id_producto):
        usuario = next((u for u in self._usuarios if u.id == id_usuario), None)
        if not usuario:
            return False, "Usuario no encontrado"
        
        producto = next((p for p in self._productos if p.id == id_producto), None)
        if not producto:
            return False, "Producto no encontrado"
        
        nuevo_id = max([v.id for v in self._ventas], default=0) + 1
        
        venta = Venta(
            id=nuevo_id,
            id_usuario=usuario.id,
            nombre_usuario=usuario.nombre_completo,
            id_producto=producto.id,
            nombre_producto=producto.nombre,
            precio_producto=producto.precio
        )
        
        self._ventas.append(venta)
        self._guardar_ventas()
        return True, f"Venta registrada ✅ ID: {nuevo_id}"

    def _guardar_ventas(self):
        datos = [v.to_dict() for v in self._ventas]
        self.archivo.guardar_json("ventas.json", datos)
