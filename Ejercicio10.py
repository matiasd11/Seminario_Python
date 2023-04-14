nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#Inciso A
nombres = nombres.replace("'", "").split(",")

def dicc_nombre_notas():
    """Devuelve un diccionario con ambas notas de cada alumno como value y el nombre como key"""
    count = 0
    dicc = {}
    for i in nombres:
        dicc[i] = (notas_1[count], notas_2[count])
        count+=1
    return dicc

estudiantes = dicc_nombre_notas()
print(estudiantes)

#Inciso B

def calcular_promedio_estudiantes():
    """Calcula el promedio de todos los estudiantes y los devuelve en un diccionario con los nombres como keys y las notas promedio como values"""
    promedios = {}
    for alumno in estudiantes:
        promedio = (estudiantes[alumno][0] + estudiantes[alumno][1])/2
        promedios[alumno] = promedio
    return promedios

promedios = calcular_promedio_estudiantes()
print(promedios)


#Inciso C
def calcular_promedio_general():
    """Calcula y devuelve el promedio general de todos los alumnos y los devuelve como float"""
    promedio_gral = sum(promedios.values())/len(promedios)
    return promedio_gral

print(f"Promedio General: {round(calcular_promedio_general(),2)}")

#Inciso D
def max_alumno_nota_promedio():
    """Imprime el alumno con mayor nota y la nota, para ello tiene que acceder al diccionario de promedios"""
    alumno_max = max(promedios, key=lambda x: promedios[x])
    print(f"Alumno con mayor nota promedio: {alumno_max}, Nota: {promedios[alumno_max]}")

max_alumno_nota_promedio()


#Inciso E
def min_nota_alumno():
    """Imprime el alumno con la nota mas baja y la nota, comparando entre las dos notas de cada alumno"""
    alumno_min = min(estudiantes, key = lambda x: min(estudiantes[x]))
    nota_min = min(estudiantes[alumno_min])
    print(f"Alumno con nota Minima: {alumno_min}, Nota: {nota_min}")
    
min_nota_alumno()

