# Solicitar datos
cantidad = int(input("Cantidad de productos: "))
precio_total = float(input("Precio total: $"))

# Calcular descuento
if cantidad > 10:
    descuento = precio_total * 0.10
    precio_final = precio_total - descuento
    print(f"\nDescuento aplicado: 10%")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Precio final: ${precio_final:.2f}")
else:
    print(f"\nSin descuento")
    print(f"Precio final: ${precio_total:.2f}")