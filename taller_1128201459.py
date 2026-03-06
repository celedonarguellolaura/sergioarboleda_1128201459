edad=25
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

    #Bucle
for i in range(5):
    print("hola mundo")

#bucle while
contador = 1

while contador <= 5:
    print("numero:"+str(contador))
    contador = contador + 1
    
for i in range(5):
    print("numero:"+str(i))

for i in range(0, 12, 3):
    print("numero:"+str(i))
    
encontrado = False
numerobuscado = 7
numeros = [1, 3, 5, 7, 9]
for numero in numeros:
    if numero == numerobuscado:
        encontrado = True
        break
print   ("Número", numerobuscado, "encontrado:", encontrado)

for i in range(3):
    for j in range(1,4):
        print("i="+str(i)+" j="+str(j))
