import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Proyecto 7')

hist_checkbox = st.checkbox('Construir histograma')

if hist_checkbox:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox = st.checkbox('Construir grafico de dispersion.')

if scatter_checkbox:
    st.write('Creacion de un grafico de dispersion (odometer vs price)')
    scatter_fig = px.scatter(
        car_data, x='odometer', y='price', title='Relacion entre kilometros y precio')
    st.plotly_chart(scatter_fig, use_container_width=True)
