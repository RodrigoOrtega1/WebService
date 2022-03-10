import csv
import pandas as pd

# Clase que implementa un convertidor de archivo csv a diccionario de python

# Convierte un csv a DataFrame de la libreria 'pandas'
def to_df(doc_name):
    df = pd.read_csv(doc_name)
    return df

# Convierte un documento csv a diccionario de python
def to_dic(doc_name, row1, row2):
    dic = {}
    with open(doc_name, mode = 'r') as inp:
        reader = csv.reader(inp)
        dic = {rows[row1]:rows[row2] for rows in reader}
    return dic

data = to_df('dataset1.csv')
data['Origen'] = data['origin_latitude'].astype(str) + ',' + data['origin_longitude'].astype(str)
data['Destino'] = data['destination_latitude'].astype(str) + ',' + data['destination_longitude'].astype(str)
del data['origin_latitude']
del data['origin_longitude']
del data['destination_latitude']
del data['destination_longitude']
print(data)
a = data.drop_duplicates()
print(a)
a.to_csv('hola.csv')
# diccionario = data.to_dict()
# print(diccionario)
