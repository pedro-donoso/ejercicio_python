# Lista de excursiones
excursiones = [
    {
        "id": 1,
        "nombre": "Reserva Nacional Río Clarillo",
        "fecha": "2025-12-11",
        "cupos": 10,
    }
]

# Mostrar excursiones disponibles
print("EXCURSIONES DISPONIBLES")
print('=' * 40)
for exc in excursiones:
    if exc['cupos'] > 0:
        print(
            f"{exc['id']}. {exc['nombre']} - {exc['fecha']} - "
            f"{exc['cupos']} cupos"
        )

# Realizar resereva
print("\nREALIZAR RESERVA")
nombre = input("Ingrese su nombre: ")

try:
    id_excursion = int(input("Número de excursión: "))

    # Buscar la excursión
    excursion_encontrada = None
    for exc in excursiones:
        if exc['id'] == id_excursion:
            excursion_encontrada = exc
            break

    if excursion_encontrada is None:
            print("Número de excursión no válido")
    elif excursion_encontrada['cupos'] <= 0:
            print("No hay cupos disponibles para esta excursión")
    else:
            # Confirmar reserva antes de realizarla
            print(f"\nExcursión: {excursion_encontrada['nombre']}")
            print(f"Fecha: {excursion_encontrada['fecha']}")
            print(f"Cupos disponibles: {excursion_encontrada['cupos']}")

            confirmacion = input("¿Desea confirmar su reserva? (s/n): ").lower()

            if confirmacion == 's' or confirmacion == 'si':
                excursion_encontrada['cupos'] -= 1
                print(f"Reserva confirmada para {nombre}")
                print(f"Cupos restantes: {excursion_encontrada['cupos']}")
            else:
                print("Reserva cancelada")

except ValueError:
    print("Por favor ingrese un número válido")
