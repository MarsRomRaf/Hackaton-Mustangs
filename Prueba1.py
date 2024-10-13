#"AIzaSyB9aQGfOu65yQxlqL16MYb0GC6V1n1Ufh0"
import streamlit as st
import pandas as pd
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from guardar_datos import guardar_datos  # Importa la subrutina para guardar datos
from actualizar_datos import actualizar_datos  # Importa la subrutina para actualizar datos
from economia_datos import evaluar_estabilidad  # Importa la subrutina para evaluar estabilidad

# Configura tu API Key de Gemini
gemini_api_key = "AIzaSyCjZYzsH_l12nfZclUyqMzPZTqD_JwWkMs"  # Reemplaza con tu API Key válida

# Crea un modelo de lenguaje usando LangChain con Gemini
llm = GoogleGenerativeAI(api_key=gemini_api_key, model="gemini-1.5-pro")

# Define el prompt para la conversación
prompt_template = PromptTemplate(
    input_variables=["user_input"],
    template="Eres un asesor financiero que va a ayudar al usuario mediante educación financiera a mejorar sus finanzas. El usuario dice: {user_input}. ¿Cómo responderías?"
)

# Define un nuevo prompt para estrategias financieras
strategy_prompt_template = PromptTemplate(
    input_variables=["evaluation_result"],
    template="Basado en el siguiente resultado de evaluación de estabilidad económica: {evaluation_result}, ¿qué estrategia financiera recomendarías al usuario?"
)

# Define un nuevo prompt para consejos personalizados
advice_prompt_template = PromptTemplate(
    input_variables=["categoria"],
    template="Eres un asesor financiero. El usuario tiene una categoría popular en sus compras: {categoria}. ¿Qué consejos financieros personalizados le darías para manejar mejor sus finanzas en esta categoría?"
)

parser = StrOutputParser()

# Crea una cadena de lenguaje con el modelo y el prompt
chain = LLMChain(llm=llm, prompt=prompt_template)

# Subrutina para ocultar preguntas
def boton_esconder():
    st.session_state.show_questions = False  # Cambia el estado para no mostrar preguntas

# Función para analizar los patrones de consumo por categorías o giros comerciales
def analizar_patrones(df):
    if 'Categoria' in df.columns:
        # Agrupar los productos por categoría y contar las compras
        categoria_popular = df['Categoria'].value_counts().idxmax()
        return categoria_popular
    else:
        st.write("La columna 'Categoria' no está presente en los datos.")
        return None

# Generar una promoción basada en la categoría popular
def generar_promocion(categoria):
    promociones = {
        'Electrónica': "10% de descuento en accesorios de electrónica.",
        'Ropa': "Compra 2 y lleva 1 gratis en artículos de ropa.",
        'Alimentos': "20% de descuento en alimentos saludables.",
        'Hogar': "15% de descuento en productos para el hogar.",
        'Deportes': "30% de descuento en ropa deportiva."
    }
    return promociones.get(categoria, "Promoción especial: 5% de descuento en todos los productos.")

# Interfaz de Streamlit
st.image("banorte.png", use_column_width=True)
st.title("Educación Financiera")
st.write("¡Bienvenido a tu educación financiera virtual!")

# Pregunta adicional para hacer dudas
user_question = st.text_input("¿Tienes alguna duda? Pregúntame:")
if user_question:
    question_chain = LLMChain(llm=llm, prompt=prompt_template)
    answer = question_chain.run(user_input=user_question)
    st.write("Respuesta:", answer)

# Cargar los datos del archivo CSV
archivo='/users/maria/chatbot/Libro1.csv'
df = pd.read_csv(archivo)

# Mostrar las columnas disponibles para verificar el archivo
#st.write("Columnas en el archivo CSV:", df.columns)

# Memoria para almacenar la respuesta inicial del usuario
if "user_data" not in st.session_state:
    st.session_state.user_data = {"is_client": None, "name": None, "client_number": None}
if "show_questions" not in st.session_state:
    st.session_state.show_questions = True  # Inicializa para mostrar preguntas

# Pregunta inicial: ¿Eres cliente?
is_client = st.radio("¿Eres cliente?", ("Sí", "No"))
st.session_state.user_data["is_client"] = is_client

# Mostrar opciones en función de la respuesta del usuario
if st.session_state.user_data["is_client"] == "Sí":
    # Solicitar el número de cliente
    client_number = st.text_input("Por favor, ingresa tu número de cliente:")
    st.session_state.user_data["client_number"] = client_number
    
    # Verificar si el número de cliente está en los datos
    if client_number:
        cliente_data = df[df['Num. Cliente'] == int(client_number)]
        if not cliente_data.empty:
            st.write("Gracias por proporcionar tu número de cliente.")
            
            # Analizar patrones de consumo del cliente
            categoria_popular = analizar_patrones(cliente_data)
            if categoria_popular:
                promocion = generar_promocion(categoria_popular)
                
                # Mostrar la promoción sugerida
                st.write(f"Categoría más popular en tus compras: {categoria_popular}")
                st.write(f"Promoción sugerida: {promocion}")

                # Obtener consejos personalizados según la categoría
                advice_chain = LLMChain(llm=llm, prompt=advice_prompt_template)
                financial_advice = advice_chain.run(categoria=categoria_popular)
                
                # Mostrar los consejos financieros personalizados
                st.write("Consejos financieros personalizados:")
                st.write(financial_advice)

            else:
                st.write("No se pudo determinar la categoría más popular.")
                
        else:
            st.write("Número de cliente no encontrado.")
elif st.session_state.user_data["is_client"] == "No":
    # Solicitar el nombre del usuario
    new_user_name = st.text_input("Por favor, ingresa tu nombre:")
    st.session_state.user_data["name"] = new_user_name
    
    # Verificar que el nombre ha sido proporcionado
    if new_user_name:
        st.write(f"Hola {new_user_name}, gracias por registrarte.")
        
        # Mostrar preguntas solo si show_questions es True
        if st.session_state.show_questions:
            # Preguntas con opciones múltiples
            monthly_income = st.selectbox("1. ¿Cuáles son tus ingresos mensuales?", 
                                          ["A) Menor de $10,000", 
                                           "B) Entre $10,000 a $30,000", 
                                           "C) Mayor a $30,000"])
            
            debt_percentage = st.selectbox("2. ¿Qué porcentaje de tus ingresos ocupas para pagar tus deudas?", 
                                           ["A) 50% o más", 
                                            "B) Entre 20% y 49%", 
                                            "C) Menor al 20%"])
            
            credit_experience = st.selectbox("3. ¿Cómo ha sido tu experiencia con los créditos?", 
                                             ["A) Historial con atrasos frecuentes o impagos", 
                                              "B) Historial con algunos retrasos, pero sin impagos significativos", 
                                              "C) Historial sin atrasos y pagos puntuales"])
            
            savings_investments = st.selectbox("4. ¿Tienes ahorros o inversiones y cuántos meses cubrirían tus gastos fijos?", 
                                               ["A) No tiene ahorros", 
                                                "B) Ahorros que cubren 3 y 6 meses de gastos", 
                                                "C) Ahorros que cubren más de 6 meses de gastos"])
            
            # Botón para guardar las respuestas
            if st.button("Guardar respuestas"):
                guardar_datos(new_user_name, monthly_income[0], debt_percentage[0], credit_experience[0], savings_investments[0])
                st.write("Las respuestas han sido guardadas exitosamente.")
                
                # Ejecutar la subrutina para actualizar los datos
                actualizar_datos()
                st.write("Los datos han sido actualizados y guardados en 'Datos_actualizados.csv'.")
                
                # Evaluar la estabilidad económica del usuario
                resultado_evaluacion = evaluar_estabilidad(new_user_name)
                st.write(f"Evaluación de estabilidad económica: {resultado_evaluacion}")
                
                # Obtener una estrategia financiera basada en el resultado de evaluación
                strategy_chain = LLMChain(llm=llm, prompt=strategy_prompt_template)
                strategy_response = strategy_chain.run(evaluation_result=resultado_evaluacion)
                
                # Mostrar la estrategia recomendada
                st.write("Estrategia financiera recomendada:")
                st.write(strategy_response)
