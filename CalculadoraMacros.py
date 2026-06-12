"""
Datos físicos básicos: Peso (kg), altura (cm) y edad (años). 
Género: Para ajustar la fórmula de la Tasa Metabólica Basal (TMB). 
Nivel de actividad física: Categoría que va desde sedentario hasta extremadamente activo, usada para multiplicar la TMB y obtener el Gasto Energético Total (TDEE). 
Objetivo: Definir si se busca perder grasa (déficit calórico), ganar músculo (superávit) o mantener el peso. 
Composición corporal (opcional pero recomendado): El porcentaje de grasa corporal es necesario si se utiliza la fórmula Katch-McArdle, considerada más precisa para personas con experiencia; de lo contrario, se usan Harris-Benedict o Mifflin-St Jeor.
"""
print("--- CALCULADORA INTELIGENTE DE MACROS ---")
print("Esta herramienta te ayudará a calcular tus requerimientos basados en tus datos físicos, actividad y objetivos.\n")

#1. Recolección de datos (Todo en un solo bloque)
nombre = input(" ¿Cúal es tu nombre? ")
genero = input(f"Hola {nombre}, ¿Eres hombre (h) o mujer (m)? ").lower()
peso = float(input("¿Cuál es tu peso en kg? :  "))
altura = float(input("¿Cúal es tu altura en cm?: "))
edad = float(input("¿Cúal es tu edad?: "))
nivel_actividad = input("¿Cúal es tu nivel de actividad física? (sedentario, ligero, activo, muy activo): ").lower()
objetivo = input("¿Cúal es tu objetivo? (perder grasa, ganar músculo, mantener peso): ").lower()

print(f"\nProcesando los tados de {nombre}...\n")

#2. Matemáticas compartidas: Fórmula base de Mifflin-StJeor
tmb_base = (10 * peso) + (6.25 * altura) - (5 * edad)

#3. El ajuste condicional (El If)
if genero == "h" or genero == "hombre":
    tmb_final = tmb_base + 5
    print("Metabloismo basal calculado (Ajuste masculino).")
    
elif genero == "m" or genero == "mujer":
    tmb_final = tmb_base - 161
    print("Metabolismo basal calculado (Ajuste femenino).")

else:
    print("Error: Género no reconocido. Porfavor reinicia el programa.")
    tmb_final = 0

# 4. Cálculo del Gasto Energético Total (TDEE)
if nivel_actividad == "sedentario":
    multiplicador = 1.2
elif nivel_actividad == "ligero":
    multiplicador = 1.375
elif nivel_actividad == "moderado":
    multiplicador = "activo"
elif nivel_actividad == "muy activo":
    multiplicador = 1.9
else:
    print("Nivel de actividad no reconocido. Se usará 'sedentario' por defecto.")
    multiplicador = 1.2

#Calculamos el TDEE multiplicando la caja anterior por el nuevo factor
tdee = tmb_final * multiplicador

#5. Resta o suma dependiendo del objetivo (Subir peso + 400, mantenimiento 0, bajar peso - 400)
if objetivo == "perder grasa":
    operacionObjetivo = tdee - 400
elif objetivo == "ganar musculo":
    operacionObjetivo = tdee + 400
elif objetivo == "mantener peso":
    operacionObjetivo = tdee
else:
    print("No se reconoce ese objetivo por defecto se usara mantenimiento")
    operacionObjetivo = tdee


#Mostramos el primer resultado en pantalla
print(f"Tu tasa metabólica basal (TMB) es: {tmb_final} calorías.")
print("\nCalculo de tdee")
print(f"Tu gasto Energético total (TDEE) es de: {tdee:.2f} calorías.")
print("\nTus calorias finales:")
print(f"Tus calorias diarias serian: {operacionObjetivo:.2f} calorías.")