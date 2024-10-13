Read.me
Mustangs - 23
Hackathon Banorte 2024

## Nota
Los archivos se encuentran en un drive y se envío el link, debido al peso de la carpeta.

Este proyecto es una aplicación web que proporciona educación financiera a los usuarios mediante la utilización de la inteligencia artificial. Utiliza Streamlit para la interfaz de usuario y LangChain con Google Generative AI para el procesamiento del lenguaje natural.

La aplicación permite a los usuarios realizar preguntas sobre finanzas, obtener recomendaciones personalizadas basadas en sus patrones de consumo, y recibir estrategias financieras para mejorar su situación económica. Además, permite a los usuarios registrar sus datos y evaluar su estabilidad financiera.

## Tecnologías Utilizadas

- **Streamlit**: Para crear la interfaz de usuario.
- **LangChain**: Para integrar modelos de lenguaje generativos.
- **Google Generative AI**: Para procesar y generar respuestas a preguntas financieras.
- **Pandas**: Para la manipulación y análisis de datos en formato CSV.

## Requisitos

Asegúrate de tener instalado Python y las siguientes librerías:

```bash
pip install streamlit langchain langchain-google-generai pandas
```

## Configuración

1. **API Key de Google Gemini**: 
   - Reemplaza el valor de `gemini_api_key` en el código con tu clave de API válida.

2. **Datos de Entrada**:
   - Asegúrate de tener un archivo `Libro1.csv` que contenga datos sobre clientes y sus patrones de consumo.

## Ejecución

Para ejecutar la aplicación, navega al directorio del proyecto y ejecuta el siguiente comando:

```bash
streamlit run app.py
```
Donde `app.py` es el nombre del archivo que contiene el código de la aplicación.

## Funcionalidades

- Consulta Financiera: Los usuarios pueden hacer preguntas sobre finanzas personales y recibir respuestas generadas por el modelo de IA.
- Análisis de Patrones de Consumo: La aplicación analiza los datos del cliente para identificar categorías de consumo populares y sugiere promociones basadas en esos datos.
- Recomendaciones Personalizadas: Los usuarios reciben consejos financieros personalizados según su categoría de consumo más popular.
- Registro de Datos: Los usuarios pueden registrar su información financiera, que se guarda y actualiza para análisis futuros.
- Evaluación de Estabilidad Financiera: La aplicación evalúa la estabilidad financiera del usuario y sugiere estrategias financieras adecuadas.

## Archivos Importantes

- `guardar_datos.py`: Subrutina para guardar las respuestas del usuario.
- `actualizar_datos.py`: Subrutina para actualizar los datos en el sistema.
- `economia_datos.py`: Subrutina para evaluar la estabilidad financiera del usuario.