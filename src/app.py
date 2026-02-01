import streamlit as st
import pandas as pd

from utils.data_processing import clean_data
from utils.visualization import (
    plot_price_distribution,
    plot_fuel_type_count
)

# -----------------------------
# 1. Cargar los datos
# -----------------------------
url = "https://raw.githubusercontent.com/anfagudelogo-tpt/datasets/refs/heads/main/car_price_dataset.csv"

df = pd.read_csv(url)
df = clean_data(df)

# -----------------------------
# 2. Título y descripción
# -----------------------------
st.title("Análisis Descriptivo de Vehículos")

st.write(
    "Esta aplicación permite explorar un dataset de vehículos, "
    "proporcionando estadísticas y visualizaciones interactivas."
)

# -----------------------------
# 3. Resumen estadístico
# -----------------------------
st.subheader("Resumen Estadístico de los Datos")

tabla_resumen = df.describe()
st.dataframe(tabla_resumen)

# -----------------------------
# 4. Gráficos generales
# -----------------------------
st.subheader("Visualizaciones Generales")

fig1 = plot_price_distribution(df)
st.pyplot(fig1)

fig2 = plot_fuel_type_count(df)
st.pyplot(fig2)

# -----------------------------
# 5. Filtro por marca
# -----------------------------
st.subheader("Análisis por Marca")

selected_brand = st.text_input(
    "Ingrese una marca de vehículo para filtrar los datos:"
)

if st.button("Generar Análisis"):
    df_filtered = df[df["brand"] == selected_brand]

    if df_filtered.empty:
        st.warning("Ingrese una marca válida.")
    else:
        st.write(
            f"📊 Datos filtrados para la marca: **{selected_brand}**"
        )

        st.dataframe(df_filtered.describe())

        fig_filtered = plot_price_distribution(df_filtered)
        st.pyplot(fig_filtered)
