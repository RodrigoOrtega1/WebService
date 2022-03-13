from csv_converter import to_df
from api_call import peticion
import pandas as pd

# Manipula los datos dados para tomar solo los necesarios
def short_dataset(dataset):
    df = to_df(dataset).drop_duplicates()
    df['Origen'] = df['origin_latitude'].astype(str) + ',' + df['origin_longitude'].astype(str)
    df['Destino'] = df['destination_latitude'].astype(str) + ',' + df['destination_longitude'].astype(str)
    df.drop(columns=['origin', 'destination', 'origin_longitude', 'origin_latitude', 'destination_latitude', 'destination_longitude'], inplace=True)
    return df

def peticion_api(df, columna1, columna2):
    """
    Toma dos columnas en formato DataFrame y con sus datos llama al API de
    openweathermap
    Params:
        df          - El DataFrame a usar
        columna1    - El nombre de la primera columna por la que se quiere iterar
        columna2    - El nombre de la segunda columna por la que se quiere iterar
    Returns:
        list        - La lista con la respuesta del api
    """
    list = []
    for index, row in df.iterrows():
        elementos1 = row[columna1].split(",")
        elementos2 = row[columna2].split(",")
        list.append(f"ORIGEN: {peticion(elementos1[0], elementos1[1])} - DESTINO: {peticion(elementos2[0], elementos2[1])}")
    return list

def to_list(df):
    return '\n'.join([str(x) for x in df])

df = short_dataset("data/dataset1.csv")
print("Llamando al API... (puede tardar)")
resp = peticion_api(df, "Origen", "Destino")
resp_lst = to_list(resp)
print("Resultado:")
print(resp_lst)
print("Programa completo.")
