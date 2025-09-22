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

# Aplicar descuentos
descuento_total = descuento_cantidad + descuento_frecuente
descuento_monto = precio_total * (descuento_total / 100)
precio_final = precio_total - descuento_monto

# Mostrar resultado
print(f"\nDescuento por cantidad: {descuento_total}%")
print(f"Descuento por cliente frecuente: {descuento_frecuente}%")
print(f"Descuento total: {descuento_total}")
print(f"Descuento: ${descuento_monto:.2f}")
print(f"Precio final: ${precio_final:.2f}")