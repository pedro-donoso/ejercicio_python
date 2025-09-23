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

print("\n" + "=" * 50)

# Wow. Número gigante a la vista: suma de números pares del 0 al 500,000
print("Wow. Número gigante a la vista:")
print("Sumando números pares del 0 al 500,000...")
print("-" * 50)

# Inicializar la suma
suma_pares = 0
contador_pares = 0

# Bucle for que suma todos los números pares del 0 al 500,000
print("Calculando... (esto puede tomar unos segundos)")
for numero in range(0, 500001, 2): #Rango con paso de 2 para solo números pares
    suma_pares += numero
    contador_pares += 1

# Mostrar los resultados
print(f"Números pares sumados: {contador_pares:,}")
print(f"Suma total de números pares del 0 al 500,000:")
print(f"{suma_pares:,}")
print("-" * 50)
print("¡Número gigante completado!")
