# Solicitar datos
cantidad = int(input("Cantidad de productos: "))
precio_total = float(input("Precio total: $"))
compras_previas= int(input("Compras previas: "))
promocion_especial = input("¿Es día de promoción especial? (s/n): ").lower() == 's'

# Calcular descuentos
descuento_cantidad = 0
descuento_frecuente = 0
descuento_monto = 0
descuento_promocion = 0

# Descuento por cantidad (más de 10 productos)
if cantidad > 10:
    descuento_cantidad = 10

# Descuento por cliente frecuente (más de 5 compras previas)
if compras_previas > 5:
    descuento_frecuente = 5

# Descuento por monto alto (más de $500)
if precio_total > 500:
    descuento_monto = 7

# Descuento por promoción especial
if promocion_especial:
    descuento_promocion = 15

# Aplicar descuentos
descuento_total = descuento_cantidad + descuento_frecuente + descuento_monto + descuento_promocion

# Limitar descuento máximo al 30%
if descuento_total > 30:
    descuento_total = 30

descuento_monto_total = precio_total * (descuento_total / 100)
precio_final = precio_total - descuento_monto_total

# Mostrar resultado
print(f"\nDescuento por cantidad: {descuento_cantidad}%")
print(f"Descuento por cliente frecuente: {descuento_frecuente}%")
print(f"Descuento por monto alto: {descuento_monto}%")
print(f"Descuento por promoción especial: {descuento_promocion}%")
print(f"Descuento total: {descuento_total}%")
print(f"Descuento: ${descuento_monto_total:.2f}")
print(f"Precio final: ${precio_final:.2f}")