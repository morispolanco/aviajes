import streamlit as st
import requests

# Función para realizar consultas a la API de DashScope
def query_dashscope(prompt):
    api_key = st.secrets["DASHSCOPE_API_KEY"]
    url = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "qwen-plus",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Configuración de la página
st.set_page_config(page_title="Agencia de Viajes", layout="wide")
st.title("Aplicaciones Útiles para Agencias de Viajes")

# Barra lateral con opciones
st.sidebar.title("Menú de Utilidades")
option = st.sidebar.selectbox(
    "Selecciona una utilidad:",
    [
        "1. Consulta de Destinos Populares",
        "2. Generador de Itinerarios",
        "3. Calculadora de Presupuesto",
        "4. Traductor de Frases Útiles",
        "5. Clima en Destino",
        "6. Recomendador de Hoteles",
        "7. Conversor de Monedas",
        "8. Planificador de Actividades",
        "9. Guía Cultural",
        "10. Chat con Asistente Virtual",
    ],
)

# Lógica para cada opción con botón de ejecución
if option == "1. Consulta de Destinos Populares":
    st.header("Consulta de Destinos Populares")
    if st.button("Ejecutar"):
        destinos = query_dashscope("¿Cuáles son los destinos turísticos más populares del mundo?")
        st.write(destinos)

elif option == "2. Generador de Itinerarios":
    st.header("Generador de Itinerarios")
    destino = st.text_input("Ingresa el destino:")
    if st.button("Ejecutar") and destino:
        itinerario = query_dashscope(f"Genera un itinerario de 5 días para visitar {destino}.")
        st.write(itinerario)

elif option == "3. Calculadora de Presupuesto":
    st.header("Calculadora de Presupuesto")
    presupuesto = st.number_input("Ingresa tu presupuesto total:", min_value=0, step=100)
    if st.button("Ejecutar") and presupuesto > 0:
        distribucion = query_dashscope(f"Distribuye {presupuesto} USD en vuelos, alojamiento, comida y actividades.")
        st.write(distribucion)

elif option == "4. Traductor de Frases Útiles":
    st.header("Traductor de Frases Útiles")
    frase = st.text_input("Ingresa la frase a traducir:")
    idioma = st.text_input("Ingresa el idioma objetivo:")
    if st.button("Ejecutar") and frase and idioma:
        traduccion = query_dashscope(f"Traduce '{frase}' al {idioma}.")
        st.write(traduccion)

elif option == "5. Clima en Destino":
    st.header("Clima en Destino")
    ciudad = st.text_input("Ingresa la ciudad:")
    if st.button("Ejecutar") and ciudad:
        clima = query_dashscope(f"¿Cómo es el clima en {ciudad}?")
        st.write(clima)

elif option == "6. Recomendador de Hoteles":
    st.header("Recomendador de Hoteles")
    destino_hotel = st.text_input("Ingresa el destino:")
    if st.button("Ejecutar") and destino_hotel:
        hoteles = query_dashscope(f"Recomienda hoteles económicos en {destino_hotel}.")
        st.write(hoteles)

elif option == "7. Conversor de Monedas":
    st.header("Conversor de Monedas")
    cantidad = st.number_input("Ingresa la cantidad:", min_value=0, step=1)
    moneda_origen = st.text_input("Moneda origen (ej. USD):")
    moneda_destino = st.text_input("Moneda destino (ej. EUR):")
    if st.button("Ejecutar") and cantidad > 0 and moneda_origen and moneda_destino:
        conversion = query_dashscope(f"Convierte {cantidad} {moneda_origen} a {moneda_destino}.")
        st.write(conversion)

elif option == "8. Planificador de Actividades":
    st.header("Planificador de Actividades")
    destino_actividades = st.text_input("Ingresa el destino:")
    if st.button("Ejecutar") and destino_actividades:
        actividades = query_dashscope(f"Sugiere actividades para hacer en {destino_actividades}.")
        st.write(actividades)

elif option == "9. Guía Cultural":
    st.header("Guía Cultural")
    pais = st.text_input("Ingresa el país:")
    if st.button("Ejecutar") and pais:
        cultura = query_dashscope(f"Describe la cultura y costumbres de {pais}.")
        st.write(cultura)

elif option == "10. Chat con Asistente Virtual":
    st.header("Chat con Asistente Virtual")
    pregunta = st.text_input("Haz una pregunta:")
    if st.button("Ejecutar") and pregunta:
        respuesta = query_dashscope(pregunta)
        st.write(respuesta)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Desarrollado por Moris Polanco")
