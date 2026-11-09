"""Modelos sencillos para un sistema de inventario y ventas."""
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Producto:
    codigo: str
    nombre: str
    precio: Decimal
    existencia: int

    def __post_init__(self):
        """Valida las reglas de negocio inmediatamente después de instanciar."""
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if self.existencia < 0:
            raise ValueError("La existencia no puede ser negativa")


@dataclass(frozen=True)
class LineaVenta:
    codigo: str
    cantidad: int


@dataclass(frozen=True)
class ResultadoVenta:
    total: Decimal
    unidades: int
