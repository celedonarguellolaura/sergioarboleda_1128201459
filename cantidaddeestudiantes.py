estudiantes = ["shayla", "María", "lianna", "valery", "valerie", "adrina", "marcos", "juan", "xavi", "camilo",]

# agregar un nuevo estudiante a la lista
estudiantes.append("maria")
print(estudiantes) # ['shayla', 'María', 'lianna', 'valery', 'valerie', 'adrina', 'marcos', 'juan', 'xavi', 'camilo', 'maria', 'eduiw']

#  obtener la cantidad de estudiantes en la lista
print(len(estudiantes)) # 11

#buscar si un estudiante en la lista
if "marcos" in estudiantes:
    print("marcos esta en la lista de estudiantes") 
    
    # eliminar un estudiante por nombre
estudiantes.remove("marcos")
print(estudiantes) # ['shayla', 'María', 'lianna', 'valery', 'valerie', 'adrina', 'juan', 'xavi', 'camilo', 'maria', 'eduiw']