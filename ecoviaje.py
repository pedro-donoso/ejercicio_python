# Lista de excursiones
excursiones = [
    {"id": 1, "nombre": "Reserva Nacional Río Clarillo", "fecha": "2025-12-11", "cupo_maximo": 20, "cupo_disponible": 10}
]

def mostrar_excursiones_disponibles():
    print("Excursiones ecológicas disponibles")
    print("=" * 50)

    excursiones_disponibles = []
    for excursion in excursiones:
        if excursion["cupo_disponible"] > 0:
            excursiones_disponibles.append(excursion)

    if len(excursiones_disponibles) == 0:
        print("No hay excursiones disponibles en este momento.")
    else:
        for excursion in excursiones_disponibles:
            print(f"ID: {excursion['id']}")
            print(f"Nombre: {excursion['nombre']}")
            print(f"Fecha: {excursion['fecha']}")
            print(f"Cupos disponibles: {excursion['cupo_disponible']}/{excursion['cupo_maximo']}")
            print("-" * 30)

mostrar_excursiones_disponibles()