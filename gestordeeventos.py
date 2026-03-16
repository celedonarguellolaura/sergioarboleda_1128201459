import datetime

# 1. Crear evento
def crear_evento(nombre, dia, mes, año):
    fecha = datetime.date(año, mes, dia)
    evento = {"nombre": nombre, "fecha": fecha}
    return evento

# 2. Calcular días hasta el evento
def dias_hasta_evento(fecha_evento):
    hoy = datetime.date.today()
    diferencia = fecha_evento - hoy
    return diferencia.days

# 3. Verificar si el evento ya pasó
def evento_pasado(fecha_evento):
    hoy = datetime.date.today()
    return fecha_evento < hoy

# 4. Función principal
def main():
    nombre = input("Nombre del evento: ")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))

    evento = crear_evento(nombre, dia, mes, año)
    fecha_evento = evento["fecha"]

    dias = dias_hasta_evento(fecha_evento)

    if evento_pasado(fecha_evento):
        print(f"El evento ya pasó. Fue hace {abs(dias)} días.")
    elif dias > 0:
        print(f"Faltan {dias} días para tu evento.")
    else:
        print("¡El evento es hoy!")

# Ejecutar el programa
main()