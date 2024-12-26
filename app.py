import pandas as pd
import plotly.express as px
import streamlit as st
import plotly

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# mostrar un encabezado
st.header('Analisis de datos de anuncios de venta de coches')

st.write('Encabezado de los datos')
st.dataframe(car_data.head())  # imprimir primeros renglones

# crear un botón para histograma
hist_button_1 = st.button('Construir histograma de tipo de auto')

if hist_button_1:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="type")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear un botón para histograma
scatter_button = st.button('Construir gráfico de dispersión de kilometraje')

if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un graf de dispersion
    fig2 = px.scatter(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

# crear una casilla de verificación
build_scatter = st.checkbox('Construir un diagrama de dispersion de modelo de auto')

if build_scatter:  # si la casilla de verificación está seleccionada
    st.write('Diagrama de dispersión de modelo de auto')

    # crear un graf de dispersion
    fig3 = px.scatter(car_data, x="model_year")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)


build_histogram_2 = st.checkbox('Construir un histograma de precio')

if build_histogram_2:
    st.write('histograma para el precio')
    fig4 = px.histogram(car_data, x="price")
    st.plotly_chart(fig4, use_container_width=True)


# git status  para ver todos los cambios
# git add . para agregar todos los cambios
# git commit -m "mensaje" para hacer un commit
# git push para subir los cambios
# git pull para bajar los cambios
# git clone para clonar un repositorio
# git branch para ver las ramas
