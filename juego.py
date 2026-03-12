import random

opciones = ['piedra', 'papel', 'tijera']
victorias_usuario = 0
victorias_maquina = 0

while True:
    usuario = input("Elige piedra, papel o tijera: ").lower()
    while usuario not in opciones:
        usuario = input("Opción inválida. Elige piedra, papel o tijera: ").lower()
    
    maquina = random.choice(opciones)
    
    print(f"Tú elegiste: {usuario}")
    print(f"La máquina eligió: {maquina}")
    
    if usuario == maquina:
        resultado = "Empate"
    elif (usuario == 'piedra' and maquina == 'tijera') or \
         (usuario == 'tijera' and maquina == 'papel') or \
         (usuario == 'papel' and maquina == 'piedra'):
        resultado = "¡Ganaste!"
        victorias_usuario += 1
    else:
        resultado = "Perdiste"
        victorias_maquina += 1
    
    print(resultado)
    print(f"Marcador - Tú: {victorias_usuario} | Máquina: {victorias_maquina}")
    
    jugar_otra = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_otra != 's':
        break
