import math

# 1. Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

# 2. Función para calcular la hipotenusa
def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    return hipotenusa

# 3. Función para calcular potencia
def calcular_potencia(base, exponente):
    potencia = math.pow(base, exponente)
    return potencia

# 4. Función principal con menú
def main():
    while True:
        print("\n--- CALCULADORA CIENTÍFICA ---")
        print("1. Calcular área de círculo")
        print("2. Calcular hipotenusa")
        print("3. Calcular potencia")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            radio = float(input("Ingresa el radio: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es {area:.2f}")

        elif opcion == "2":
            cateto1 = float(input("Ingresa el primer cateto: "))
            cateto2 = float(input("Ingresa el segundo cateto: "))
            hip = calcular_hipotenusa(cateto1, cateto2)
            print(f"La hipotenusa es {hip:.2f}")

        elif opcion == "3":
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            resultado = calcular_potencia(base, exponente)
            print(f"El resultado es {resultado:.2f}")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
main()