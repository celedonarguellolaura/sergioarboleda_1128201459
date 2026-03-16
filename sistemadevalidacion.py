# 1. Validar cédula
def validar_cedula(cedula):
    return cedula.isdigit() and 8 <= len(cedula) <= 10


# 2. Validar email
def validar_email(email):
    if "@" in email and "." in email:
        partes = email.split("@")
        if len(partes) == 2 and partes[1].endswith(".com"):
            return True
    return False


# 3. Validar calificaciones
def validar_calificaciones(calificaciones):
    for c in calificaciones:
        if c < 0 or c > 5:
            return False
    return True


# 5. Calcular promedio
def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    return round(promedio, 2)


# 4. Crear estudiante
def crear_estudiante(cedula, nombre, email, calificaciones):

    if not validar_cedula(cedula):
        print("Cédula inválida.")
        return None

    if not validar_email(email):
        print("Email inválido.")
        return None

    if not validar_calificaciones(calificaciones):
        print("Calificaciones inválidas.")
        return None

    promedio = calcular_promedio(calificaciones)

    estudiante = {
        "cedula": cedula,
        "nombre": nombre,
        "email": email,
        "promedio": promedio
    }

    return estudiante


# 6. Clasificar desempeño
def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Satisfactorio"
    else:
        return "Necesita mejorar"


# 7. Listar estudiantes
def listar_estudiantes(lista_estudiantes):

    if len(lista_estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    print("\nCédula    | Nombre        | Promedio | Desempeño")

    for e in lista_estudiantes:
        desempeño = clasificar_desempeño(e["promedio"])
        print(f'{e["cedula"]} | {e["nombre"]} | {e["promedio"]} | {desempeño}')


# Buscar estudiante
def buscar_estudiante(lista_estudiantes, cedula):
    for e in lista_estudiantes:
        if e["cedula"] == cedula:
            desempeño = clasificar_desempeño(e["promedio"])
            print(f'{e["nombre"]} | Promedio: {e["promedio"]} | Desempeño: {desempeño}')
            return

    print("Estudiante no encontrado.")


# 8. Función principal
def main():

    estudiantes = []

    while True:

        print("\n--- SISTEMA DE GESTIÓN DE ESTUDIANTES ---")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Buscar estudiante por cédula")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":

            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            email = input("Email: ")

            notas = input("Calificaciones (separadas por coma): ")
            calificaciones = [float(n) for n in notas.split(",")]

            estudiante = crear_estudiante(cedula, nombre, email, calificaciones)

            if estudiante:
                estudiantes.append(estudiante)
                desempeño = clasificar_desempeño(estudiante["promedio"])
                print(f'Estudiante agregado exitosamente. Promedio: {estudiante["promedio"]} | Desempeño: {desempeño}')

        elif opcion == "2":
            listar_estudiantes(estudiantes)

        elif opcion == "3":
            cedula = input("Cédula a buscar: ")
            buscar_estudiante(estudiantes, cedula)

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


# Ejecutar programa
main()