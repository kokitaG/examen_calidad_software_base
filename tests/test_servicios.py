import pytest
from decimal import Decimal
from inventario.modelos import Producto

@pytest.fixture
def catalogo_productos():
    """Fixture que proporciona un catálogo de productos preconfigurado para las pruebas."""
    return {
        "P-01": Producto("P-01", "Cuaderno", Decimal("10.00"), 100),
        "P-02": Producto("P-02", "Lapicero", Decimal("5.00"), 50),
        "P-03": Producto("P-03", "Calculadora", Decimal("50.00"), 10)
    }

class ProcesadorVentasServicio:
    """Clase de servicio emulada para evaluar la lógica comercial y de impuestos (12% IVA)."""
    @staticmethod
    def calcular_total_linea(producto: Producto, cantidad: int, aplicar_iva: bool = True) -> Decimal:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero")
        if cantidad > producto.existencia:
            raise ValueError("Existencias insuficientes")
        
        subtotal = producto.precio * cantidad
        if aplicar_iva:
            return (subtotal * Decimal("1.12")).quantize(Decimal("0.01"))
        return subtotal.quantize(Decimal("0.01"))

# Suite de pruebas parametrizadas utilizando la fixture de catálogo
@pytest.mark.parametrize(
    "codigo_prod, cantidad_solicitada, aplicar_iva, total_esperado",
    [
        ("P-01", 2, True, Decimal("22.40")),   # Caso 1: 2 Cuadernos ($20.00) + 12% IVA = $22.40
        ("P-01", 5, False, Decimal("50.00")),  # Caso 2: 5 Cuadernos ($50.00) sin IVA = $50.00
        ("P-02", 10, True, Decimal("56.00")),  # Caso 3: 10 Lapiceros ($50.00) + 12% IVA = $56.00
        ("P-03", 1, True, Decimal("56.00")),   # Caso 4: 1 Calculadora ($50.00) + 12% IVA = $56.00
    ]
)
def test_calculo_totales_parametrizados(catalogo_productos, codigo_prod, cantidad_solicitada, aplicar_iva, total_esperado):
    """Prueba parametrizada que evalúa múltiples combinaciones de cálculo fiscal."""
    # Arrange
    producto = catalogo_productos[codigo_prod]
    
    # Act
    total_calculado = ProcesadorVentasServicio.calcular_total_linea(producto, cantidad_solicitada, aplicar_iva)
    
    # Assert
    assert total_calculado == total_esperado
