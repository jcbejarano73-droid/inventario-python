# ==========================================
# PROGRAMA DE AUDITORÍA DE INVENTARIO
# ==========================================

inventario = [
    [101, "Mouse Gamer", 3, 10],
    [102, "Teclado Mecánico", 15, 10],
    [103, "Monitor 24 Pulgadas", 5, 8],
    [104, "Audífonos RGB", 2, 6],
    [105, "Silla Gamer", 12, 10]
]

# FUNCIÓN
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad

# INICIO DEL PROGRAMA
print("===================================")
print("      AUDITORÍA DE INVENTARIO")
print("===================================\n")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock Actual:", stock_actual)
    print("Stock Mínimo:", stock_minimo)
    print("Cantidad a Pedir:", cantidad_pedir)
    print("-----------------------------------")

print("\nProceso finalizado correctamente.")