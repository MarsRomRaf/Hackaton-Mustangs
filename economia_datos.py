import csv

def evaluar_estabilidad(nombre_usuario, archivo="Datos_actualizados.csv"):
    # Leer el archivo CSV
    with open(archivo, "r") as file:
        reader = csv.reader(file)
        datos = list(reader)

    # Buscar la fila que contiene el nombre del usuario
    encabezados = datos[0]  # Obtener encabezados
    nombre_columna = encabezados.index("Nombre")  # Obtener índice de la columna "Nombre"
    suma_columna = encabezados.index("suma")  # Obtener índice de la columna "suma"
    
    # Inicializar la variable de respuesta
    resultado = None

    # Recorrer los datos y encontrar el nombre del usuario
    for fila in datos[1:]:  # Saltar la fila de encabezado
        if fila[nombre_columna] == nombre_usuario:  # Comparar con el nombre del usuario
            valor_suma = int(fila[suma_columna])  # Convertir el valor de la columna "suma" a entero
            
            # Evaluar la condición de estabilidad
            if 10 <= valor_suma <= 12:
                resultado = "Estable"
            elif 6 <= valor_suma < 10:
                resultado = "Normal"
            elif valor_suma <= 5:
                resultado = "No estable"
            break  # Salir del bucle una vez encontrado el usuario

    # Retornar el resultado si se encontró el usuario, de lo contrario, indicar que no se encontró
    if resultado is not None:
        return resultado
    else:
        return "Usuario no encontrado."

# Ejemplo de uso
# resultado = evaluar_estabilidad("Nombre del Usuario")
# print(resultado)
