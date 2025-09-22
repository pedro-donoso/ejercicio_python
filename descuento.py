# Solicitar datos
cantidad = int(input("Cantidad de productos: "))
precio_total = float(input("Precio total: $"))
compras_previas= int(input("Compras previas: "))

# Calcular descuentos
descuento_cantidad = 0
descuento_frecuente = 0

# Descuento por cantidad (más de 10 productos)
if cantidad > 10:
    descuento_cantidad = 10

# Descuento por cliente frecuente (más de 5 compras previas)
if compras_previas > 5:
    descuento_frecuente = 5

