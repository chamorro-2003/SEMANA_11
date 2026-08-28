from typing import List, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """Clase que representa la gestión de un restaurante, incluyendo productos, usuarios y ventas."""

    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._ventas: List[Venta] = []

    def establecer_datos(
        self, productos: List[Producto], usuarios: List[Usuario], ventas: List[Venta]
    ) -> None:
        self._productos = productos
        self._usuarios = usuarios
        self._ventas = ventas

    def obtener_productos(self) -> List[Producto]:
        return self._productos

    def obtener_usuarios(self) -> List[Usuario]:
        return self._usuarios

    def obtener_ventas(self) -> List[Venta]:
        return self._ventas

    def buscar_producto(self, producto_id: int) -> Optional[Producto]:
        for p in self._productos:
            if p.producto_id == producto_id:
                return p
        return None

    def buscar_usuario(self, usuario_id: str) -> Optional[Usuario]:
        for u in self._usuarios:
            if u.usuario_id == str(usuario_id).strip():
                return u
        return None

    def registrar_producto(self, nuevo_producto: Producto) -> bool:
        if self.buscar_producto(nuevo_producto.producto_id):
            print(f"¡Error! Ya existe un producto con el ID {nuevo_producto.producto_id}.")
            return False
        self._productos.append(nuevo_producto)
        return True

    def registrar_usuario(self, nuevo_usuario: Usuario) -> bool:
        if self.buscar_usuario(nuevo_usuario.usuario_id):
            print(
                f"¡Error! Ya existe un usuario registrado con el ID {nuevo_usuario.usuario_id}."
            )
            return False
        self._usuarios.append(nuevo_usuario)
        return True

    def vender_producto(self, usuario_id: str, producto_id: int, cantidad: int) -> bool:
        usuario = self.buscar_usuario(usuario_id)
        producto = self.buscar_producto(producto_id)

        if usuario is None:
            print(
                f"¡Error! Venta rechazada: El usuario con ID '{usuario_id}' no está registrado."
            )
            return False
        if producto is None:
            print(f"¡Error! Venta rechazada: El producto con ID {producto_id} no existe.")
            return False
        if cantidad <= 0:
            print("¡Error! Venta rechazada: La cantidad solicitada debe ser mayor a cero.")
            return False
        if producto.stock < cantidad:
            print(
                f"¡Error! Venta rechazada: Stock insuficiente. Disponible: {producto.stock}, Solicitado: {cantidad}."
            )
            return False

        # Generación de un nuevo ID de venta basado en la cantidad actual de ventas
        nuevo_id_venta = len(self._ventas) + 1

        # Proceso de venta y actualización de stock
        producto.vender(cantidad)
        nueva_venta = Venta(
            nuevo_id_venta, usuario.usuario_id, producto.producto_id, cantidad
        )
        self._ventas.append(nueva_venta)

        print(
            f"!Venta procesada exitosamente¡ Nuevo stock de '{producto.nombre}': {producto.stock}"
        )
        return True

    def consultar_ventas_usuario(self, usuario_id: str) -> List[Venta]:

        """Filtra y devuelve las ventas correspondientes a una identificación de usuario."""
        ventas_usuario: List[Venta] = []
        id_limpio = str(usuario_id).strip()
        for v in self._ventas:
            if v.usuario_id == id_limpio:
                ventas_usuario.append(v)
        return ventas_usuario
