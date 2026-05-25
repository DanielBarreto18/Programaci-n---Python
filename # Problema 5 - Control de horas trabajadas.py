# Problema 5 - Control de horas trabajadas

# Matriz con los recursos y horas trabajadas de lunes a viernes
# [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]

recursos = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["Ana", 7, 8, 8, 7, 8],
    ["Luis", 9, 10, 9, 8, 9],
    ["María", 6, 7, 8, 7, 6]
]

# Función para calcular total de horas y clasificación
def calcular_horas(datos_recurso):
    nombre = datos_recurso[0]

    # Suma de horas trabajadas
    total_horas = sum(datos_recurso[1:])

    # Clasificación de la jornada
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion


# Mostrar resultados
print("REPORTE SEMANAL DE HORAS TRABAJADAS\n")

for recurso in recursos:
    nombre, total, clasificacion = calcular_horas(recurso)

    print("Nombre:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)
    print("-----------------------------")