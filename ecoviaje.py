# Lista de excursiones
excursiones = [
    {"id": 1, "nombre": "Reserva Nacional Río Clarillo", "fecha": "2025-12-11", "cupos": 10}
]

# Mostrar excursiones disponibles
print("EXCURSIONES DISPONIBLES")
print("=" * 40)
for exc in excursiones:
    if exc["cupos"] > 0:
        print(f"{exc['id']}. {exc['nombre']} - {exc['fecha']} - {exc['cupos']} cupos)")

# Realizar resereva
print("\nREALIZAR RESERVA")
nombre = input("Ingrese su nombre: ")
id_excursion = int(input("Numero de excursion: "))        

for exc in excursiones:
    if exc["id"] == id_excursion and exc["cupos"] > 0:
        exc["cupos"] -= 1
        print(f"Reserva confirmada para {nombre} en {exc['nombre']}")
        break
else:
    print("Excursión no disponible")