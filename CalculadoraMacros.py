"""
Datos físicos básicos: Peso (kg), altura (cm) y edad (años). 
Género: Para ajustar la fórmula de la Tasa Metabólica Basal (TMB). 
Nivel de actividad física: Categoría que va desde sedentario hasta extremadamente activo, usada para multiplicar la TMB y obtener el Gasto Energético Total (TDEE). 
Objetivo: Definir si se busca perder grasa (déficit calórico), ganar músculo (superávit) o mantener el peso. 
Composición corporal (opcional pero recomendado): El porcentaje de grasa corporal es necesario si se utiliza la fórmula Katch-McArdle, considerada más precisa para personas con experiencia; de lo contrario, se usan Harris-Benedict o Mifflin-St Jeor.
"""
print("--- CALCULADORA INTELIGENTE DE MACROS ---")
print("Esta herramienta te ayudará a calcular tus requerimientos basados en tus datos físicos, actividad y objetivos.\n")

# 1. Recolección de datos
nombre = input("¿Cuál es tu nombre? ")
genero = input(f"Hola {nombre}, ¿Eres hombre (h) o mujer (m)? ").lower()
peso = float(input("¿Cuál es tu peso en kg?: "))
altura = float(input("¿Cuál es tu altura en cm?: "))
edad = int(input("¿Cuál es tu edad?: "))
nivel_actividad = input("Nivel de actividad (sedentario, ligero, moderado, activo (5 dias + fin de semana), muy activo): ").lower()
objetivo = input("¿Cuál es tu objetivo? (perder grasa, ganar musculo, mantener peso): ").lower()

print(f"\nProcesando los datos de {nombre}...\n")

# 2. Matemáticas compartidas: Fórmula base de Mifflin-St Jeor
tmb_base = (10 * peso) + (6.25 * altura) - (5 * edad)

# 3. El ajuste condicional (El If)
if genero == "h" or genero == "hombre":
    tmb_final = tmb_base + 5
    print("✓ Metabolismo basal calculado (Ajuste masculino).")
elif genero == "m" or genero == "mujer":
    tmb_final = tmb_base - 161
    print("✓ Metabolismo basal calculado (Ajuste femenino).")
else:
    print("Error: Género no reconocido. Por favor reinicia el programa.")
    tmb_final = 0

# 4. Cálculo del Gasto Energético Total (TDEE)
if nivel_actividad == "sedentario":
    multiplicador = 1.2
elif nivel_actividad == "ligero":
    multiplicador = 1.375
elif nivel_actividad == "moderado":
    multiplicador = 1.55   
elif nivel_actividad == "activo" or nivel_actividad == "activo (5 dias + fin de semana)":
    multiplicador = 1.725  # El ajuste exacto para rutina de fuerza constante + fin de semana dinámico
elif nivel_actividad == "muy activo":
    multiplicador = 1.9
else:
    print("Nivel de actividad no reconocido. Se usará 'sedentario' por defecto.")
    multiplicador = 1.2

tdee = tmb_final * multiplicador

# 5. Resta o suma dependiendo del objetivo 
if objetivo == "perder grasa":
    operacionObjetivo = tdee - 400
elif objetivo == "ganar musculo":
    operacionObjetivo = tdee + 300  # 300 es un superávit más limpio que 400
elif objetivo == "mantener peso":
    operacionObjetivo = tdee
else:
    print("No se reconoce ese objetivo, por defecto se usará mantenimiento.")
    operacionObjetivo = tdee

# 6. Macros totales del día 

# Proteína: 2.2g por kilo de peso (ideal para mantenimiento muscular avanzado)
gramos_proteina = peso * 2.2
calorias_proteina = gramos_proteina * 4

# Grasas: 1g por kilo de peso
gramos_grasa = peso * 1.0
calorias_grasa = gramos_grasa * 9

# Carbohidratos: El resto de las calorías para llenar el tanque de energía
calorias_restantes = operacionObjetivo - (calorias_proteina + calorias_grasa)
gramos_carbohidratos = calorias_restantes / 4

# 7. Mostrar resultados en pantalla
print("\n==========================================")
print(f"Tu Tasa Metabólica Basal (TMB) es: {tmb_final:.0f} calorías.")
print(f"Tu Gasto Energético Total (TDEE) es de: {tdee:.0f} calorías.")
print(f"Tus CALORÍAS DIARIAS DEFINITIVAS son: {operacionObjetivo:.0f} calorías.")

print("\n--- TUS MACROS TOTALES ---")
print(f"🍗 Gramos de proteína: {gramos_proteina:.0f}g")
print(f"🍚 Gramos de carbohidratos: {gramos_carbohidratos:.0f}g")
print(f"🥑 Gramos de grasas: {gramos_grasa:.0f}g")
print("==========================================")