persona = {"nombre": "laura c", "edad": 17, "ciudad": "santa marta"}

#iterar sobre claves
for clave in persona:
    print(clave) 
    
    #iterar sobre pares clave-valor
for clave, valor in persona.items():
    print(clave + ": " + str(valor)) 