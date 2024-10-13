import csv

def actualizar_datos(archivo="Datos.csv", archivo_salida="Datos_actualizados.csv"):
    # Mapeo para convertir las letras a valores numéricos
    conversion = {"A": 3, "B": 2, "C": 1}

    # Leer el archivo original
    with open(archivo, "r") as file:
        reader = csv.reader(file)
        datos = list(reader)

    # Actualizar los valores de las columnas 2 a 5 y añadir la suma
    for i in range(1, len(datos)):  # Saltar la fila de encabezado
        # Convertir las respuestas a valores numéricos
        datos[i][1] = conversion.get(datos[i][1], 0)  # Columna 2
        datos[i][2] = conversion.get(datos[i][2], 0)  # Columna 3
        datos[i][3] = conversion.get(datos[i][3], 0)  # Columna 4
        datos[i][4] = conversion.get(datos[i][4], 0)  # Columna 5
        
        # Calcular la suma de las columnas modificadas
        suma = datos[i][1] + datos[i][2] + datos[i][3] + datos[i][4]
        datos[i].append(suma)

    # Agregar el encabezado de la nueva columna "suma"
    datos[0].append("suma")

    # Guardar los datos actualizados en un nuevo archivo CSV
    with open(archivo_salida, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(datos)

# Llama a la función (opcional, descomentar si es necesario)
# actualizar_datos()
