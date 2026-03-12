import random

# Definir los caracteres disponibles
mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'
numeros = '0123456789'
especiales = '!@#$%'

# Combinar todos los caracteres
todos_caracteres = mayusculas + minusculas + numeros + especiales

# Función para generar la contraseña
def generar_contrasena(longitud):
    contrasena = ''
    for _ in range(longitud):
        contrasena += random.choice(todos_caracteres)
    return contrasena

# Bucle principal
while True:
    # Pedir la longitud de la contraseña
    try:
        longitud = int(input("Ingresa la longitud de la contraseña (entre 8 y 20): "))
        if 8 <= longitud <= 20:
            # Generar y mostrar la contraseña
            contrasena = generar_contrasena(longitud)
            print(f"Contraseña generada: {contrasena}")
            
            # Preguntar si quiere otra
            respuesta = input("¿Quieres generar otra contraseña? (s/n): ").lower()
            if respuesta == 'n':
                print("¡Hasta luego!")
                break
            elif respuesta != 's':
                print("Respuesta no válida. Asumiendo 's' para continuar.")
        else:
            print("Error: La longitud debe estar entre 8 y 20 caracteres.")
    except ValueError:
        print("Error: Ingresa un número válido.")
