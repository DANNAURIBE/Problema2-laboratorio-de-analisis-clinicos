# -----------------------------------------------------
# Nombre del estudiante: Danna Valeria Uribe Santiago
# Grupo: 213022_270
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia
# -----------------------------------------------------

# Programa para determinar si una persona tiene anemia
# según edad, sexo y nivel de hemoglobina.

print("=== Diagnóstico de Anemia ===")

edad = float(input("Ingrese la edad: "))
unidad = input("¿La edad está en meses o años?: ").lower()
sexo = input("Ingrese el sexo (M/F): ")
hemoglobina = float(input("Ingrese el nivel de hemoglobina (g/dL): "))

# Determinar rango según edad, unidad y sexo
if unidad == "meses":
    if edad <= 1:
        rango = (13.0, 26.0)
    elif edad <= 6:
        rango = (10.0, 18.0)
    elif edad <= 12:
        rango = (11.0, 15.0)
    else:
        print("Edad no válida en meses")
        exit()

elif unidad == "años":
    if 1 < edad <= 5:
        rango = (11.5, 15.0)
    elif 5 < edad <= 10:
        rango = (12.6, 15.5)
    elif 10 < edad <= 15:
        rango = (13.0, 15.5)
    elif edad > 15:
        if sexo.lower() == "f":
            rango = (12.0, 16.0)
        elif sexo.lower() == "m":
            rango = (14.0, 18.0)
        else:
            print("Sexo no válido")
            exit()
    else:
        print("Edad no válida")
        exit()
else:
    print("Unidad no válida")
    exit()

# Comparar hemoglobina con el rango
if hemoglobina < rango[0]:
    resultado = "Positivo (tiene anemia)"
else:
    resultado = "Negativo (no tiene anemia)"

print("Resultado del análisis:", resultado)

"""  danna Uriebe Santiago"""

# -----------------------------------------------------
# Tabla de referencia de hemoglobina (g/dL)
#
# Grupo de edad/sexo        | Rango referencia | Mínimo
# -----------------------------------------------------
# 0 – 1 mes                 | 13.0 – 26.0      | 13.0
# >1 y ≤6 meses             | 10.0 – 18.0      | 10.0
# >6 y ≤12 meses            | 11.0 – 15.0      | 11.0
# >1 y ≤5 años              | 11.5 – 15.0      | 11.5
# >5 y ≤10 años             | 12.6 – 15.5      | 12.6
# >10 y ≤15 años            | 13.0 – 15.5      | 13.0
# Mujeres >15 años          | 12.0 – 16.0      | 12.0
# Hombres >15 años          | 14.0 – 18.0      | 14.0
# -----------------------------------------------------
