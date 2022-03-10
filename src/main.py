from csv_converter import to_df
from api_call import peticion
import pandas as pd

# Hace la peticion al api de openweathermap con los tokens dados
def peticion_api(columna1, columna2):
    list = []
    for index, row in df.iterrows():
        elementos1 = row[columna1].split(",")
        elementos2 = row[columna2].split(",")
        list.append(f"ORIGEN: {peticion(elementos1[0], elementos1[1])} - DESTINO: {peticion(elementos2[0], elementos2[1])}")
    return list

# Manipula los datos dados para tomar solo los necesarios
df = to_df("data/dataset1.csv").drop_duplicates()
df['Origen'] = df['origin_latitude'].astype(str) + ',' + df['origin_longitude'].astype(str)
df['Destino'] = df['destination_latitude'].astype(str) + ',' + df['destination_longitude'].astype(str)
df.drop(columns=['origin', 'destination', 'origin_longitude', 'origin_latitude', 'destination_latitude', 'destination_longitude'], inplace=True)
df.to_csv("data/usable_data.csv")

resp = peticion_api("Origen", "Destino")
resp_cformato = '\n'.join([str(x) for x in resp])
print(resp_cformato)
