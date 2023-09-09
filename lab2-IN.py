import pandas as pd
import random
import numpy as np
import os
import openpyxl

# Generar un arreglo de 6 elementos de texto renombrando sus índices e imprimir los datos
arreglo_texto = pd.Series(["A", "B", "C", "D", "E", "F"], index=["uno", "dos", "tres", "cuatro", "cinco", "seis"])
print("Arreglo de texto con índices personalizados:")
print(arreglo_texto)

# Generar un arreglo de 3 elementos de texto con sus 3 valores numéricos e imprimir los datos
arreglo_numerico = pd.Series([1, 2, 3], index=["a", "b", "c"])
print("\nArreglo de texto con valores numéricos:")
print(arreglo_numerico)

#  Generar un arreglo de 10 números aleatorios e imprimir diferentes segmentos de datos
arreglo_aleatorio = pd.Series([random.randint(1, 100) for _ in range(10)])
print("\nArreglo de números aleatorios:")
print(arreglo_aleatorio)

print("Primeros 5 números:")
print(arreglo_aleatorio[:5])

print("Últimos 5 números:")
print(arreglo_aleatorio[-5:])

print("2 primeros números:")
print(arreglo_aleatorio[:2])

print("2 últimos números:")
print(arreglo_aleatorio[-2:])

# Generar un DataFrame con 6 elementos de texto con sus respectivos valores numéricos e imprimir los datos
data = {"Texto": ["A", "B", "C", "D", "E", "F"], "Valor": [1, 2, 3, 4, 5, 6]}
df = pd.DataFrame(data)
print("\nDataFrame con columnas cambiadas:")
print(df)

# Verificar si el archivo "Ventas.csv" ya existe antes de crearlo
if not os.path.exists("Ventas.csv"):
    # Crear el archivo "Ventas.csv" solo si no existe
    datos_ventas = {
        "Producto": ["Producto A", "Producto B", "Producto C"],
        "Ventas_Enero": [100, 150, 200],
        "Ventas_Febrero": [120, 160, 210],
        "Ventas_Marzo": [130, 155, 220]
    }

    ventas = pd.DataFrame(datos_ventas)
    ventas.to_csv("Ventas.csv", index=False)

# Leer el archivo "Ventas.csv"
ventas = pd.read_csv("Ventas.csv")
print("\nDatos del archivo Ventas.csv:")
print(ventas)

# Generar un arreglo con las ventas del primer trimestre del año e imprimir los datos
ventas_primer_trimestre = ventas[["Ventas_Enero", "Ventas_Febrero", "Ventas_Marzo"]]
print("\nVentas del primer trimestre del año:")
print(ventas_primer_trimestre)

# Imprimir el número de registros y el número de campos
num_registros, num_campos = ventas.shape
print(f"\nNúmero de registros: {num_registros}")
print(f"Número de campos: {num_campos}")

# Generar un arreglo numérico con las ventas del primer trimestre del año e imprimir estadísticas
ventas_primer_trimestre_array = ventas_primer_trimestre.values.flatten()
print("\nArreglo numérico con las ventas del primer trimestre del año:")
print(ventas_primer_trimestre_array)

media = ventas_primer_trimestre_array.mean()
correlacion = ventas_primer_trimestre.corr().iloc[0, 1]
valor_minimo = ventas_primer_trimestre_array.min()
valor_maximo = ventas_primer_trimestre_array.max()
mediana = np.median(ventas_primer_trimestre_array)
desviacion_estandar = ventas_primer_trimestre_array.std()

print(f"Media: {media}")
print(f"Correlación: {correlacion}")
print(f"Valor mínimo: {valor_minimo}")
print(f"Valor máximo: {valor_maximo}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion_estandar}")

print("\nSolo la primera columna del dataset:")
print(ventas["Ventas_Enero"])

print("\nLas 2 primeras columnas:")
print(ventas[["Ventas_Enero", "Ventas_Febrero"]])

print("\nPrimera fila y última columna:")
print(ventas.iloc[0, -1])

print("\nValores de la primera fila:")
print(ventas.iloc[0])

# Crear un archivo Excel "Ventas02.xlsx" y luego leerlo
datos_ventas_excel = {
    "Producto": ["Producto X", "Producto Y", "Producto Z"],
    "Ventas_Enero": [90, 120, 180],
    "Ventas_Febrero": [110, 145, 190],
    "Ventas_Marzo": [120, 155, 200]
}

ventas_excel_df = pd.DataFrame(datos_ventas_excel)

# Guardar el DataFrame en un archivo Excel "Ventas02.xlsx" sin el índice
ventas_excel_df.to_excel("Ventas02.xlsx", index=False)

# Leer el archivo Excel "Ventas02.xlsx" sin la primera fila (encabezado)
ventas_excel = pd.read_excel("Ventas02.xlsx", header=None, skiprows=[0])
print("\nDatos del archivo Excel Ventas02.xlsx (sin encabezado):")
print(ventas_excel)
