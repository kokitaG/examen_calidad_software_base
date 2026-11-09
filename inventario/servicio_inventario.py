"""Actividad P2: completar las reglas de negocio y sus pruebas unitarias."""
from decimal import Decimal
from inventario.modelos import Producto
from inventario.repositorio import RepositorioProductos


class ServicioInventario:
    def __init__(self, repositorio: RepositorioProductos) -> None:
        self.repositorio = repositorio

    def agregar_producto(self, codigo: str, nombre: str, precio: Decimal, existencia: int) -> Producto:
        """Registra un producto; valida código, nombre, precio y existencia.

        Requisitos: código/nombre no vacíos; precio > 0; existencia >= 0;
        no permitir códigos duplicados. Devolver el producto guardado.
        """
        # TODO P2: implementar reglas de validación y persistencia.
        raise NotImplementedError("Implementa agregar_producto en P2")

    def consultar_existencia(self, codigo: str) -> int:
        """Devuelve existencias; si no existe, propaga ProductoNoEncontrado."""
        # TODO P2
        raise NotImplementedError("Implementa consultar_existencia en P2")

    def validar_inventario(self, codigo: str, cantidad: int) -> bool:
        """Exige cantidad > 0 y producto existente.

        Devuelve True cuando hay suficientes unidades. Devuelve False si
        la existencia es insuficiente (no modifica el inventario).
        """
        # TODO P2
        raise NotImplementedError("Implementa validar_inventario en P2")

    def calcular_total(self, codigo: str, cantidad: int) -> Decimal:
        """Devuelve precio * cantidad si cantidad > 0 y producto existe.

        No descuenta inventario. Una existencia insuficiente no invalida
        el cálculo de cotización; la venta real lo validará después.
        """
        # TODO P2
        raise NotImplementedError("Implementa calcular_total en P2")
