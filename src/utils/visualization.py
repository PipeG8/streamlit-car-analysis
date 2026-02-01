import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def plot_fuel_type_count(df: pd.DataFrame):


    """""


    Genera un gráfico de barras que muestra la cantidad de vehículos por tipo de combustible


    :param df: DataFrame con los datos de vehículos
    :return: Figura de Matplotlib con el gráfico generado


    """


    fig, ax = plt.subplots(figsize=(8, 5))


    sns.countplot(x=df["fuel_type"], palette="viridis", ax=ax)

    
    ax.set_xlabel("Tipo de Combustible")


    ax.set_ylabel("Cantidad de Vehículos")


    ax.set_title("Cantidad de Vehículos por Tipo de Combustible")


    ax.grid()


    return fig

def plot_price_distribution(df: pd.DataFrame):

    """

    Genera un histograma que muestra la distribución de precios de los vehículos.

    :param df: DataFrame con los datos de vehículos.

    :return: Figura de Matplotlib con el gráfico generado.

    """

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.histplot(df["price"], bins=30, kde=True, color="blue", ax=ax)

    ax.set_xlabel("Precio")

    ax.set_ylabel("Frecuencia")

    ax.set_title("Distribución de Precios de los Vehículos")

    ax.grid()

    return fig