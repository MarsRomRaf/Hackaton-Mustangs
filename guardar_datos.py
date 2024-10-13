import csv

def guardar_datos(nombre, respuesta1, respuesta2, respuesta3, respuesta4, archivo="Datos.csv"):
    # Verificar si el archivo ya existe
    try:
        with open(archivo, "x", newline="") as file:
            # Crear el archivo con los encabezados de las columnas si no existe
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"])
    except FileExistsError:
        pass  # El archivo ya existe, no es necesario crear los encabezados

    # Escribir los datos en la siguiente fila disponible en el archivo CSV
    with open(archivo, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nombre, respuesta1, respuesta2, respuesta3, respuesta4])
