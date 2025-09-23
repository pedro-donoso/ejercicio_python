# Programa que imprime todos los números enteros del 0 al 100

print("Números enteros del 0 al 100:")
print("-" * 30)

# Bucle for que imprime números del 0 al 100 (inclusive)
for numero in range(101):
    print(numero)

print("-" * 30)
print("¡Bucle completado!")

print("\n" + "=" * 50)

# Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
print("Múltiples de 2 entre 2 y 500:")
print("-" * 30)

# Bucle for que imprime múltiplos de 2 del 2 al 500 (inclusive)
for numero in range(2, 501, 2):
    print(numero)

print("-" * 30)
print(f"¡Múltiples de 2 completados! Total: {(500-2)//2 + 1} números")

# Contando Vanilla Ice: números del 1 al 100 con reglas especiales
print("Contando Vanilla Ice (1 al 100):")
print("-" * 30)

# Bucle for que imprime números del 1 al 100 con reglas especiales
for numero in range(1, 101):
    if numero % 10 == 0: #Si es divisible por 10
        print("baby")
    elif numero % 5 == 0: #Si es divisible por 5 (pero no por 10)
        print("ice ice")
    else: #Si no es divisible por 5
        print(numero)

print("-" * 30)
print("¡Contando Vanilla Ice completado!")