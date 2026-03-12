# Programa de análisis de números
# Este programa pide números al usuario uno por uno hasta que ingrese 0,
# luego calcula y muestra estadísticas de los números ingresados.

# Inicialización de variables
contador = 0
suma = 0
numero_mayor = None
numero_menor = None
pares = 0
impares = 0

print("Ingrese números uno por uno. Ingrese 0 para terminar.")

while True:
    try:
        numero = int(input("Ingrese un número: "))
        if numero == 0:
            break
        # Actualizar contador y suma
        contador += 1
        suma += numero
        # Actualizar mayor y menor
        if numero_mayor is None or numero > numero_mayor:
            numero_mayor = numero
        if numero_menor is None or numero < numero_menor:
            numero_menor = numero
        # Contar pares e impares
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Mostrar resultados
if contador > 0:
    promedio = suma / contador
    print(f"\nCantidad total de números ingresados: {contador}")
    print(f"Suma de todos los números: {suma}")
    print(f"Promedio de los números: {promedio:.2f}")
    print(f"Número mayor: {numero_mayor}")
    print(f"Número menor: {numero_menor}")
    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")
else:
    print("\nNo se ingresaron números válidos antes de 0.")
