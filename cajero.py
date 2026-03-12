saldo = 1000

while True:
    print("Menú:")
    print("1. Ver saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Su saldo actual es: {saldo}")
    elif opcion == "2":
        monto = float(input("Ingrese el monto a depositar: "))
        saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: {saldo}")
    elif opcion == "3":
        monto = float(input("Ingrese el monto a retirar: "))
        if monto <= saldo:
            saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {saldo}")
        else:
            print("Saldo insuficiente.")
    elif opcion == "4":
        print("Gracias por usar el cajero.")
        break
    else:
        print("Opción inválida. Intente de nuevo.")