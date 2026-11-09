import pytest
from decimal import Decimal
from inventario.modelos import Producto

def test_creacion_valida_producto():
    """Valida la instanciación de un producto con sus atributos correctos."""
    # Estructura real: Producto(codigo, nombre, precio, existencia)
    producto = Producto("P-01", "Teclado Mecánico", Decimal("45.50"), 15)
    assert producto.nombre == "Teclado Mecánico"
    assert producto.precio == Decimal("45.50")
    assert producto.existencia == 15

def test_validacion_precio_negativo_lanza_excepcion():
    """Verifica que precios menores a cero disparen un error lógico."""
    with pytest.raises(ValueError):
        Producto("P-02", "Producto Inválido", Decimal("-10.00"), 5)

def test_validacion_stock_negativo_lanza_excepcion():
    """Verifica que existencias menores a cero disparen un error lógico."""
    with pytest.raises(ValueError):
        Producto("P-03", "Producto Sin Stock", Decimal("20.00"), -5)
