import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Dasb')
st.write('mi primera data app!')

# crear un botón para histograma
hist_button = st.button('Construir histograma')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear un botón para histograma
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un graf de dispersion
    fig2 = px.scatter(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # crear un graf de dispersion
    fig3 = px.scatter(car_data, x="model_year")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)
