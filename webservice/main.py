from csv_converter import a_df
from api_call import peticion
import pandas as pd

def short_dataset(dataset):
    '''
    Toma un archivo .csv
    Regresa un DataFrame con la informacion necesaria
    :param dataset: Un archivo .csv
    :return: Un DataFrame con la informacion necesaria
    '''
    df = a_df(dataset).drop_duplicates()
    df['Origen'] = df['origin_latitude'].astype(str) + ',' + df['origin_longitude'].astype(str)
    df['Destino'] = df['destination_latitude'].astype(str) + ',' + df['destination_longitude'].astype(str)
    df.drop(columns=['origin', 'destination', 'origin_longitude', 'origin_latitude', 'destination_latitude', 'destination_longitude'], inplace=True)
    return df

def peticion_api(df, columna1, columna2):
    '''
    Toma dos columnas de un DataFrame
    Regresa una lista con la informacion de OpenWeatherMap
    :param df: Un DataFrame
    :param columna1: Una columna del DataFrame
    :param columna2: Una columna del DataFrame
    :return list: Una lista con informacion de OpenWeatherMap
    '''
    if type(columna1) is not str or type(columna2) is not str:
        raise ValueError("El nombre de la columna debe estar en una cadena")
    list = []
    for index, row in df.iterrows():
        elementos1 = row[columna1].split(",")
        elementos2 = row[columna2].split(",")
        list.append(f"ORIGEN: {peticion(elementos1[0], elementos1[1])} - DESTINO: {peticion(elementos2[0], elementos2[1])}")
    return list

def to_str(list):
    '''
    Toma una lista
    Regresa una cadena de la lista
    :param list: Una lista
    :return: Una cadena de la lista
    '''
    if type(list) is not list:
        raise ValueError("Esta funcion solo admite listas")
    return '\n'.join([str(x) for x in list])

def main():
    df = short_dataset("data/dataset1.csv")
    print("Llamando al API... (puede tardar)")
    resp = peticion_api(df, "Hola", "Destino")
    resp_str = to_str(resp)
    print("Resultado:")
    print(resp_str)
    print("Programa completo.")

if __name__ == '__main__':
    main()
