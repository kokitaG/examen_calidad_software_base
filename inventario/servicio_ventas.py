"""Actividad P3: integrar inventario, repositorio y registro de ventas."""
from inventario.modelos import LineaVenta, ResultadoVenta
from inventario.repositorio import RepositorioProductos
from inventario.servicio_inventario import ServicioInventario


class ServicioVentas:
    def __init__(self, inventario: ServicioInventario, repositorio: RepositorioProductos) -> None:
        self.inventario = inventario
        self.repositorio = repositorio

    def registrar_venta(self, linea: LineaVenta) -> ResultadoVenta:
        """Vende una línea de producto.

        Reglas: cantidad > 0, producto existente, existencias suficientes.
        Si no hay existencia, lanzar InventarioInsuficiente.
        Si se concreta la venta, descontar unidades exactamente una vez,
        devolver total y unidades. Ante error, no modificar existencias.
        """
        # TODO P3: implementar integración de componentes.
        raise NotImplementedError("Implementa registrar_venta en P3")
