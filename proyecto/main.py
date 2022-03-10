from csv_converter import to_df
from api_call import peticion
import pandas as pd

def peticion_api(columna1, columna2):
    list = []
    count = 0
    for index, row in df.iterrows():
        elementos1 = row[columna1].split(",")
        # print(elementos1)
        elementos2 = row[columna2].split(",")
        # print(elementos2)
        # count += 1
        # print(count)
        # print("---------------------")
        # list.extend(peticion(elementos1[0], elementos1[1]) + "," + peticion(elementos2[0], elementos2[1]))
        list.append(f"Origen: {peticion(elementos1[0], elementos1[1])}, Destino: {peticion(elementos2[0], elementos2[1])}")
    return list

df = to_df('dataset1.csv').drop_duplicates()
# Une las columnas origin_latitude y origin_longitude en la columna Origen
df['Origen'] = df['origin_latitude'].astype(str) + ',' + df['origin_longitude'].astype(str)

# Une las columnas destination_latitude y destination_longitude en la columna Destino
df['Destino'] = df['destination_latitude'].astype(str) + ',' + df['destination_longitude'].astype(str)

# Quita las columnas que contienen datos innecesarios al funcionamiento del programa
df.drop(columns=['origin', 'destination', 'origin_longitude', 'origin_latitude', 'destination_latitude', 'destination_longitude'], inplace=True)

df.to_csv("functional_data.csv")

list = peticion_api("Origen", "Destino")
print(list)
print(len(list))

# s = pd.DataFrame([dic]).T
# print(s)
